'''
3. Weather Data Tracker
Concepts: 3D Lists · While Loop · Indexing · Data Types
Problem Statement:
• A weather agency tracks data for 3 cities, across 4 seasons, recording 3 values each: [temperature,
humidity, rainfall].
• Store all data in a 3D list: [city][season][measurement].
• City names: ['Tokyo', 'Osaka', 'Kyoto']
• Season names: ['Spring', 'Summer', 'Autumn', 'Winter']
• Use a while loop to print the full weather report for each city and season.
• Find the hottest season (highest temperature) for each city.
• Find the city with the highest total annual rainfall.
Acceptance Criteria:
• Define a 3D list with shape [3][4][3].
• Use index access: weather[c][s][0] for temp, [1] for humidity, [2] for rainfall.

• Use nested while loops with index for all traversals — no sum() or max().
• Track hottest season per city using a variable reset each city iteration.
• Track total rainfall per city using an accumulator variable.
Expected Output:
==========================================
WEATHER REPORT
==========================================
City: Tokyo
Spring | Temp: 18C Humidity: 60% Rain: 120mm
Summer | Temp: 34C Humidity: 80% Rain: 180mm
Autumn | Temp: 22C Humidity: 65% Rain: 140mm
Winter | Temp: 8C Humidity: 50% Rain: 60mm
Hottest season: Summer (34C)
City: Osaka
Spring | Temp: 20C Humidity: 62% Rain: 110mm
Summer | Temp: 36C Humidity: 82% Rain: 170mm
Autumn | Temp: 24C Humidity: 64% Rain: 130mm
Winter | Temp: 9C Humidity: 52% Rain: 55mm
Hottest season: Summer (36C)
City: Kyoto
Spring | Temp: 19C Humidity: 61% Rain: 105mm
Summer | Temp: 35C Humidity: 79% Rain: 165mm
Autumn | Temp: 23C Humidity: 63% Rain: 125mm
Winter | Temp: 7C Humidity: 51% Rain: 50mm
Hottest season: Summer (35C)
City with highest annual rainfall: Tokyo (500mm)
'''
weather = [
    [#Tokyo
        [18, 60, 120],
        [34, 80, 180],
        [22, 65, 140],
        [8, 50, 60]
    ],
    [#Osaka
        [20, 62, 110],
        [36, 82, 170],
        [24, 64, 130],
        [9, 52, 55]
    ],
    [#Kyoto
        [19, 61, 105],
        [35, 79, 165],
        [23, 63, 125],
        [7, 51, 50]
    ]

]

cities = ["Tokyo", "Osaka", "Kyoto"]
seasons = ["Spring", "Summer", "Autumn", "Winter"]

print("==========================================")
print("WEATHER REPORT")
print("==========================================")


c = 0
highest_rainfall_city = " "
highest_rainfall_amount = 0

while c <   len(cities):
    print(f"City: {cities[c]}")

    s = 0

    hottest_temp = weather[c][0][0]
    hottest_season = seasons[0]
    total_rainfall = 0

    while s < len(seasons):

         temp = weather[c][s][0]
         humidity = weather[c][s][1]
         rainfall = weather[c][s][2]
         print(f"{seasons[s]}  | Temp: {temp}C Humidity: {humidity}%  Rain:{rainfall}mm")

         if temp > hottest_temp:
             hottest_temp = temp
             hottest_season = seasons[s]
    
         total_rainfall += rainfall
         s += 1
    print(F"Hottest season: {hottest_season} ({hottest_temp}C)")

    if total_rainfall > highest_rainfall_amount:
            highest_rainfall_amount = total_rainfall
            highest_rainfall_city = cities[c]
    c +=1
print(f"City with highest annual rainfall: {highest_rainfall_city} {highest_rainfall_amount}mm")


    