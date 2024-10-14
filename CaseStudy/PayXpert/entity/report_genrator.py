class ReportGenerator:
    def __init__(self):
        self.reports = []

    def generate_payroll_report(self, payroll_data):
        """Generate a payroll report from the provided payroll data."""
        if not isinstance(payroll_data, list) or not payroll_data:
            raise ValueError("Payroll data must be a non-empty list.")

        report_lines = ["Payroll Report"]
        report_lines.append("=" * 30)
        
        for payroll in payroll_data:
            report_lines.append(f"Employee ID: {payroll['EmployeeID']}")
            report_lines.append(f"Pay Period: {payroll['PayPeriodStartDate']} to {payroll['PayPeriodEndDate']}")
            report_lines.append(f"Basic Salary: ${payroll['BasicSalary']:.2f}")
            report_lines.append(f"Overtime Pay: ${payroll['OvertimePay']:.2f}")
            report_lines.append(f"Deductions: ${payroll['Deductions']:.2f}")
            total_pay = payroll['BasicSalary'] + payroll['OvertimePay'] - payroll['Deductions']
            report_lines.append(f"Total Pay: ${total_pay:.2f}")
            report_lines.append("-" * 30)

        self.reports.append("\n".join(report_lines))
        print("\n".join(report_lines))

    def generate_tax_report(self, tax_data):
        """Generate a tax report from the provided tax data."""
        if not isinstance(tax_data, list) or not tax_data:
            raise ValueError("Tax data must be a non-empty list.")

        report_lines = ["Tax Report"]
        report_lines.append("=" * 30)

        for tax in tax_data:
            report_lines.append(f"Employee ID: {tax['EmployeeID']}")
            report_lines.append(f"Tax Year: {tax['TaxYear']}")
            report_lines.append(f"Tax Amount: ${tax['TaxAmount']:.2f}")
            report_lines.append("-" * 30)

        self.reports.append("\n".join(report_lines))
        print("\n".join(report_lines))

    def generate_financial_record_report(self, financial_data):
        """Generate a financial record report from the provided financial record data."""
        if not isinstance(financial_data, list) or not financial_data:
            raise ValueError("Financial record data must be a non-empty list.")

        report_lines = ["Financial Record Report"]
        report_lines.append("=" * 30)

        for record in financial_data:
            report_lines.append(f"Employee ID: {record['EmployeeID']}")
            report_lines.append(f"Date: {record['RecordDate']}")
            report_lines.append(f"Description: {record['Description']}")
            report_lines.append(f"Amount: ${record['Amount']:.2f}")
            report_lines.append(f"Record Type: {record['RecordType']}")
            report_lines.append("-" * 30)

        self.reports.append("\n".join(report_lines))
        print("\n".join(report_lines))

# Example Usage
if __name__ == "__main__":
    payroll_data = [
        {
            'EmployeeID': 1,
            'PayPeriodStartDate': '2023-01-01',
            'PayPeriodEndDate': '2023-01-15',
            'BasicSalary': 3000,
            'OvertimePay': 200,
            'Deductions': 100
        },
        {
            'EmployeeID': 2,
            'PayPeriodStartDate': '2023-01-01',
            'PayPeriodEndDate': '2023-01-15',
            'BasicSalary': 3200,
            'OvertimePay': 150,
            'Deductions': 80
        }
    ]

    tax_data = [
        {
            'EmployeeID': 1,
            'TaxAmount': 500,
            'TaxYear': 2023
        },
        {
            'EmployeeID': 2,
            'TaxAmount': 600,
            'TaxYear': 2023
        }
    ]

    financial_data = [
        {
            'EmployeeID': 1,
            'RecordDate': '2023-01-10',
            'Description': 'Bonus',
            'Amount': 1000,
            'RecordType': 'Income'
        },
        {
            'EmployeeID': 2,
            'RecordDate': '2023-01-15',
            'Description': 'Expense',
            'Amount': 200,
            'RecordType': 'Expense'
        }
    ]

    report_gen = ReportGenerator()
    report_gen.generate_payroll_report(payroll_data)
    report_gen.generate_tax_report(tax_data)
    report_gen.generate_financial_record_report(financial_data)
