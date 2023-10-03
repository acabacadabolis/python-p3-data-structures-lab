spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    food_names = [x.get("name") for x in spicy_foods]
    return food_names

def get_spiciest_foods(spicy_foods):
    high_spice = [x for x in spicy_foods if x.get("heat_level")>=5]
    return high_spice

def print_spicy_foods(spicy_foods):
    for x in spicy_foods:
        print(f"{x.get('name')} ({x.get('cuisine')}) | Heat Level: " + (x.get('heat_level')*"🌶"))

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for x in spicy_foods:
        if x.get("cuisine")==cuisine:
            return x

def print_spiciest_foods(spicy_foods):
    for x in spicy_foods:
        if x.get("heat_level")>=5:
            print(f"{x.get('name')} ({x.get('cuisine')}) | Heat Level: " + (x.get('heat_level')*"🌶"))

def get_average_heat_level(spicy_foods):
    heat_levels = [x.get("heat_level") for x in spicy_foods]
    avg = sum(heat_levels) / len(heat_levels)
    return avg

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
