#!/usr/bin/python3
monthly_income_str = input("Enter your monthly income: ")
monthly_expenses_str = input("Enter your total monthly expenses: ")

monthly_income = float(monthly_income_str)
monthly_expenses = float(monthly_expenses_str)

monthly_savings = monthly_income - monthly_expenses

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"Your monthly savings are ${monthly_savings:.0f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.0f}.")
