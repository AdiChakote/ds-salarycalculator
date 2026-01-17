employee_Name = input("Employee Name: ")
daily_salary = int(input("Daily Salary: "))
no_days_worked = int(input("Number of Days Worked: "))

base_salary = daily_salary * no_days_worked

def bonus(salary):
    your_salary = salary + (salary* 10 / 100)
    return your_salary

def deduction(salary):
    your_salary = salary - (salary* 10 / 100)
    return your_salary

if no_days_worked >= 26:
    final_salary = bonus(base_salary)
elif no_days_worked <= 20:
    final_salary = deduction(base_salary)
else:
    final_salary = base_salary

print("Employee Name: ", employee_Name)
print("Your Monthly Salary: ", final_salary)


