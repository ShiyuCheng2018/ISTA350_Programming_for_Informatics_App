import random


def price_of_rocks(type_rock, weight, is_gem):
    if type_rock == "quartz":
        if is_gem == False:
            price = 5.50
        else:
            price = 21.99
    elif type_rock == "garnet":
        if is_gem == False:
            price = 40.00
        else:
            price = 299.00
    elif type_rock == "meteorite":
        price = 15.50
    return price * weight

def  total_price():
    wanna_quit = False
    price = 0
    while not wanna_quit:
        type = input("What type of rocks that you want? (quartz crystals / garnets / meteorite) ")
        weight_answer = input(f"How much weights of {type}? ")
        is_gem_answer = input("Do you want gem quality (y/n)? ")
        unit_answer = input("What unit of weight did you use ? (pound / gram) ")

        weight = unit_convert(float(weight_answer), unit_answer)

        if type == "quartz crystals":
            price += price_of_rocks(type, weight, is_gem_answer)
        elif type == "garnets":
            price += price_of_rocks(type, weight, is_gem_answer)
        elif type == "meteorite":
            price += price_of_rocks(type, weight, is_gem_answer)

        wanna_quit = input("Wanna quit? (False / True) ")

        if wanna_quit == "True":
            print(f"The total price is $ {price}, thank you for your shopping.")
            return price
        else:
            print("\nAlright, please continue your shopping....\n")
            wanna_quit = False

def unit_convert(weight, unit):
    if unit == "gram":
        return weight / 453.592
    return weight

def draw_hand():
    suit = random.randint(1, 4)
    value = 0
    for each in range(4):
        rank = random.randint(1, 13)
        value += suit * rank
    print(value)


def main():
    draw_hand()


main()
