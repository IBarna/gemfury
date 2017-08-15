class Employee:
    num_of_empl = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_empl += 1

    def full_name(self):
        # print self.first + ' ' + self.last
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay + self.raise_amount)
        #print self.pay

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

import datetime
my_date = datetime.date(2016, 7, 2)

print(Employee.is_workday(my_date))


#print Employee.from_string('John-Doe-2000').first
#print Employee.num_of_empl
