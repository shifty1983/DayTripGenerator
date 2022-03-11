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
mode_of_trasnportation_list = ['Rental car', 'Car service', 'Uber', 'Public transportation']

def destination_choice(destination):
    random_destination = '0'
    previous_destination = '0'
    user_confirmation = 'n'
    while user_confirmation == 'n':
        random_destination = random.choice(destination)
        if previous_destination == random_destination:
            continue
        user_confirmation = input(f'{random_destination} has been chosen as the location for your day trip. Is this acceptable? y/n ')
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
        user_confirmation = input(f'{random_restaurant} has been chosen as the restaurant to eat at. Is this acceptable? y/n ')
        if user_confirmation == 'y':
            print("Let's move on to entertainment now.")
        if user_confirmation == 'n':
            print("Let's try again.")
    return(random_restaurant)

def entertainment_choice(entertainment):
    random_entertainment = '0'
    previous_entertainment = '0'
    user_confirmation = 'n'
    while user_confirmation == 'n':
        random_entertainment = random.choice(entertainment)
        if previous_entertainment == random_entertainment:
            continue
        user_confirmation = input(f'{random_entertainment} has been chosen as the entertainment choice for the day. Is this acceptable? y/n ')
        if user_confirmation == 'y':
            print("Let's move on to tranportation now.")
        if user_confirmation == 'n':
            print("Let's try again.")
    return(random_entertainment)

def transportation_choice(transportation):
    random_transportation = '0'
    previous_transportation = '0'
    user_confirmation = 'n'
    while user_confirmation == 'n':
        random_transportation = random.choice(transportation)
        if previous_transportation == random_transportation:
            continue
        user_confirmation = input(f'{random_transportation} has been chosen as your tranportation for the day. Is this acceptable? y/n ')
        if user_confirmation == 'y':
            print("Let's move on to restaurants now.")
        if user_confirmation == 'n':
           print("Let's try again.")
           previous_transportation = random_transportation
    return(random_transportation)

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

entertainment_list = '0'
if destination == 'San Fransisco':
    entertainment_list = san_fransisco_entertainment_list
elif destination == 'Orlando':
    entertainment_list = orlando_entertainment_list
elif destination == 'New York':
    entertainment_list = new_york_entertainment_list
else:
    entertainment_list = chicago_entertainment_list
entertainment = entertainment_choice(entertainment_list)

tranportation = transportation_choice(mode_of_trasnportation_list)

