class FinancialRecord:
    def __init__(self, record_id=None, employee_id=None, record_date=None, 
                 description=None, amount=0.0, record_type=None):
        self.__record_id = record_id
        self.__employee_id = employee_id
        self.__record_date = record_date
        self.__description = description
        self.__amount = amount
        self.__record_type = record_type

    # Getters and Setters
    # (Similar structure as Employee class)
    # Getter and Setter for record_id
    @property
    def record_id(self):
        return self.__record_id

    @record_id.setter
    def record_id(self, record_id):
        self.__record_id = record_id

    # Getter and Setter for employee_id
    @property
    def employee_id(self):
        return self.__employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        self.__employee_id = employee_id

    # Getter and Setter for record_date
    @property
    def record_date(self):
        return self.__record_date

    @record_date.setter
    def record_date(self, record_date):
        self.__record_date = record_date

    # Getter and Setter for description
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    # Getter and Setter for amount
    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        self.__amount = amount

    # Getter and Setter for record_type
    @property
    def record_type(self):
        return self.__record_type

    @record_type.setter
    def record_type(self, record_type):
        self.__record_type = record_type

    def __str__(self):
        return (f"FinancialRecord(record_id={self.__record_id}, employee_id={self.__employee_id}, "
                f"record_date={self.__record_date}, description='{self.__description}', "
                f"amount={self.__amount}, record_type='{self.__record_type}')")
