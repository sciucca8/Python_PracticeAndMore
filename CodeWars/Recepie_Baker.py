def cakes(recipe, stock):
    rapporti = []

    for ingr in recipe:
        if ingr not in list(stock.keys()):
            return 0
        else:
            for stock_ingr in stock:
                if ingr == stock_ingr:
                    rapporti.append(int(stock[stock_ingr] / recipe[ingr]))

    return min(rapporti) 



print(cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}))