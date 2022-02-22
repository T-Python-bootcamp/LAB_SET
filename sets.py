# Ahmed visited those cities {"Hail", "Riyadh", "Dubai"}  
# and Faris visited {"Riyadh", "Jizan", "Abu Dhabi", "Hail"} .

ahmedVisited = {"Hail", "Riyadh", "Dubai"}
faresVisited = {"Riyadh", "Jizan", "Abu Dhabi", "Hail"}

allCities = ahmedVisited | faresVisited
print(allCities)


insCities = ahmedVisited & faresVisited
print(insCities)

difCiti = faresVisited - ahmedVisited
print(difCiti)