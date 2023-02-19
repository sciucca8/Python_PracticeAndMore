#creare una funzione che prenda come input due liste di stessa lunghezza e restituisca un dizionario con chiave e valori dati dagli elementi appaiati delle due liste
def zip_lists(ls1, ls2):
    dict_zip = {}

    for key, value in zip(ls1, ls2):
        dict_zip[key] = value
    
    return dict_zip

print(zip_lists(["cane", "formica", "ragno"], [4, 6, 8]))
 