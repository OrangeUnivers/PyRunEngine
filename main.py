import os.path
import json
import warnings
import time
import math

# check if neccesary files are available
if not os.path.exists("map"):
    raise Exception("'map' folder is Missing!")
if not os.path.isfile("settings.json"):
    raise Exception("'settings.json' is Missing!")
with open("settings.json", "r") as file:
    settings = json.load(file)

if not "maps" in settings:
    raise Exception("The 'maps' Key is missing in 'settings.json'!")
if len(settings["maps"]) == 0:
    raise Exception("There is no map to load! Add a map to the 'maps' Key in 'settings.json.")
maps = settings["maps"]
missingMaps = []
for index in range(len(maps)):
    maps[index] = maps[index].replace("\n", "")
    if not os.path.isfile("map/"+maps[index]+".json"):
        missingMaps.append(maps[index])
if len(missingMaps) > 0:
    raise Exception("A map is missing! The missing maps are:\n- "+"\n- ".join(missingMaps))

mapFiles = {}

for index in range(len(maps)):
    with open("map/"+maps[index]+".json", "r") as file:
        mapFiles[maps[index]] = json.load(file)

# for map in maps:
#     for index in range(len(mapFiles[map])):
#         mapFiles[map][index] = mapFiles[map][index].replace("\n", "")
if not "firstMap" in settings:
    warnings.warn("'firstMap' Key is missing in 'settings.json'. Using default value: " + maps[0] + ".")
    settings["firstMap"] = maps[0]
if not os.path.isfile("map/"+settings["firstMap"]+".json"):
    raise Exception("The 'firstMap' Key '"+settings["firstMap"]+"' in 'settings.json' isn't available as a map.")
def getLang(key: str, lang: str = None) -> str:
    if lang is None:
        lang = settings["fallbackLang"]
    if lang in settings and key in settings[lang]:
        return settings[lang][key]
    fallback_langs = settings.get("fallbackLang", [])
    for fallback in fallback_langs:
        if fallback in settings and key in settings[fallback]:
            return settings[fallback][key]
    return key
def formatText(text: str):
    formatTable = {
        "0": "\x1b[30m",
        "2": "\x1b[32m",
        "7": "\x1b[2m",
        "9": "\x1b[34m",
        "a": "\x1b[92m"
    }
def getWidth(percentage: float = None) -> int:
    if percentage:
        return int(os.get_terminal_size()[0] // percentage)
    return int(os.get_terminal_size()[0])
def getHeight(percentage: float = None) -> int:
    if percentage:
        return int(os.get_terminal_size()[1] // percentage)
    return int(os.get_terminal_size()[1])
print("sadads")
# def printer(x = 1):
#     for i in range(x):
#         print("                                                                                                                                                                                           ")

# def overwrite(lines = int):
#     print("\033[" + str(lines) + "A",end="\x1b[2K")
#     printer(lines)
#     print("\033[" + str(lines) + "A",end="\x1b[2K")
# print("Welcome to Invest")
# print("In Invest you could look if you could live a life on where you are relieing completly on investing i cryptocurrentcys")
# printer()
# input("> ")
# overwrite(4)
# input()
while True:
    print("This program will remove eveything in the command history of this session. Do you want to open anyways? (Y/n)")
    userInput = input("- ")
    if userInput == "n" or userInput == "N":
        exit()
    elif userInput == "y" or userInput == "Y":
        break
    print("\033[2A", end="\x1b[2K")
    print("")
    print(" "* (2+len(userInput)))
    print("\033[2A", end="\x1b[2K")
# Main Loop
firstRun = True
lastSizeX = None
lastSizeY = None
savedPositions = {"x": [], "y": []}
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    lastSizeX = getWidth()
    lastSizeY = getHeight()
    savedPositions["x"].append(getWidth())
    savedPositions["y"].append(getHeight())
    # for i in range(int(round(((getHeight() - round((getHeight() / 1.7) - 2, 0)) / 2), 0))):
    #     print("")
    # print(str(" "*(int(round(((getWidth() - round((getWidth() / 1.7) - 2, 0)) / 2), 0)))) + "╭" + str("─" * int(round((getWidth() / 1.7) - 2, 0))) + "╮")
    # for i in range(int(round((getHeight() / 1.7) - 2, 0))):
    #     print(str(" "*(int(round(((getWidth() - round((getWidth() / 1.7) - 2, 0)) / 2), 0)))) + "│" + str(" " * int(round((getWidth() / 1.7) - 2, 0))) + "│")
    # print(str(" "*(int(round(((getWidth() - round((getWidth() / 1.7) - 2, 0)) / 2), 0)))) + "╰" + str("─" * int(round((getWidth() / 1.7) - 2, 0))) + "╯")
    # for i in range(int(round(((getHeight() - round((getHeight() / 1.7) - 2, 0)) / 2), 0))):
    #     print("")
    print(settings["minSceneSize"][0] > getWidth(1.7))
    print(getHeight(1.7) >= settings["minSceneSize"][1])
    print(getHeight(1.7))
    print(settings["minSceneSize"][1])
    if settings["minSceneSize"][0] > getWidth(1.7) and getHeight(1.7) >= settings["minSceneSize"][1]:
        for i in range((getHeight() - getHeight(1.7) - 2) // 2):
            print("")
        print(str("─" * getWidth()))
        for i in range(getHeight(1.7)):
            print("")
        print(str("─" * getWidth()))
        for i in range((getHeight() - getHeight(1.7) - 2) // 2):
            print("")
        input("? ")
        continue
    if settings["minSceneSize"][1] > getHeight(1.7) and getWidth(1.7) >= settings["minSceneSize"][0]:
        for i in range(getHeight()-1):
            print(str(" "*((getWidth() - getWidth(1.7) - 1) // 2)) + "│" + str(" " * getWidth(1.7)) + "│")
        input("? ")
        continue
    if settings["minSceneSize"][0] > getWidth(1.7) and getHeight(1.7) >= settings["minSceneSize"][1]:
        for i in range((getHeight() - getHeight(1.7) - 2) // 2):
            print("")
        print(str("─" * getWidth()))
        for i in range(getHeight(1.7)):
            print("")
        print(str("─" * getWidth()))
        for i in range((getHeight() - getHeight(1.7) - 2) // 2):
            print("")
        input("? ")
        continue
    if settings["minSceneSize"][1] > getHeight(1.7) and getWidth(1.7) > settings["minSceneSize"][0]:
        for i in range(getHeight()-1):
            print(str(" "*((getWidth() - getWidth(1.7) - 1) // 2)) + "│" + str(" " * getWidth(1.7)) + "│")
        input("? ")
        continue
    for i in range((getHeight() - getHeight(1.7) - 2) // 2):
        print(" " * getWidth())
    print(str(" "*((getWidth() - getWidth(1.7) - 1) // 2)) + "╭" + str("─" * getWidth(1.7)) + "╮")
    for i in range(getHeight(1.7)):
        print(str(" "*((getWidth() - getWidth(1.7) - 1) // 2)) + "│" + str(" " * getWidth(1.7)) + "│")
    print(str(" "*((getWidth() - getWidth(1.7) - 1) // 2)) + "╰" + str("─" * getWidth(1.7)) + "╯")
    for i in range((getHeight() - getHeight(1.7) - 2) // 2 + (0 if (getHeight() - getHeight(1.7) - 2) % 2 == 0 else 1) - 1):
        print("")
    userInput = input(" > ")
    if userInput == "exit":
        break
    elif userInput == "refresh":
        continue
    elif userInput == "debug":
        print("Xs: " + ", ".join(str(x) for x in savedPositions["x"]) + "; Ys: " + ", ".join(str(y) for y in savedPositions["y"]))
        break
