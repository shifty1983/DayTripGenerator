import random

def get_choice(choice_list, choice_type):
    random_choice = '0'
    previous_choice = '0'
    user_confirmation = 'n'
    while user_confirmation == 'n':
        random_choice = random.choice(choice_list)
        if previous_choice == random_choice:
            continue
        user_confirmation = input(f'{random_choice} has been chosen as the {choice_type} for your day trip. Is this acceptable? y/n ')
        if user_confirmation == 'y':
            print(f"Let's move on to {choice_type} now.")
        if user_confirmation == 'n':
           print("Let's try again.")
           previous_choice = random_choice
    return(random_choice)

def run_generator():

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

    user_confirmation = 'n'  
    while user_confirmation == 'n':
        destination = get_choice(destination_list, 'destination')

        restaurant_list = '0'
        if destination == 'San Fransisco':
            restaurant_list = san_fransisco_restaurants_list
        elif destination == 'Orlando':
            restaurant_list = orlando_restaurants_list
        elif destination == 'New York':
            restaurant_list = new_york_restaurants_list
        else:
            restaurant_list = chicago_restaurants_list
        restaurant = get_choice(restaurant_list, 'restaurant')

        entertainment_list = '0'
        if destination == 'San Fransisco':
            entertainment_list = san_fransisco_entertainment_list
        elif destination == 'Orlando':
            entertainment_list = orlando_entertainment_list
        elif destination == 'New York':
            entertainment_list = new_york_entertainment_list
        else:
            entertainment_list = chicago_entertainment_list
        entertainment = get_choice(entertainment_list, 'entertainment')

        tranportation = get_choice(mode_of_trasnportation_list, 'transportation')

        user_confirmation = input(f'You will be going to {destination}, have a nice meal at {restaurant}, {entertainment} is where you will have some fun, and you will get around by {tranportation} during your trip. Is this acceptable? y/n ')
        if user_confirmation == 'y':
            print("Have fun on your day trip.")
        if user_confirmation == 'n':
            print("Let's try again.")

run_generator()
