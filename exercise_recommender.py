# Insert copyright statement here
from math import *
# Gather various user inputs: age, fitness level, weight, and primary fitness goal
age = int(input('Enter your age (as an integer) in years: '))
while age < 15 or age > 75:
    print("This system is meant for young adults to older people \n"
          "Please enter an integer between 15 to 75\n")
    age = int(input('Enter your age in years: '))

fitness_level = int(input("Enter your fitness level as an integer \n"
                      "1 for couch potato, 2 for an average individual \n"
                      "or 3 for an athlete: "))
while fitness_level < 1 or fitness_level > 3:
    print("You have entered an invalid fitness_level. Try again\n")
    fitness_level = int(input("Enter your fitness level as an integer \n"
                      "1 for couch potato, 2 for an average individual \n"
                      "or 3 for an athlete: "))

weight = float(input('Enter your current weight (in lbs): '))

fitness_goal = input("Enter your primary fitness goal as a character \n"
                      "a: lose weight, b: improve flexibility, or c: build muscle:\n ")

while fitness_goal.lower() not in ['A'.lower(), 'B'.lower(), 'C'.lower()]:
    print("You have entered an invalid input for your fitness goal")
    fitness_goal = input("Enter your primary fitness goal as a character \n"
                "a: lose weight, b: improve flexibility, or c: build muscle:\n ")

# Difficulty (on a scale of 1  to 20) is calculated using a logistic growth model
def calculate_difficulty(age_user, fitness_level_user, correction_factor):
    difficulty = (20/ 1 + e ** (-0.08 * age_user)) - 2 * fitness_level_user
    difficulty = difficulty * correction_factor
    return difficulty

if fitness_goal.lower() == "A".lower():
    # Cardio exercise initial values
    cardio_exercises = ['Running', 'Jump Rope', 'Kickboxing', 'Elliptical', 'Swimming', 'Rowing']
    MET_values = [10, 11.8, 8.5, 7, 9, 8]
    correction_factors = [0.6, 0.85, 0.75, 0.5, 0.8, 0.85]
    # Calculate the score for cardio exercises
    def calculate_cardio_scores(cardio_exercises, MET_values, weight, correction_factors):
        cardio_scores = []
        calorie_burn_rate = 0
        for i in range(len(MET_values)):
            calorie_burn_rate = weight/2.2 * MET_values[i] * (3.5*60)/200
            difficulty = calculate_difficulty(age, fitness_level, correction_factors[i])
            cardio_scores.append(2 * sqrt(calorie_burn_rate) + 5 * (20-difficulty))
        return cardio_scores

    # Calculating the scores for all cardio exercises
    cardio_scores_lst = calculate_cardio_scores(cardio_exercises, MET_values, weight, correction_factors)

    # Build a dictionary with the exercises as keys and scores as values
    cardio_dict = {}
    for i in range(len(cardio_exercises)):
        cardio_dict.update({cardio_exercises[i]: cardio_scores_lst[i]})

    # Generate recommendation for best two cardio exercises
    def generate_cardio_recommendations(dict):
        # Sort the dictionary keys by the values
        sorted_exercises = sorted(dict, key = dict.__getitem__)
        # Print the recommendations
        print('Based on your data we recommend ' + sorted_exercises[-1] +
              ' as your most effective exercise \nand ' + sorted_exercises[-2] +
              ' for your second most effective exercise')

    generate_cardio_recommendations(cardio_dict)

elif fitness_goal.lower() == "B".lower():
    upper_body_stretches = ['Cat-Camel Pose', 'Upper Trapezius (Neck Stretch)', 'Cross Body Shoulder Stretch'
                            'Chest Stretch', 'Child''s Pose']
    lower_body_stretches = ['Hamstring Stretch', 'Butterfly Stretch', 'Hip Flexor Lunge Stretch',
                            'Pigeon Stretch', 'Lying Quad Stretch']
    upper_body_avg_volume = [551, 243, 436, 262, 231, 617]
    upper_body_correction_factors = []
    lower_body_avg_volume = [779, 1290, 967, 1168.5, 2150]
    lower_body_correction_factors = []
    def calculate_stretching_scores(weight,upper_body_volume, lower_body_vol,difficulty):
        upper_body__stretch_scores = []
        lower_body_stretch_scores = []
        stretch_score = 0;
        for idx in range(len(upper_body_stretches)):
            stretch_score = 2 * sqrt()




