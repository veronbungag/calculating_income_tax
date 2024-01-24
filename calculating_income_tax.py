#define a function for calculating income tax
def calculate_income_tax(income):
    #add taxable income as 0
    taxable_income = 0
#if income is less than or equal 10000
    if income <= 10000:
        taxable_income = 0
    elif income <= 20000:
        #0% tax rate on first 10,000
        tax = income - 10000
        #10% tax rate 
        taxable_income = tax * 10 / 100
    else:
    #first 10,000
        taxable_income = 0
#next 10,000 10% tax
#remaining 20% tax rate
#return taxable income
#add income value and calculate income tax
#print the income tax payable