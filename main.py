class RentalProperty:
    def __init__(self, purchase_price, rental_income, operating_expenses, holding_period):
        self.purchase_price = purchase_price
        self.rental_income = rental_income
        self.operating_expenses = operating_expenses
        self.holding_period = holding_period

    def calculate_roi(self):
        net_income = self.rental_income - self.operating_expenses
        total_income = net_income * self.holding_period
        total_cost = self.purchase_price * self.holding_period
        return (total_income - total_cost) / total_cost

# Get input values from user
purchase_price = float(input("Enter the purchase price of the property: "))
rental_income = float(input("Enter the monthly rental income: "))
operating_expenses = float(input("Enter the monthly operating expenses: "))
holding_period = int(input("Enter the holding period (in months): "))

# Create RentalProperty object and calculate ROI
property1 = RentalProperty(purchase_price, rental_income, operating_expenses, holding_period)
roi = property1.calculate_roi()

# Print the ROI result
print(f"The Bigger Pockets ROI for this rental property is {roi:.2%}")
