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
    new_list = [food["name"] for food in spicy_foods]
    return new_list
    pass

def get_spiciest_foods(spicy_foods):
    new_list = [food for food in spicy_foods if food["heat_level"] > 5]
    return new_list
    pass

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {food["heat_level"] * "🌶"}')
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None
    pass

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)
    pass

def get_average_heat_level(spicy_foods):
    sum = 0
    counter = 0
    for food in spicy_foods:
        sum += food["heat_level"]
        counter +=1
    # sum =  (sum + heat["heat_level"] for heat in spicy_foods)
    # print (sum / counter)
    return int(sum / counter)
    pass

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    pass

print_spicy_foods(spicy_foods)
get_average_heat_level(spicy_foods)