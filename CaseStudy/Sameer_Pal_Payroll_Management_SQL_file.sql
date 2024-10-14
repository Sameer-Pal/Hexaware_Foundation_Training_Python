CREATE DATABASE PayXpert;
use PayXpert;

CREATE TABLE Employee (
    EmployeeID INT IDENTITY PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    DateOfBirth DATE NOT NULL,
    Gender VARCHAR(10) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE,
    PhoneNumber VARCHAR(15) NOT NULL,
    Address TEXT NOT NULL,
    Position VARCHAR(50) NOT NULL,
    JoiningDate DATE NOT NULL,
    TerminationDate DATE
);



INSERT INTO Employee (FirstName, LastName, DateOfBirth, Gender, Email, PhoneNumber, Address, Position, JoiningDate)
VALUES ('', '', '2023-01-01', 'Male', 'test@test.com', '9876543210', '', '', '2023-01-01');

select * from Payroll
select * from Employee

select * from FinancialRecord


select * from Tax


CREATE TABLE Payroll (
    PayrollID INT IDENTITY PRIMARY KEY,
    EmployeeID INT,
    PayPeriodStartDate DATE NOT NULL,
    PayPeriodEndDate DATE NOT NULL,
    BasicSalary DECIMAL(10, 2) NOT NULL,
    OvertimePay DECIMAL(10, 2) DEFAULT 0.00,
    Deductions DECIMAL(10, 2) DEFAULT 0.00,
    NetSalary DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

select* from Payroll;
CREATE TABLE Tax (
    TaxID INT IDENTITY PRIMARY KEY,
    EmployeeID INT,
    TaxYear INT NOT NULL,  -- Use INT to store the year
    TaxableIncome DECIMAL(10, 2) NOT NULL,
    TaxAmount DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

CREATE TABLE FinancialRecord (
    RecordID INT IDENTITY PRIMARY KEY,
    EmployeeID INT,
    RecordDate DATE NOT NULL,
    Description VARCHAR(255) NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    RecordType VARCHAR(50) NOT NULL,
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

select * from FinancialRecord;

INSERT INTO Employee (FirstName, LastName, DateOfBirth, Gender, Email, PhoneNumber, Address, Position, JoiningDate)
VALUES
('John', 'Doe', '1985-02-15', 'Male', 'john.doe@example.com', '1234567890', '123 Elm St, CityA', 'Software Engineer', '2020-01-10'),
('Jane', 'Smith', '1990-05-20', 'Female', 'jane.smith@example.com', '1234567891', '124 Elm St, CityA', 'Data Analyst', '2019-03-15'),
('Alice', 'Johnson', '1988-07-25', 'Female', 'alice.johnson@example.com', '1234567892', '125 Elm St, CityA', 'HR Manager', '2021-02-01'),
('Bob', 'Williams', '1975-09-30', 'Male', 'bob.williams@example.com', '1234567893', '126 Elm St, CityA', 'Project Manager', '2018-05-20'),
('Charlie', 'Brown', '1995-12-05', 'Male', 'charlie.brown@example.com', '1234567894', '127 Elm St, CityA', 'UI/UX Designer', '2022-07-30'),
('Eve', 'Davis', '1992-04-18', 'Female', 'eve.davis@example.com', '1234567895', '128 Elm St, CityA', 'DevOps Engineer', '2021-11-10'),
('Grace', 'Wilson', '1983-11-12', 'Female', 'grace.wilson@example.com', '1234567896', '129 Elm St, CityA', 'QA Engineer', '2020-09-25'),
('Henry', 'Miller', '1991-06-15', 'Male', 'henry.miller@example.com', '1234567897', '130 Elm St, CityA', 'Network Administrator', '2022-02-14'),
('Isabella', 'Moore', '1986-01-22', 'Female', 'isabella.moore@example.com', '1234567898', '131 Elm St, CityA', 'Marketing Specialist', '2019-08-30'),
('Jack', 'Taylor', '1994-03-28', 'Male', 'jack.taylor@example.com', '1234567899', '132 Elm St, CityA', 'Sales Executive', '2023-04-05');

select * from Employee
INSERT INTO Payroll (EmployeeID, PayPeriodStartDate, PayPeriodEndDate, BasicSalary, OvertimePay, Deductions, NetSalary)
VALUES
(1, '2023-01-01', '2023-01-15', 3000.00, 200.00, 150.00, 3050.00),
(2, '2023-01-01', '2023-01-15', 2800.00, 150.00, 120.00, 2830.00),
(3, '2023-01-01', '2023-01-15', 3200.00, 250.00, 200.00, 3250.00),
(4, '2023-01-01', '2023-01-15', 4000.00, 300.00, 250.00, 4050.00),
(5, '2023-01-01', '2023-01-15', 3500.00, 180.00, 170.00, 3510.00),
(6, '2023-01-01', '2023-01-15', 3300.00, 220.00, 200.00, 3320.00),
(7, '2023-01-01', '2023-01-15', 3000.00, 150.00, 180.00, 2970.00),
(8, '2023-01-01', '2023-01-15', 3100.00, 160.00, 190.00, 3070.00),
(9, '2023-01-01', '2023-01-15', 3600.00, 190.00, 160.00, 3630.00),
(10, '2023-01-01', '2023-01-15', 3400.00, 170.00, 200.00, 3370.00);


INSERT INTO Tax (EmployeeID, TaxYear, TaxableIncome, TaxAmount)
VALUES
(1, 2022, 25000.00, 3000.00),
(2, 2022, 24000.00, 2900.00),
(3, 2022, 26000.00, 3200.00),
(4, 2022, 30000.00, 4000.00),
(5, 2022, 28000.00, 3500.00),
(6, 2022, 27000.00, 3400.00),
(7, 2022, 25000.00, 3100.00),
(8, 2022, 29000.00, 3700.00),
(9, 2022, 31000.00, 4100.00),
(10, 2022, 30000.00, 3900.00);

INSERT INTO FinancialRecord (EmployeeID, RecordDate, Description, Amount, RecordType)
VALUES
(1, '2023-01-01', 'Salary Payment', 3000.00, 'Credit'),
(2, '2023-01-02', 'Bonus Payment', 500.00, 'Credit'),
(3, '2023-01-03', 'Deduction', -200.00, 'Debit'),
(4, '2023-01-04', 'Overtime Payment', 300.00, 'Credit'),
(5, '2023-01-05', 'Salary Payment', 2800.00, 'Credit'),
(6, '2023-01-06', 'Bonus Payment', 400.00, 'Credit'),
(7, '2023-01-07', 'Deduction', -150.00, 'Debit'),
(8, '2023-01-08', 'Overtime Payment', 250.00, 'Credit'),
(9, '2023-01-09', 'Salary Payment', 3200.00, 'Credit'),
(10, '2023-01-10', 'Bonus Payment', 600.00, 'Credit');
select * from FinancialRecord