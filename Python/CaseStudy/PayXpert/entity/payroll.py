class Payroll:
    def __init__(self, payroll_id=None, employee_id=None, pay_period_start_date=None, 
                 pay_period_end_date=None, basic_salary=0.0, overtime_pay=0.0, 
                 deductions=0.0, net_salary=0.0):
        self.__payroll_id = payroll_id
        self.__employee_id = employee_id
        self.__pay_period_start_date = pay_period_start_date
        self.__pay_period_end_date = pay_period_end_date
        self.__basic_salary = basic_salary
        self.__overtime_pay = overtime_pay
        self.__deductions = deductions
        self.__net_salary = net_salary

    # Getters and Setters
    # (Similar structure as Employee class)
    # Getter and Setter for payroll_id
    @property
    def payroll_id(self):
        return self.__payroll_id

    @payroll_id.setter
    def payroll_id(self, payroll_id):
        self.__payroll_id = payroll_id

    # Getter and Setter for employee_id
    @property
    def employee_id(self):
        return self.__employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        self.__employee_id = employee_id

    # Getter and Setter for pay_period_start_date
    @property
    def pay_period_start_date(self):
        return self.__pay_period_start_date

    @pay_period_start_date.setter
    def pay_period_start_date(self, pay_period_start_date):
        self.__pay_period_start_date = pay_period_start_date

    # Getter and Setter for pay_period_end_date
    @property
    def pay_period_end_date(self):
        return self.__pay_period_end_date

    @pay_period_end_date.setter
    def pay_period_end_date(self, pay_period_end_date):
        self.__pay_period_end_date = pay_period_end_date

    # Getter and Setter for basic_salary
    @property
    def basic_salary(self):
        return self.__basic_salary

    @basic_salary.setter
    def basic_salary(self, basic_salary):
        if basic_salary < 0:
            raise ValueError("Basic salary cannot be negative.")
        self.__basic_salary = basic_salary

    # Getter and Setter for overtime_pay
    @property
    def overtime_pay(self):
        return self.__overtime_pay

    @overtime_pay.setter
    def overtime_pay(self, overtime_pay):
        if overtime_pay < 0:
            raise ValueError("Overtime pay cannot be negative.")
        self.__overtime_pay = overtime_pay

    # Getter and Setter for deductions
    @property
    def deductions(self):
        return self.__deductions

    @deductions.setter
    def deductions(self, deductions):
        if deductions < 0:
            raise ValueError("Deductions cannot be negative.")
        self.__deductions = deductions

    # Getter and Setter for net_salary
    @property
    def net_salary(self):
        return self.__net_salary

    @net_salary.setter
    def net_salary(self, net_salary):
        if net_salary < 0:
            raise ValueError("Net salary cannot be negative.")
        self.__net_salary = net_salary

    def calculate_net_salary(self):
        """Calculate net salary based on basic salary, overtime pay, and deductions."""
        self.__net_salary = (self.__basic_salary + self.__overtime_pay) - self.__deductions
        return self.__net_salary

    def __str__(self):
        return (f"Payroll(payroll_id={self.__payroll_id}, employee_id={self.__employee_id}, "
                f"pay_period_start_date={self.__pay_period_start_date}, "
                f"pay_period_end_date={self.__pay_period_end_date}, "
                f"basic_salary={self.__basic_salary}, overtime_pay={self.__overtime_pay}, "
                f"deductions={self.__deductions}, net_salary={self.__net_salary})")

