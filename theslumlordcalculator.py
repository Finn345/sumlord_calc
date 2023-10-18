#create a program that will calculate the Return on Investment(ROI) for a rental property using Object Oriented Programming
# ROI = Annual Cash Flow / Total investment
#For Russell, the local slumlord, with love xoxo 
class Calculator:
    def __init__(self):
        self.acf = 0  # Annual Cash Flow
        self.ti = 0   # Total Investment
        self.ri = 0   # Rental Income
        self.li = 0   # Laundry Income
        self.si = 0   # Storage Income
        self.mi = 0   # Misc Income and fees for breathing in the general direction of our property
        self.taxes = 0 #Government sponsered stealing
        self.insur = 0 #Insurance for legal garbage
        self.wat_sew = 0 #Water and sewer
        self.garb = 0 #Garbage collecting
        self.elec = 0 #Electric
        self.hoa = 0 # Theives of joy I mean Home Owners Acolyte
        self.lawncare = 0 #The local gardener men who garden very well
        self.vacancy = 0 #The amount of money wasted on keeping up on empty rooms because I am a scummy landlord
        self.repairs = 0 #For when tenets just dont shut up about a creaky door or leaky faucet
        self.capex = 0 #The money that gets spent for no reason to keep those entitled young ones happy
        self.propmgmt = 0 #Money spent on local scum to run the places I own
        self.mort = 0 #Mortgage payments

    def rent(self):
        self.ri = int(input("Enter your rental income: "))
        self.li = int(input("Enter your laundry income: "))
        self.si = int(input("Enter your storage income: "))
        self.mi = int(input("Enter your misc income: "))

    def cf(self):
        total_expenses = int(input("Enter your total monthly expenses: "))
        mon_inc = self.ri + self.li + self.si + self.mi - total_expenses
        print(f'Your monthly income is {mon_inc}.')
        an_inc = mon_inc * 12
        print(f"Your annual income is {an_inc}.")

    def exp(self):
        self.taxes = int(input("Enter the amount of taxes in dollars: "))
        self.insur = int(input("Enter the amount you pay for insurance in dollars: "))
        self.wat_sew = int(input('Enter your monthly water and sewer bill: '))
        self.garb = int(input("Enter your monthly garbage fees: "))
        self.elec = int(input("Enter your electric bill: "))
        self.hoa = int(input("Enter your HOA fees(even if the HOA are thieves): "))
        self.lawncare = int(input("Enter your lawncare: "))
        self.vacancy = int(input("Enter your vacancy costs: "))
        self.repairs = int(input("Enter your monthly repair cost: "))
        self.capex = int(input("Enter your CapEx: "))
        self.propmgmt = int(input("Enter how much you pay for property management: "))
        self.mort = int(input("Enter how much the mortgage payment is per month: "))

    def cashoncash(self):
        mon_exp = self.taxes + self.insur + self.wat_sew + self.garb + self.elec + self.hoa + self.lawncare + self.vacancy + self.repairs + self.capex + self.propmgmt + self.mort
        dwnpay = int(input("Enter the down payment: "))
        clocost = int(input("Enter the closing costs: "))
        rehbud = int(input("Enter your rehab budget: "))
        misoth = int(input('Enter any other miscellaneous investments: '))
        total_invest = mon_exp + dwnpay + clocost + rehbud + misoth
        print(f"Your total investment is: {total_invest}")
        cashret = (self.acf / total_invest) * 100

        print(f"The cash on cash return with all data provided, totals out to equal {cashret}%!")

# Create an instance of the Calculator class
calculator = Calculator()

# Calculate income and expenses
calculator.rent()
calculator.exp()
calculator.cf()

# Calculate cash-on-cash return
calculator.cashoncash()
