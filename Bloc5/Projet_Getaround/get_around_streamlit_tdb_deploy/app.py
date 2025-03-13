import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
import os

# -----------------------------------------------------------------------------
def main():

    ###########################################################################
    st.title("Tableau de bord : GetAround")

    ###########################################################################
    st.header("Sommaire")
    st.markdown(
        r"""
            * Getaround projette de mettre en place un délai minimum entre 2 locations pour :
                * mieux respecter le début des locations
                * réduire de potentielles insatisfactions clients.
            
        """
    )

    ###########################################################################
    df = pd.read_excel("get_around_delay_analysis.xlsx", sheet_name="rentals_data")

    ###########################################################################
    st.subheader("Exploration des données")

    # Transformation en "str" des id
    df['rental_id'] = df['rental_id'].astype(str)
    df['car_id'] = df['car_id'].astype(str)
    df['previous_ended_rental_id'] = df['previous_ended_rental_id'].apply(lambda x: str(int(x)) if not pd.isna(x) else x)

    # Ajour de colonne au df
    # colonne Retard constaté sur la location précedente (quand cette location existe)
    df["previous_delay_at_checkout_in_minutes"] = df["previous_ended_rental_id"].apply(lambda id : id if pd.isna(id) else df[df["rental_id"] == id]["delay_at_checkout_in_minutes"].sum())

    ###########################################################################
    # Checkin type
    st.subheader("Mode de checkin")

    df_cnt = df["checkin_type"].value_counts()
    fig1 = px.pie(df_cnt, values = "count", names=df_cnt.index)
    st.plotly_chart(fig1, theme=None, use_container_width=True, key="1")
    
    st.markdown(
        """
            ### :orange[**Remarques :**]
            * 20% des checkin/out en mode connect
        """
    )

    ###########################################################################
    # State
    st.subheader("Statuts des locations")
 
    df_cnt = df["state"].value_counts()
    fig2 = px.pie(df_cnt, values = "count", names=df_cnt.index)
    st.plotly_chart(fig2, theme=None, use_container_width=True, key="2")

    st.markdown(
        """
            ### :orange[**Conclusion :**]
            * 15% des locations sont annulées
        """
    )

    ###########################################################################
    # Distribution des diff. entre fin de locations et location suivante
    st.subheader("Distribution des diff. de temps entre les fins des locations et les locations suivantes")
 
    df_cnt = df["time_delta_with_previous_rental_in_minutes"].value_counts()
    fig3 = px.bar(df_cnt, y = "count", x=df_cnt.index, labels=df_cnt.index)
    st.plotly_chart(fig3, theme=None, use_container_width=True, key="3")


    ###########################################################################
    # Distribution des diff. fin prévue et réel des location
    st.subheader("Distribution des diff. fin prévu et réel des location (hors avances et retard > 12H)")
 
    df_disp = df[(df["delay_at_checkout_in_minutes"] > 0) & (df["delay_at_checkout_in_minutes"] <= 720)]
    fig4 = px.histogram(df_disp, x="delay_at_checkout_in_minutes")
    st.plotly_chart(fig4, theme=None, use_container_width=True, key="4")


    ###########################################################################
    # création de dataframe : impacts en fct de seuil (locations impactés & retards couverts)
    # Seuils de 0 à 12h par tranche de 30mn
    df_impacts_seuil = pd.DataFrame()

    df_impacts_seuil["seuil"] = [s for s in range(0, 6*60+1, 30)]

    list_locs_impactees = []
    list_retards = [] 

    for seuil in df_impacts_seuil["seuil"] :

        nb_locs_impactees = ((df["time_delta_with_previous_rental_in_minutes"] < seuil)).sum()
        list_locs_impactees.append(nb_locs_impactees)
        
        nb_retards = ((df["previous_delay_at_checkout_in_minutes"] > seuil)).sum()
        list_retards.append(nb_retards)

    df_impacts_seuil["locs_impactees"] = list_locs_impactees
    df_impacts_seuil["locs_retards"] = list_retards

    # En fct de chaque seuil, potentiellement : le nombre de locations impactées et les retards couverts  
    st.subheader("""
                 Analyse des impacts en fonction des seuils :
                 - les locations impactées (si celles ne sont pas réalisé ultérieurement)
                 - les locations résiduelles restituées en retard (pouvant générer des insatisfactions client et/ou annulation)
                 """)

    fig5 = px.line(df_impacts_seuil, y = ["locs_impactees", "locs_retards"], x="seuil", labels=df_cnt.index, title="cheking_type = tous")
    st.plotly_chart(fig5, theme=None, use_container_width=True, key="5")

    st.markdown(
        """
            ### :orange[**Conclusion :**]
            * Un seuil de 1H serait un bon compromis entre :
            * - Un manque un gagner (~ 400 locs) induit par les locations impactées (si celles ne sont pas réalisées ultérieurement)
            * - Un risque d'insatisfaction et/ou annulation client (~ 400 locs) occasionnés par les stats des retards constatés  

        """
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    main()
    os.system(f"streamlit run dashboard.py --server.port={port} --server.enableCORS=true")
