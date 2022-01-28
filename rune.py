#!/usr/bin/python3

import sys
import random
import codecs

def help():
  global defnb
  print()
  print("rune diplays runes in differents formats")
  print("")
  print("parameters :")
  print(f"  actions : get [nb] | random [nb = {defnb}]")
  print("  formats : text | line | tab | list | csv | json | xml | html")
  print("  options : full / all / upper / rot13")
  print()
  print("made with Python3 - 2022 Stef Code - More info at https://runx.fr")
  print()

runes = [
    ["Fehu"     ,"Prospérité" ,"Richesse"]    , ["Uruz"     ,"Force"      ,"Santé"]
  , ["Thurisaz" ,"Défense"    ,"Violence"]    , ["Ansuz"    ,"Conscience" ,"Connaissance"]
  , ["Raidho"   ,"Voyage"     ,"Roue"]        , ["Kenaz"    ,"Ouverture"  ,"Feu"]
  , ["Gebo"     ,"Rencontre"  ,"Association"] , ["Wunjo"    ,"Victoire"   ,"Bonheur"]
  , ["Hagalaz"  ,"Bouleversement","Problème"] , ["Naudhiz"  ,"Epreuve"    ,"Contrainte"]
  , ["Isa"      ,"Immobilité" ,"Blocage"]     , ["Jera"     ,"Causalité"  ,"Récolte"]
  , ["Eihwaz"   ,"Endurance"  ,"Cycle"]       , ["Perthro"  ,"Mystère"    ,"Destin"]
  , ["Algiz"    ,"Protection" ,"Confiance"]   , ["Sowilo"   ,"Energie"    ,"Succès"]
  , ["Tiwaz"    ,"Courage"    ,"Justice"]     , ["Berkano"  ,"Maternité"  ,"Communauté"]
  , ["Ehwaz"    ,"Progrès"    ,"Mouvement"]   , ["Mannaz"   ,"Humanité"   ,"Intelligence"]
  , ["Laguz"    ,"Fluidité"   ,"Eau"]         , ["Ingwaz"   ,"Fertilité"  ,"Graine"]
  , ["Dagaz"    ,"Lumière"    ,"Savoir"]      , ["Othala"   ,"Héritage"   ,"Patrimoine"]
]

maxnb = 24 # Maximum number of results
defnb = 5  # Default number of results

(action, format) = [""] * 2
(all, full, sort, upper, rot13) = [False] * 5

for arg in sys.argv[1:]:
  if (not action):
    if arg in ("random", "get", "help"):
      action = arg
  if (not format):
    if arg in ("text", "line", "tab", "csv", "list", "json", "xml", "html"):
      format = arg
  if arg == "all":
    all = True
  if arg == "full":
    full = True
  elif arg == "sort":
    sort = True
  elif arg == "upper":
    upper = True
  elif arg == "rot13":
    rot13 = True

if not action:
  action = "random"
if not format:
  format = "text"

# print(f"Action: {action}, Format: {format}")

ids = []
if action == "random":
  nb = 0
  if all:
    nb = maxnb
  for arg in sys.argv[1:]:
    if (not nb):
      try:
        nb = int(arg)
        if nb <= 0:
          nb = 0
        elif nb > maxnb:
          nb = maxnb
      except:
        pass
  if nb == 0:
    nb = defnb
  for i in range(len(runes)):
    ids.append(i+1)
  random.shuffle(ids)
  ids = ids[:nb]
elif action == "get":
  if all:
    for i in range(maxnb):
      ids.append(i+1)
  else:
    for arg in sys.argv[1:]:
      if (len(ids) < maxnb):
        try:
          id = int(arg)
          if id in range(1,len(runes)+1) and id not in ids:
            ids.append(id)
        except:
          pass
  if not ids:
    ids.append(random.randint(1,len(runes)))

if action == "help":
  help()
else:
  # Begin of runes
  if sort:
    ids.sort()
  if (format in ["list"]):
    print("(", end="")
  elif (format in ["json"]):
    print("[", end="")
  elif (format in ["xml"]):
    print("<?xml version=\"1.0\"?>")
    print("<runes>")
  elif (format in ["html"]):
    print("<table>")

  # Loop for runes
  for i in range(len(ids)):
    rune = runes[ids[i]-1][0]
    prim = runes[ids[i]-1][1]
    sec = runes[ids[i]-1][2]
    if upper:
      rune = rune.upper()
      prim = prim.upper()
      sec = sec.upper()
    if rot13:
       rune = codecs.encode(rune, "rot_13")
       prim = codecs.encode(prim, "rot_13")
       sec = codecs.encode(sec, "rot_13")

    if format == "text":
      if full:
        print(rune, prim, sec)
      else:
        print(rune)

    if format == "line":
      if i > 0:
        print(" ", end="")
      if full:
        print(rune, prim, sec, end="")
      else:
        print(rune, end="")

    elif format == "tab":
      if (i > 0):
        print("\t", end="")
      if full:
        print(f"{rune}\t{prim}\t{sec}", end="")
      else:
        print(f"{rune}", end="")

    elif format == "csv":
      if full:
        print(f"{ids[i]},{rune},{prim},{sec}")
      else:
        print(f"{ids[i]},{rune}")

    elif format == "list":
      if (i > 0):
        print(", ", end="")
      if full:
        print(f"(\"{rune}\", \"{prim}\", \"{sec}\")", end="")
      else:
        print(f"\"{rune}\"", end="")

    elif format == "json":
      if (i > 0):
        print(", ", end="")
      if full:
        print("\n  {"
          +f"\"id\":\"{ids[i]}\", \"name\":\"{rune}\""
          +f", \"prim\":\"{prim}\", \"sec\":\"{sec}\""
          +"}", end="")
      else:
        print("{"+f"\"id\":\"{ids[i]}\", \"name\":\"{rune}\""+"}", end="")

    elif format == "xml":
      print(f"  <rune id=\"{ids[i]}\">")
      print(f"    <name>{rune}</name>")
      if full:
        print(f"    <prim>{prim}</prim>")
        print(f"    <sec>{prim}</sec>")
      print(f"  </rune>")

    elif format == "html":
      print(f"  <tr>")
      print(f"    <td>{ids[i]}</td>")
      print(f"    <td>{rune}</td>")
      if full:
        print(f"    <td>{prim}</td>")
        print(f"    <td>{sec}</td>")
      print(f"  </tr>")

  # End of runes
  if (format in ["line", "tab"]):
    print()
  if (format in ["list"]):
    print(")")
  elif (format in ["json"]):
    if full:
      print()
    print("]")
  elif (format in ["xml"]):
    print("</runes>")
  elif (format in ["html"]):
    print("</table>")
