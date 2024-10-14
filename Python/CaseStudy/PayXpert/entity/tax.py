class Tax:
    def __init__(self, tax_id=None, employee_id=None, tax_year=None, taxable_income=0.0, 
                 tax_amount=0.0):
        self.__tax_id = tax_id
        self.__employee_id = employee_id
        self.__tax_year = tax_year
        self.__taxable_income = taxable_income
        self.__tax_amount = tax_amount

    # Getters and Setters
    # (Similar structure as Employee class)
    # Getter and Setter for tax_id
    @property
    def tax_id(self):
        return self.__tax_id

    @tax_id.setter
    def tax_id(self, tax_id):
        self.__tax_id = tax_id

    # Getter and Setter for employee_id
    @property
    def employee_id(self):
        return self.__employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        self.__employee_id = employee_id

    # Getter and Setter for tax_year
    @property
    def tax_year(self):
        return self.__tax_year

    @tax_year.setter
    def tax_year(self, tax_year):
        self.__tax_year = tax_year

    # Getter and Setter for taxable_income
    @property
    def taxable_income(self):
        return self.__taxable_income

    @taxable_income.setter
    def taxable_income(self, taxable_income):
        if taxable_income < 0:
            raise ValueError("Taxable income cannot be negative.")
        self.__taxable_income = taxable_income

    # Getter and Setter for tax_amount
    @property
    def tax_amount(self):
        return self.__tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        if tax_amount < 0:
            raise ValueError("Tax amount cannot be negative.")
        self.__tax_amount = tax_amount

    def calculate_tax(self, tax_rate):
        """Calculate the tax amount based on taxable income and a given tax rate."""
        if tax_rate < 0:
            raise ValueError("Tax rate cannot be negative.")
        self.__tax_amount = self.__taxable_income * tax_rate
        return self.__tax_amount

    def __str__(self):
        return (f"Tax(tax_id={self.__tax_id}, employee_id={self.__employee_id}, "
                f"tax_year={self.__tax_year}, taxable_income={self.__taxable_income}, "
                f"tax_amount={self.__tax_amount})")
