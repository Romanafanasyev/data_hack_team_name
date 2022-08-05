import json

# initialize all arguments
min_book_price = 100.0
max_book_price = 3000.0
title_len = 10

# loading config.json
jsonDataFile = open('data_hack_team_name/config.json', 'r')
jsonData = jsonDataFile.read()
dictData = json.loads(jsonData)

# update arguments values from config.json
if "Book" in dictData:
    print(dictData["Book"])
    if "price_min" in dictData["Book"]:
        min_book_price = dictData["Book"]["price_min"]

    if "price_max" in dictData["Book"]:
        max_book_price = dictData["Book"]["price_max"]

    if "title_len" in dictData["Book"]:
        max_book_price = dictData["Book"]["title_len"]

print(min_book_price, max_book_price, title_len)