# -------------------------------------------
# Group Exercise: The Road Trip Budgeter
# -------------------------------------------
# This is a COLLABORATIVE exercise. You will build one program together.
#
# The Goal: Create a calculator that estimates the total cost of a road trip.
#
# ROLES (Driver vs. Navigator):
# At any time, only ONE person is typing.
# - **The Driver**: The person sitting at the keyboard typing the code.
# - **The Navigators**: The others watching the screen, checking for typos,
#   and helping figure out the maths logic.
#
# Problem Solving Challenge:
# You aren't just printing text. You must use maths logic.
# You will be SWAPPING COMPUTERS to practise pulling code from the cloud!
# -------------------------------------------
# GROUP INSTRUCTIONS
# -------------------------------------------
# 1. Open your Group Repository in GitHub Codespaces.
# 2. Ensure every group member has the repo open on their own screen.
# 3. Decide who starts as The Driver for Task 1.
# 4. BE READY TO MOVE! You will switch seats often.
# -------------------------------------------


# -------------------------------------------
# Task 1: Fuel Calculation (Driver A Starts)
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 1: Fuel Calculation\n"
    + "-------------------------------------------")

# PROBLEM: We need to know how much gas money we need.
# Formula: (Distance / Car Efficiency) * Price of Gas

# TODO (Driver A):
# 1. Ask the user for the **distance** of the trip (in miles/km).
#    Convert the answer to a float() and save it in a variable with a descriptive name.
# 2. Ask the user for the car's **fuel efficiency** (miles/km per litre).
#    Convert the answer to a float() and save it in a variable with a descriptive name.
# 3. Ask the user for the **price of gas** (per litre).
#    Convert the answer to a float() and save it in a variable with a descriptive name.
# 4. Calculate the cost: (distance / efficiency) * gas_price.
#    Save this in a variable with a descriptive name.
# 5. Print: "Estimated Fuel Cost: £X" (Use the calculation variable you just made).

# Write your code below:


# -------------------------------------------
# CHECKPOINT
# -------------------------------------------
# 1. Run the code to check the maths.
# 2. In the terminal: git add Ex2_group.py
# 3. In the terminal: git commit -m "Added fuel logic"
# 4. In the terminal: git push origin main
#
# *** STOP! ***
# EVERYONE STAND UP. MOVE TO THE NEXT STUDENT'S COMPUTER.
# DO NOT TOUCH THE KEYBOARD YET.
# -------------------------------------------


# -------------------------------------------
# Task 2: Accommodation (Driver B)
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Task 2: Accommodation Costs\n"
    + "-------------------------------------------")

# INSTRUCTIONS:
# You are now at a new computer.
# The code here is OLD. You need to fetch what the previous Driver wrote!
# 1. Run `git pull origin main` in the terminal.

# PROBLEM: We need to know the hotel costs.
# Formula: Nights * Price Per Night

# TODO (Driver B):
# 1. Ask the user for the number of **nights** they are staying.
#    Convert the answer to an int() and save it in a variable with a descriptive name.
# 2. Ask the user for the **price per night** of the hotel.
#    Convert the answer to a float() and save it in a variable with a descriptive name.
# 3. Calculate the total: nights * hotel_price.
#    Save this in a variable with a descriptive name.
# 4. Print: "Estimated Hotel Cost: £X"

# Navigators: Watch closely! Make sure they convert the input correctly.

# Write your code below:


# -------------------------------------------
# CHECKPOINT
# -------------------------------------------
# 1. Run the code. You should see Fuel AND Hotel prompts now.
# 2. git add Ex2_group.py
# 3. git commit -m "Added hotel logic"
# 4. git push origin main
#
# *** STOP! ***
# EVERYONE STAND UP. MOVE TO THE NEXT STUDENT'S COMPUTER.
# -------------------------------------------


# -------------------------------------------
# Task 3: Food & Grand Total (Driver C or A)
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Task 3: Food & Grand Total\n"
    + "-------------------------------------------")

# INSTRUCTIONS:
# You are at a new computer again.
# 1. Run `git pull origin main` to get the latest changes.

# PROBLEM: Everyone needs to eat, and we need a final sum.
# Formula: People * Daily Food Budget * Nights

# TODO:
# 1. Ask the user for the number of **people** going on the trip.
#    Convert the answer to an int() and save it in a variable with a descriptive name.
# 2. Ask the user for the **daily food budget** (per person).
#    Convert the answer to a float() and save it in a variable with a descriptive name.
# 3. Calculate the food cost: people * daily_food_budget * nights.
#    IMPORTANT: To get the number of 'nights', look at the code from Task 2 
#    to see what variable name the previous Driver used!
# 4. Calculate the Grand Total: fuel_cost + hotel_total + food_total.
#    (Again, check previous tasks to see what variable names they used for the costs).
# 5. Print the Final Trip Cost.

# Write your code below:


# -------------------------------------------
# CHECKPOINT
# -------------------------------------------
# 1. git add Ex2_group.py
# 2. git commit -m "Calculated grand total"
# 3. git push origin main
#
# *** STOP! ***
# STAND UP. MOVE TO THE NEXT STUDENT'S COMPUTER.
# -------------------------------------------


# -------------------------------------------
# EXTENSION ACTIVITIES
# -------------------------------------------

# Extension 1: Split the Bill
# -------------------------------------------
# 1. Run `git pull origin main` before starting!

print("\n-------------------------------------------\n"
    + "Extension 1: Split the Bill\n"
    + "-------------------------------------------")

# TODO:
# 1. Create a variable called 'per_person_cost'.
# 2. Calculate it by dividing your Grand Total variable by your People variable.
# 3. Print: "Each person pays: £X"

# Write your code below:


# -------------------------------------------
# CHECKPOINT
# -------------------------------------------
# 1. git add Ex2_group.py
# 2. git commit -m "Completed Extension 1"
# 3. git push origin main
#
# *** STOP! ***
# STAND UP. MOVE TO THE NEXT STUDENT'S COMPUTER.
# -------------------------------------------


# Extension 2: Destination Formatting
# -------------------------------------------
# 1. Run `git pull origin main` before starting!

print("\n-------------------------------------------\n"
    + "Extension 2: Destination Formatting\n"
    + "-------------------------------------------")

# TODO:
# 1. Ask the user for the **name of the destination**.
#    Save this in a variable with a descriptive name.
# 2. Use .capitalize() (or .title()) to ensure the city name looks correct
#    even if they typed it in lowercase.
# 3. Print: "Budget calculated for trip to [destination]!"

# Write your code below:


# -------------------------------------------
# CHECKPOINT
# -------------------------------------------
# 1. git add Ex2_group.py
# 2. git commit -m "Completed Extension 2"
# 3. git push origin main
#
# *** STOP! ***
# STAND UP. MOVE TO THE NEXT STUDENT'S COMPUTER.
# -------------------------------------------


# Extension 3: The Safety Buffer
# -------------------------------------------
# 1. Run `git pull origin main` before starting!

print("\n-------------------------------------------\n"
    + "Extension 3: The Safety Buffer\n"
    + "-------------------------------------------")

# PROBLEM: Trips always cost more than expected.

# TODO:
# 1. Create a variable called 'buffer' and set it to 1.2 (this means 120%).
# 2. Create a variable called 'safe_budget'.
# 3. Calculate it by multiplying your Grand Total variable by 'buffer'.
# 4. Print the Safe Budget.

# Write your code below:


# -------------------------------------------
# CHECKPOINT
# -------------------------------------------
# 1. git add Ex2_group.py
# 2. git commit -m "Completed Extension 3"
# 3. git push origin main
#
# *** STOP! ***
# ONE FINAL SWAP! MOVE TO THE NEXT STUDENT'S COMPUTER.
# -------------------------------------------


# -------------------------------------------
# ADVANCED ACTIVITY: The "Leftover" Calculator
# -------------------------------------------
# 1. Run `git pull origin main`.

print("\n-------------------------------------------\n"
    + "ADVANCED ACTIVITY: The Leftover Calculator\n"
    + "-------------------------------------------")

# TODO:
# 1. Ask the user for their **maximum budget limit**.
#    Convert it to a float() and save it in a variable with a descriptive name.
# 2. Create a variable called 'difference'.
#    Calculate it by subtracting your Grand Total FROM your new Max Budget variable.
# 3. Print the 'difference'.
#
# NOTE: If the result is negative, it means you are over budget!
# (We haven't really learned IF statements yet, but look at the number.
# If it has a minus sign, you need a cheaper hotel!)

# Write your code below:


# -------------------------------------------
# FINAL SUBMISSION
# -------------------------------------------
# 1. git add Ex2_group.py
# 2. git commit -m "Final submission - Road Trip Calculator"
# 3. git push origin main
#
# High-five your team and tell each other "you're awesome".
# You used Git and Codespaces to collaborate!
# -------------------------------------------
