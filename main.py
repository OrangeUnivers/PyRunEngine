mapDir = open("map/mapsLoad.txt", "r")
maps = mapDir.readlines()
print(maps)
if len(maps) == 0:
    raise Exception("There is no map to load!")

for index in maps:
    print(index)