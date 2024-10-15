class Payment:
    def __init__(self, payment_id, order_id, amount, status, payment_date):
        self._payment_id = payment_id  # Unique ID for the payment
        self._order_id = order_id      # Reference to the associated order
        self._amount = amount          # Amount paid
        self._status = status          # Payment status (e.g., "Pending", "Completed", "Failed")
        self._payment_date = payment_date  # Date of payment

    # Getter and Setter for payment_id
    @property
    def payment_id(self):
        return self._payment_id

    @payment_id.setter
    def payment_id(self, value):
        self._payment_id = value

    # Getter and Setter for order_id
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value

    # Getter and Setter for amount
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if value < 0:
            raise ValueError("Amount cannot be negative")
        self._amount = value

    # Getter and Setter for status
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        valid_statuses = ["Pending", "Completed", "Failed"]
        if value not in valid_statuses:
            raise ValueError(f"Status must be one of {valid_statuses}")
        self._status = value

    # Getter and Setter for payment_date
    @property
    def payment_date(self):
        return self._payment_date

    @payment_date.setter
    def payment_date(self, value):
        self._payment_date = value

    # Override __str__ method to display payment information
    def __str__(self):
        return f"Payment ID: {self.payment_id}, Order ID: {self.order_id}, Amount: {self.amount}, Status: {self.status}, Payment Date: {self.payment_date}"
