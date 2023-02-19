def rgb(r, g, b):
    rgb_hexa = ""

    for value in r, g, b:
        if value < 0:
            value = 0
        elif value > 255:
            value = 255
        if len(str(hex(value))[2:]) == 1:
            rgb_hexa += ('0' + str(hex(int(value)))[2:])
        else:
            rgb_hexa += str(hex(int(value)))[2:]
            
    return rgb_hexa.upper()

result = rgb(346, 12, -34)
print(result)


#Best practice
def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))    # caps x between 0 and 255: minimo tra (255 e il massimo tra (x e 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b)) # {:02X} the :02 sets the string format to a minimum length of 2 with zeros to pad if necessary
                                                               # the X sets the string to uppercase hexadecimal  
                                                               # "{:02X}"*3 == "{:02X}{:02X}{:02X}"  in both cases .format will assign r,g and b to each format specifier