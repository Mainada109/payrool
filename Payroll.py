#PYTHON ON PAYROLL

import math

class Employee():
    def __init__(self,id,name):
        self.id=id
        self.name=name
ID_No=int(input("Enter the ID Number:"))
print("Employee Name:",ID_No)
Name=input("Enter the name:")
print("Name of Employee:",Name)
    

class SalaryEmployee(Employee):
    
    def __init__(self,id,name,basic_salary,allowance):
        super().__init__(id,name)
        self.basic_salary=basic_salary
        self.allowance=allowance
    
    def calculate_payroll(self):
        Bsalary=self.basic_salary+self.allowance
        return math.trunc(Bsalary)

class HourlyEmployee(Employee):
    def __init__(self,id,name,Hourly_worked,Hourly_pay):
        super().__init__(id,name)
        self.Hourly_worked=Hourly_worked
        self.Hourly_pay=Hourly_pay
    
    def calculate_payroll(self):
        Wpay=self.Hourly_worked*self.Hourly_pay
        return math.trunc(Wpay)

class CommissionEmployee(SalaryEmployee):

    def __init__(self,id,name,commssion,basic_salary,allowance):
        super().__init__(id,name,basic_salary,allowance)
        self.commission=commssion
    
    def calculate_payroll(self):
         Commision=(self.basic_salary+self.allowance)*0.03
         return math.trunc(Commision)
    

Edetails= CommissionEmployee()
Edetails.calculate_payroll()
Edetails.__init__()
        