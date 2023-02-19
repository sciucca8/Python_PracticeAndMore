def greetings(name = ["Jhon Doe"]):
    for n in name:
        print(f"Hello {n}!")

greetings(["Tristram Mcbbride", "Baldwin Preston", "Wally Collins"])

#Bonus!
def greetings(*name):
    for n in name:
        print(f"Hello {n}!")

greetings("Jhon Doe", "Tristram Mcbbride", "Baldwin Preston", "Wally Collins")