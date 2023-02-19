# creare una funzione che prenda come input una lista di stringhe e restituisca un dizionario con chiavi date dalle varie stringhe e valori dati dalle stringhe scritte al contrario (es. "ciao": "oaic")
def list_into_dict(ls):
    my_dict = {}

    for word in ls:
        my_dict[word] = "".join(reversed(list(word)))
    
    return my_dict


print(list_into_dict(["do", "re", "mi", "fa"]))
