ahmed= {"Hail", "Riyadh", "Dubai"}
faris= {"Riyadh", "Jizan", "Abu Dhabi", "Hail"}
for union in ahmed | faris:
    print(union)
print("___________________________________")
for intersection in ahmed & faris:
    print(intersection)
print("___________________________________")
for farisVisit in faris - ahmed:
    print(farisVisit)