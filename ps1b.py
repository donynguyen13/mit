total_cost = 0
portion_down_payment = 0
down_payment_percent = 0.25
current_savings = 0
annual_salary = 0
portion_saved = 0
r = 0.04
monthly_salary_saved = 0
num_months = 0

annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))

portion_down_payment = total_cost*down_payment_percent
monthly_salary_saved = (annual_salary/12)*portion_saved
while current_savings <= portion_down_payment:
    current_savings += current_savings*(r/12) + monthly_salary_saved
    num_months += 1
print(num_months)
