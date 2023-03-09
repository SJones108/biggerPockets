class ROI:
    def __init__(self) -> None:
        self.sum= None
        self.expense= None
        self.income = None
        self.tmd = None

    def getIncome(self):
       rental_income = int(input("What is your monthly rent charge going to be? "))
       laundry = int(input("What is your monthly laundry charge? "))
       storage = int(input("What is your monthly storage charge? "))
       misc = int(input("What is your monthly misc charge? "))
       mi = (rental_income + laundry + storage + misc)
       self.income = mi
       print(f'You will make ${self.income} a month from this')
  
    def expenses(self):
        taxes = int(input("How much are taxes? "))
        insurance= int(input("What is your Insurance charge? "))
        utilities =int(input("How much are utilities? "))
        mortgage = int(input("What is the mortgage cost you pay? "))
        repairs = int(input("What is the cost of repairs and cap expenses you budgeted? "))
        propmang = int(input("What is the monthly cost for your property manager? "))
        self.expense = (taxes + insurance + utilities + mortgage + repairs + propmang)
        print(f'You will pay ${self.expense} a month from this')
       
    def cashflow(self):
        self.tmd = (self.expense-self.income)

    def annualCash(self):
        downpayment = int(input("How much are you putting down? "))
        cc = int(input("How much are the closing cost? "))
        rehab = int(input("What is your rehab budget per month? "))
        ti = (downpayment) + (cc) + (rehab)
        
        self.cashflow()
        cash = (self.tmd/ti)*100
        print(f' Your ROI on this property is {round(cash,2)} %. ')
          
    def run(self):
        info = input("Do you want to find the ROI for a proprty? or enter Q to quit")
        while info != 'Q':
            if info:
                self.getIncome()
                self.expenses()
                self.annualCash()
                break

r = ROI()
r.run()