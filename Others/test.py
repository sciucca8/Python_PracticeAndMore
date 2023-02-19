def get_rainfall():
    dict1 = {}
    for i in range(4):
        City = input('City: ')

        if City in dict1.keys():
            dict1[City] += Rainfall

        Rainfall = input('Quantity of rain: ')

        dict1[City] = Rainfall
    
    return dict1