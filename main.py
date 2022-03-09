import random

destination_list = ['San Fransisco', 'Orlando', 'New York', 'Chicago']
san_fransisco_restaurants_list = ["Scoma's", 'Nopa', 'Nari', 'Plow']
orlando_restaurants_list = ['bluezoo', 'Primo', 'Knife and Spoon', 'Grande Lakes']
new_york_restaurants_list = ["Edith's Eatery", "Zou Zou's", 'Ci Siamo', 'Hawksmoor NYC']
chicago_restaurants_list = ["Zaza's Pizzeria", 'Segnatore', 'Roux Diner', 'Bocadillo Market']
san_fransisco_entertainment_list =['Giants Game', 'Alcatraz', 'Winery Tour', 'Bus Tour']
orlando_entertainment_list = ['Disney World', 'Universal Studios', 'SeaWorld', 'Fishing']
new_york_entertainment_list = ['Broadway Show', 'Ellis Island', 'Helicopter Tour', 'Coney Island']
chicago_entertainment_list = ['River Cruise', 'Field Museum', 'Cubs Game', 'Lincoln Park Zoo']
mode_of_trasnportation_list = ['rental car', 'car service', 'Uber', 'public transportation']

def destination_choice(destination):
    random_destination = '0'
    previous_destination = '0'
    user_confirmation = 'n'
    while user_confirmation == 'n':
        random_destination = random.choice(destination)
        if previous_destination == random_destination:
            continue
        print(f'{random_destination} has been chosen as the location for your day trip. Is this acceptable? y/n ')
        user_confirmation = input()
        if user_confirmation == 'y':
            print("Let's move on to restaurants now.")
        if user_confirmation == 'n':
           print("Let's try again.")
           previous_destination = random_destination
    return(random_destination)

def restaurant_choice(restaurant):
    random_restaurant = '0'
    previous_restaurant = '0'
    user_confirmation = 'n'
    while user_confirmation == 'n':
        random_restaurant = random.choice(restaurant)
        if previous_restaurant == random_restaurant:
            continue
        print(f'{random_restaurant} has been chosen as the restaurant to eat at. Is this acceptable? y/n ')
        user_confirmation = input()
        if user_confirmation == 'y':
            print("Let's move on to entertainment now.")
        if user_confirmation == 'n':
            print("Let's try again.")
    return(random_restaurant)

destination = destination_choice(destination_list)

restaurant_list = '0'
if destination == 'San Fransisco':
    restaurant_list = san_fransisco_restaurants_list
elif destination == 'Orlando':
    restaurant_list = orlando_restaurants_list
elif destination == 'New York':
    restaurant_list = new_york_restaurants_list
else:
    restaurant_list = chicago_restaurants_list
restaurant = restaurant_choice(restaurant_list)


