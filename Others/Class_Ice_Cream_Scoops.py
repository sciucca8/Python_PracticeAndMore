import random

class Ice_cream():
    
    def __init__(self, num_flavors = 1, flavor = ["chocolate", 'cream', "lemon", "Cookie"]):
        self.flavor = random.choices(flavor, k = num_flavors)
    
    def __str__(self):                                 # or  def __depr__() ??
        return str(self.flavor)
    
    def get_flavor(self):
        return self.flavor
     
    def n_scoops(self, n = 3):
        scoops_ls = []
        for i in range(n):
            scoops_ls.append(Ice_cream())
        return scoops_ls

ice_cream1 = Ice_cream(3)
scoop_ls = Ice_cream.n_scoops(object, 6)
print(", ".join(str(scoop.flavor) for scoop in scoop_ls))
print(ice_cream1.flavor)

    


            
   
        
