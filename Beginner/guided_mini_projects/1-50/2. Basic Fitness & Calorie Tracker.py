# Tasks
# 1. Ask the user for:
    # * their weight in pounds
    # * minutes they walked
    # * minutes they lifted weights
# Use input() for all.
# 2. Convert and calculate:
    # * Convert weight to kilograms (kg = lbs * 0.453592)
    # * Calories burned:
# walking: 4 calories per minute
# lifting: 6 calories per minute
    # * Calculate total calories burned
# 3. Determine training intensity
# Using simple if/else:
    # * If total calories < 200 → "Light training"
    # * 200–500 → "Moderate training"
    # * 500 → "Intense training"
# Store in intensity_label.
# 4. Print a summary (use a single f-string block)
# Like:

# Daily Training Summary
# ----------------------
# Weight (kg): 87.54
# Calories Burned: 340
# Intensity: Moderate training

#Rules
    # * You must convert all number inputs with int()
    # * You must round kg to 2 decimals using round()
    # * You must use one final print() with triple quotes
    # * No ChatGPT correction unless you ask for it


# Weight/exercise time
user_weight_lbs = float(input("What is your weight? "))
minutes_walked = float(input("How many minutes did you walk? "))
minutes_lifting = float(input("How many minutes did you lift weights? "))

# Convert lbs to kg
lbs_kg_convert = user_weight_lbs * 0.453592

# Caloric Burn
walking_burn = minutes_walked * 4
lifting_burn = minutes_lifting * 6
total_caloric_burn = walking_burn + lifting_burn

# Training intensity
if total_caloric_burn < 200:
    intensity = "Light Training"
elif 200 <= total_caloric_burn <= 500:
    intensity = "Moderate Training"
elif total_caloric_burn > 500:
    intensity = "Intense Training"



# Training Summary
print(f"""Daily Training Summary
----------------------
Weight (kg): {lbs_kg_convert}
Calories Burned: {total_caloric_burn}
Intensity: {intensity}""")

