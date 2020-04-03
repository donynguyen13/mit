total_cost = 1000000 #cost of home
portion_down_payment = 0 #variable to store how much down payment will be
down_payment_percent = 0.25 
portion_saved = 0 #percent of salary want to save
current_savings = 0
annual_salary = 0
r = 0.04 #annual return on investments
monthly_salary_saved = 0 #variable to hold result of calculation of portion of monthly salary saved
num_months = 36
semi_annual_raise = 0.07 #semi annual salary raise
high = 10000
low = 0
steps = 0 #count of bisection steps

annual_salary = float(input('Enter your annual salary: '))
portion_down_payment = total_cost*down_payment_percent

while abs(current_savings - portion_down_payment) >= 100:
    current_savings = 0 #reset savings amount
    guess = (high + low)/2
    portion_saved = guess/10000 #convert guess savings rate to decimal
    monthly_salary_saved = (annual_salary/12)*portion_saved
    for month in range(num_months):
        month += 1 #added plus 1 because index starts at 0. Need to add so that semi annual raise is caluclated correctly
        current_savings += current_savings*(r/12) + monthly_salary_saved
        if month % 6 == 0:
            monthly_salary_saved += monthly_salary_saved*semi_annual_raise
    if current_savings < portion_down_payment and low != high:
        low = guess
    elif current_savings > portion_down_payment and low != high:
        high = guess
    else:
        print('It is not possible to pay the down payment in three years.')
        exit() #exit and stop running
    steps += 1
print('Savings:', current_savings)
print('Best Savings Rate:', portion_saved)
print('Steps in bisection search:', steps)