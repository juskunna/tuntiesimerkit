import var_dump as vd

# luodaan hotelli no. 1
hotel_1 = {
 "name": "Snow Line Hotels",
 "rating": 4.3,
 "wifi": True,
 "free_breakfast": True,
 "services": ["sauna", "meetings", "restaurant", "parking", "safaris"],
 "price_level": 4
}
# luodaan hotelli no. 2
hotel_2 = {
 "name": "North Ice Hostel",
 "rating": 3.5,
 "wifi": True,
 "free_breakfast": False,
 "services": ["sauna", "parking"],
 "price_level": 2
}
# asetetaan molemmat hotellit samaan listaan
hotels = [hotel_1, hotel_2]
# tulostetaan sisältö, käytetään var_dump -moduulia
#vd.var_dump(hotels)

#testholtel = hotels[0]
#vd.var_dump(testholtel)

# käydään läpi jokainen hotelli
for hotel in hotels:
    print(hotel['name'])

    # käydään läpi joka hotellin servicet yksi kerrallaan
    #for service in hotel['services']:
        # myös if-lausetta voi hyödyntää
        #if service == "restaurant":
         #   print("Hotellissa on ravintola")


    services = "\n" .join(hotel['services'])

    print(services)
    if "restaurants" in services:
    print("Hotellissa on ravintola.")