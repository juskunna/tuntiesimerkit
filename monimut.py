# kokoelmat kokoelman sisällä, esim. lista
temp_day_1 = [13.5, 16.4, 11.6, 11.3]
temp_day_2 = [12.1, 15.2, 11.9, 10.4]
temp_day_3 = [15.3, 17.6, 12.5, 11.6]

temperatures = [temp_day_1, temp_day_2, temp_day_3]

# Käsitellään päivät listassa
for day in temperatures:
    print("Käsitellään seuraava päivä!")
    
    # Käsitellään lämpötilat päivissä
    for temp in day:
        print(temp)