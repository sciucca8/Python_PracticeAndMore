class car(): 
    def __init__(self, model, price, color):
        self.model = model
        self.price = price
        self.color = color
    def get_color(self):
        return self.color

def color_get(obj_name):
    return obj_name.color

Tesla_Y = car("Y", 60000, "night blue")

print(Tesla_Y.get_color())
print(color_get(Tesla_Y))
print(Tesla_Y.color)

