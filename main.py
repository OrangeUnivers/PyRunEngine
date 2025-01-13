import os.path
import json
import warnings
import colorama

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

print(colorama.Fore.GREEN + "He██llo")
print(colorama.Fore.LIGHTGREEN_EX + "He██llo")