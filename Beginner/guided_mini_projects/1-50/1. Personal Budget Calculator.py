#Your program must do this:

# 1. Ask the user for three things:
    # * monthly income
    # * monthly rent/mortgage cost
    # * monthly food cost
# 2. Convert those inputs to numbers.
# Calculate:
    # * total expenses
    # * remaining money after expenses
    # * savings recommendation = 20% of income
# 4. Print a clean summary using an f-string:

#Output should be 
# Monthly Summary:
# ----------------
# Income: $4000
# Expenses: $2300
# Remaining: $1700
# Recommended Savings: $800.0


# Income, rent, food costs
#monthly_income = input("What is your monthly income? ")
#monthly_rent = input("What is your monthly rent? ")
#monthly_food = input("What is your monthly food cost? ")
# Correction
monthly_income = float(input("What is your monthly income? "))
monthly_rent = float(input("What is your monthly rent? "))
monthly_food = float(input("What is your monthly food cost? "))

# Total Expenses, after expenses remaining, Savings recommendation (20%)
total_expenses = monthly_rent + monthly_food
remaining_cash = monthly_income - total_expenses
savings = monthly_income * 0.2;round(.2)
# Corrections
    # savings = round(monthly_income *0.20, 2)

#Monthly Summary
print(f"""Monthly Summary:
      ----------------
      Income: ${monthly_income}
      Expenses: ${total_expenses}
      Remaining: ${remaining_cash}
      Recommended Savings: ${savings}""")

