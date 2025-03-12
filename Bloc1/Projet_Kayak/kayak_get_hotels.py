# Projet Kayak
# Module de récupération des informations sur les hotels (par sraping) depuis le site de booking.com

import os 
import pandas as pd
import logging
import scrapy
from scrapy.crawler import CrawlerProcess

# récupération de liste de villes à partir d'un datafram précédement crée.
df_cities_geoloc = pd.read_csv("./data/df_cities_geoloc_save.csv", index_col = 0)
cities_name = df_cities_geoloc["city_name"]
cities_id = df_cities_geoloc["city_id"]

# cities_name = ["Toulouse", "Paris"] # for short tests
# cities_id = [10, 20] # for short tests

# création de list de urls booking à scrapper "une url par ville"
cities_url = ['https://www.booking.com/searchresults.fr.html?ss={}'.format(city_name) for city_name in cities_name]

# création de la sous classe de scrapy
class BookingSpider(scrapy.Spider):

    # Name of your spider
    name = "booking"

    def start_requests(self):
        for city_id, city_url in zip(cities_id, cities_url) :
             yield scrapy.Request(url = city_url, meta={"city_id" : city_id})

    def parse(self, response):
        city_id = response.meta.get("city_id")
        hotels = response.css("div.d4924c9e74 > div > div > div > div > a")                           
        for hotel in hotels:
            hotel_href = hotel.xpath("@href").extract_first()
            yield scrapy.Request(url=hotel_href, callback=self.parse_detail, meta={"city_id" : city_id})

    def parse_detail(self, response):
        city_id = response.meta.get("city_id")
        hotel_name = response.css("div.hotelchars > div > div > div > div > div > div > div > h2::text").get()
        hotel_adress = response.css("div.hotelchars > div > div > div > div > p > span::text").get().replace('\n', '')
        hotel_note = response.css("div.hotelchars > div > div > div > div > div > div > div > div > a > div > div > div > div::text").getall()[0].replace(",", ".")
        hotel_latlng = response.css("div.hotelchars > div > div > div > div > p > span > a").xpath("@data-atlas-latlng").extract_first()
        hotel_url = response.xpath("/html/head/link[22]").xpath("@href").extract_first()
        hotel_desc = response.css("div.hotelchars > div > div > div > div > div > div > div > div > p::text").getall()[1]

        return {"hotel_name" : hotel_name,
               "city_id" : city_id,
               "hotel_adress" : hotel_adress,
               "hotel_note" : float(hotel_note),
               "hotel_lat" : float(hotel_latlng.split(",")[0]),
               "hotel_lon" : float(hotel_latlng.split(",")[1]),
               "hotel_href" : hotel_url,
               "hotel_desc" : hotel_desc
               }

filename = "df_booking_hotels.json"
if filename in os.listdir('./'):
        os.remove('./data/' + filename)

process = CrawlerProcess(settings = {
    'USER_AGENT': 'Chrome/97.0',
    'LOG_LEVEL': logging.INFO,
    "FEEDS": {
        './data/' + filename: {"format": "json"}  
    },
    "FEED_EXPORT_ENCODING" : "utf-8"
})

process.crawl(BookingSpider)
process.start()