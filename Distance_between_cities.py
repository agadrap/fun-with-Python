# This will calculate distance between two cities
# and show you coordinates for them.
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

while True:
    execute = input("Want to know how far is city_1 from city_2? Y/N")
    if execute.upper()[0] == 'Y':
        change_city = True
    else:
        break

    while change_city == True:
        city_1 = input("\nCity no1: ")
        city_2 = input("City no2: ")
        #COORDINATES

        geolocator = Nominatim(user_agent="gold_for_the_bold")
        location1 = geolocator.geocode(city_1)
        location2 = geolocator.geocode(city_2)

        print(f"\nCoordinates for {city_1}:")
        city_1_coord = (location1.latitude, location1.longitude)
        print(city_1_coord)

        print(f"\nCoordinates for {city_2}:")
        city_2_coord = (location2.latitude, location2.longitude)
        print(city_2_coord)

        # DISTANCE
        print(f"\nThe distance between {city_1} and {city_2} in miles:")
        print(geodesic(city_1_coord, city_2_coord).miles)

        miles_to_km = (geodesic(city_1_coord, city_2_coord).miles)*1.609344
        print(f"In km:   {miles_to_km}")


        again = input("Again? Y/N")

        if again.upper()[0] == 'Y':
            change_city = True
        else:
            break
