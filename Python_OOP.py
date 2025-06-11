# Python Object-Oriented Programming
    # Classes and Instances
    # Class Variables

class Employee:     #examples of classes are lists, arrays, DataFrames...

    raise_amount = 1.04     # class variable available to each instance of class
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last      
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):     #method
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Omar', 'Orsolino', 145000)
emp_2 = Employee('Amari', 'Orsolino', 0)

#print(Employee.fullname(emp_2))     #method has same output
#print(emp_2.fullname())     #as this one

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)


print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

#print(Employee.__dict__)
