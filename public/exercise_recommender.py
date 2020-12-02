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
    upper_body_stretches = ['Cat-Camel Pose', 'Upper Trapezius (Neck Stretch)', 'Overhead Triceps + Shoulders',
                            'Cross Body Shoulder Stretch', 'Chest Stretch', 'Child''s Pose']
    lower_body_stretches = ['Hamstring Stretch', 'Butterfly Stretch', 'Hip Flexor Lunge Stretch',
                            'Pigeon Stretch', 'Lying Quad Stretch']
    upper_body_avg_volume = [551, 243, 436, 262, 231, 617]
    upper_body_cfs = [0.9, 0.76, 0.83, 0.69, 0.72, 0.88]
    lower_body_avg_volume = [779, 1290, 967, 1168.5, 2150]
    lower_body_cfs = [0.78, 0.67, 0.73, 0.84, 0.69]

    def calculate_stretching_scores(weight,upper_body_vol, upper_correction, lower_body_vol, lower_correction):
        upper_body_stretch_scores = []
        lower_body_stretch_scores = []
        stretch_score = 0
        # Calculate scores for upper body stretches, store in a list
        for idx in range(len(upper_body_vol)):
            difficulty = calculate_difficulty(age, fitness_level, upper_correction[idx])
            stretch_score = 2/5 * upper_body_vol[idx] - 1/3 * weight + 5 * (20-difficulty)
            upper_body_stretch_scores.append(stretch_score)

        # Calculate scores for lower body stretches, store in a separate list
        for j in range(len(lower_body_vol)):
            difficulty = calculate_difficulty(age, fitness_level, lower_correction[j])
            stretch_score = 2/5 * lower_body_vol[j] - 1/3 * weight + 5 * (20 - difficulty)
            lower_body_stretch_scores.append(stretch_score)

        return [upper_body_stretch_scores, lower_body_stretch_scores]

    stretching_scores_lst = calculate_stretching_scores(weight, upper_body_avg_volume,
                                                        upper_body_cfs, lower_body_avg_volume, lower_body_cfs)
    # Create dictionaries to store stretches as keys and scores as values
    upper_stretch_dict = {}
    lower_stretch_dict = {}
    for i in range(len(stretching_scores_lst[0])):
        upper_stretch_dict.update({upper_body_stretches[i]: stretching_scores_lst[0][i]})

    for j in range(len(stretching_scores_lst[1])):
        lower_stretch_dict.update({lower_body_stretches[j]: stretching_scores_lst[1][j]})

    def generate_stretch_recommendation(dict1,dict2):
        # Sort the dictionary keys by the values
        sorted_exercises1 = sorted(dict1, key=dict1.__getitem__)
        sorted_exercises2 = sorted(dict2, key=dict2.__getitem__ )
        # Print the recommendations
        print('Based on your data we recommend ' + sorted_exercises1[-1] +
              ' as your most effective upper body stretch \nand ' + sorted_exercises1[-2] +
              ' for your second most effective upper body stretch\n')
        print('For your lower body we recommend ' + sorted_exercises2[-1] +
              ' as your most effective stretch \nand ' + sorted_exercises2[-2] +
              ' as your second most effective stretch')

    generate_stretch_recommendation(upper_stretch_dict, lower_stretch_dict)

else:
    upper_body_exercises = ['Pushups', 'Decline Pushups', 'Parallel Grip Pullup',
                            'Side Plank', 'Tricep Dips', 'Lateral Plank Walk']
    upper_body_avg_vol = [1276, 1276, 959, 817, 756, 1242]
    upper_body_cfs = [0.65, 0.83, 0.79, 0.86, 0.73, 0.80]
    lower_body_exercises = ['Bodyweight Squat', 'Reverse Lunges', 'Side Lunge', 'Box Jump',
                            'Bulgarian Split Squats']
    lower_body_avg_vol = [1828, 2150, 1912, 1828, 2310]
    lower_body_cfs = [0.6, 0.73, 0.71, 0.78, 0.92]
    def calculate_exercise_scores(weight,upper_body_vol, upper_correction, lower_body_vol, lower_correction):
        upper_body_ex_scores = []
        lower_body_ex_scores = []
        exercise_score = 0
        # Calculate scores for upper body stretches, store in a list
        for idx in range(len(upper_body_vol)):
            difficulty = calculate_difficulty(age, fitness_level, upper_correction[idx])
            stretch_score = 2 / 5 * upper_body_vol[idx] - 1 / 3 * weight + 5 * (20 - difficulty)
            upper_body_ex_scores.append(exercise_score)

        # Calculate scores for lower body stretches, store in a separate list
        for j in range(len(lower_body_vol)):
            difficulty = calculate_difficulty(age, fitness_level, lower_correction[j])
            stretch_score = 2 / 5 * lower_body_vol[j] - 1 / 3 * weight + 5 * (20 - difficulty)
            lower_body_ex_scores.append(exercise_score)
        return [upper_body_ex_scores, lower_body_ex_scores]

    exercise_scores_lst = calculate_exercise_scores(weight,upper_body_avg_vol,
                                                    upper_body_cfs, lower_body_avg_vol, lower_body_cfs)

    # Create dictionaries to store exercises as keys and scores as values
    upper_ex_dict = {}
    lower_ex_dict = {}
    for i in range(len(exercise_scores_lst[0])):
        upper_ex_dict.update({upper_body_exercises[i]: exercise_scores_lst[0][i]})

    for j in range(len(exercise_scores_lst[1])):
        lower_ex_dict.update({lower_body_exercises[j]: exercise_scores_lst[1][j]})

    def generate_exercise_recommendations(dict1, dict2):
        # Sort the dictionary keys by the values
        sorted_exercises1 = sorted(dict1, key=dict1.__getitem__)
        sorted_exercises2 = sorted(dict2, key=dict2.__getitem__)
        # Print the recommendations
        print('Based on your data we recommend ' + sorted_exercises1[-1] +
              ' as your most effective upper body exercise \nand ' + sorted_exercises1[-2] +
              ' for your second most effective upper body exercise\n')
        print('For your lower body we recommend ' + sorted_exercises2[-1] +
              ' as your most effective exercise \nand ' + sorted_exercises2[-2] +
              ' as your second most effective exercise')

    generate_exercise_recommendations(upper_ex_dict, lower_ex_dict)