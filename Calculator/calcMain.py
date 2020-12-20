import logging
from pip._vendor.distlib.compat import raw_input
import random

# Variables for functions
age = None
height = None
weight = None
goal_number = int()
activity_lvl = None
carbs = None
fats = ()
# Variables
gender = str()
gender_choice = False
goal_choice = False
proteins = 0
# Activity level multipliers
level_1 = 1.2
level_2 = 1.375
level_3 = 1.55
level_4 = 1.725
level_5 = 1.9

def Male_Calc(age, height, weight, goal_number, activity_lvl):
    global carbs
    global proteins
    global fats
    proteins = weight
    fats = weight * 0.5
    weight_kg = weight / 2.2
    height_cm = height * 2.54
    ### Multipliers
    male_weight_key = 66
    male_weight_multiplier = 13.7
    male_height_multiplier = 5
    male_age_multiplier = 6.8 
    ### Equations ###
    bmr_male = (male_weight_key + (male_weight_multiplier * (weight_kg))
            + (male_height_multiplier * (height_cm))
            - (male_age_multiplier * age))
    bmr_male_post = bmr_male * activity_lvl
    fat_loss_bmr_m = (bmr_male_post - (bmr_male_post * .20))
    gain_bmr_m = (bmr_male_post + 200)

    while carbs is None:
        if goal_number == 1:
            carbs = (float(fat_loss_bmr_m) - ((proteins * 4) + (fats * 9))) / 4
            round_carbs = round(carbs, 1)
            print("Here is your caloric breakdown!\nWe recommend that you consume {} calories daily.\nThis caloric value should be made up of these macro nutriuents:\nProteins = {} grams\nFats = {} grams\nCarbs = {} grams."\
                .format(fat_loss_bmr_m, proteins, fats, round_carbs))
            return
        elif goal_number == 2:
            carbs = (float(gain_bmr_m) - ((proteins * 4) + (fats * 9))) / 4
            round_carbs = round(carbs, 1)
            print("Here is your caloric breakdown!\nWe recommend that you consume {} calories daily.\nThis caloric value should be made up of these macro nutriuents:\nProteins = {} grams\nFats = {} grams\nCarbs = {} grams."\
                .format(gain_bmr_m, proteins, fats, round_carbs))
            return
        elif goal_number == 3:
            carbs = (float(bmr_male_post) - ((proteins * 4) + (fats * 9))) / 4
            round_carbs = round(carbs, 1)
            print("Here is your caloric breakdown!\nWe recommend that you consume {} calories daily.\nThis caloric value should be made up of these macro nutriuents:\nProteins = {} grams\nFats = {} grams\nCarbs = {} grams."\
                .format(bmr_male_post, proteins, fats, round_carbs))
            return
        else:
            pass

def Female_Calc(age, height, weight, goal_number, activity_lvl):
    global carbs
    global proteins
    global fats
    protein = weight
    fats = weight * 0.5
    weight_kg = weight / 2.2
    height_cm = height * 2.54
    ### Multipliers ###
    female_weight_key = 65
    female_weight_multiplier = 9.6
    female_height_multiplier = 1.8
    female_age_multiplier = 4.7
    ### Equation ###
    bmr_female = (female_weight_key + (female_weight_multiplier * (weight_kg))
              + (female_height_multiplier * (height_cm))
              - (female_age_multiplier * age))
    bmr_female_post = bmr_female * activity_lvl
    fat_loss_bmr_f = (bmr_female_post - (bmr_female_post * .20))
    gain_bmr_f = (bmr_female_post + 200)
    
    while carbs is None:
        if goal_number == 1:
            carbs = (float(fat_loss_bmr_f) - ((proteins * 4) + (fats * 9))) / 4
            round_carbs = round(carbs, 1)
            print("Here is your caloric breakdown!\nWe recommend that you consume {} calories daily.\nThis caloric value should be made up of these macro nutriuents:\nProteins = {} grams\nFats = {} grams\nCarbs = {} grams."\
                .format(fat_loss_bmr_f, proteins, fats, round_carbs))
            return
        elif goal_number == 2:
            carbs = (float(gain_bmr_f) - ((proteins * 4) + (fats * 9))) / 4
            round_carbs = round(carbs, 1)
            print("Here is your caloric breakdown!\nWe recommend that you consume {} calories daily.\nThis caloric value should be made up of these macro nutriuents:\nProteins = {} grams\nFats = {} grams\nCarbs = {} grams."\
                .format(gain_bmr_f, proteins, fats, round_carbs))
            return
        elif goal_number == 3:
            carbs = (float(bmr_female_post) - ((proteins * 4) + (fats * 9))) / 4
            round_carbs = round(carbs, 1)
            print("Here is your caloric breakdown!\nWe recommend that you consume {} calories daily.\nThis caloric value should be made up of these macro nutriuents:\nProteins = {} grams\nFats = {} grams\nCarbs = {} grams."\
                .format(bmr_female_post, proteins, fats, round_carbs))
            return
        else:
            pass

def start_calc():
    if gender == "male":
        Male_Calc(age, height, weight, goal_number, activity_lvl)
    elif gender == "female":
        Female_Calc(age, height, weight, goal_number, activity_lvl)
    else:
        pass

def Get_Stats():
    global age
    global height
    global weight
    global activity_lvl
    global goal_choice
    global gender_choice
    global gender 
    global goal_number
    while age is None:
        age = raw_input('Enter age.\n')
        try:
            age = int(age)
            assert age > 0
        except AssertionError:
            logging.warning('Value provided is not accepted.')
            age = None
        except ValueError:
            logging.warning('Provided age is not an integer, please try again.')
            age = None

    while height is None:
        height = raw_input('Enter height in inches.\n')
        try:
            height = int(height)
            assert height > 0
        except AssertionError:
            logging.warning('Value provided is not accepted.')
            height = None
        except ValueError:
            logging.warning('Provided height is not an integer, please try again.')
            height = None

    while weight is None:
        weight = raw_input('Enter weight in pounds.\n')
        try:
            weight = int(weight)
            assert weight > 0
        except AssertionError:
            logging.warning('Value provided is not accepted.')
            weight = None
        except ValueError:
            logging.warning('Provided weight is not an integer, please try again.')
            weight = None

    while activity_lvl is None:
        activity_lvl = raw_input('How active are you on a scale of 1-5?\n'
                                    '1 being sedentary, 5 being extremely active?\n')
        try:
            activity_lvl = int(activity_lvl)
            assert 0 < activity_lvl < 6
        except AssertionError:
            logging.warning('Value provide is not accepted. Please use a whole number and try again.')
            activity_lvl = None
        except ValueError:
            logging.warning('Provided activity level is not within parameters, please use a whole number and try again.')
            activity_lvl = None
        if activity_lvl == 1:
            activity_lvl = level_1
        elif activity_lvl== 2:
            activity_lvl = level_2
        elif activity_lvl == 3:
            activity_lvl = level_3
        elif activity_lvl == 4:
            activity_lvl = level_4
        elif activity_lvl == 5:
            activity_lvl = level_5
        else:
            activity_choice = None

    while goal_choice is False:
        goal = raw_input('Please select a goal for your journey.\nPlease enter one of the following choices: gain, fat loss or none.\n')
        if goal == 'fat loss' or goal == 'Fat loss':
            goal_number = 1
            goal_choice = True
        elif goal == 'gain' or goal == 'Gain':
            goal_number = 2
            goal_choice = True
        elif goal == 'None' or goal == 'none':
            goal_number = 3
            goal_choice = True
        else:
            goal_choice = False
            logging.warning("Invalid input, please try again. \n")

    while gender_choice is False:
        gender = raw_input('Are you male or female?\n')
        if gender == "male" or gender == "m" or gender == "M" or gender == "Male":
            gender_choice = True
            gender = "male"
        elif gender == "female" or gender == "f" or gender == "F" or gender == "Female":
            gender_choice = True
            gender = "female"
        else:
            gender_choice = False
            logging.warning("Invalid input, please try again.\n")
    start_calc()

Get_Stats()




