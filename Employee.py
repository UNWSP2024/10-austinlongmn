# Programmer: Austin Long
# Date: 2025-03-28
# Program: Employee Class

# Program #4 Employee Class:
# Write a class Employee that holds the following data about an employee in attributes: name, ID number, department, and job title.

# Once you have written the class, write a program that creates three Employee objects to hold the following data.

# Name	ID Number	Department	Job Title
# Susan Meyers	47899 	Accounting	Vice President
# Mark Jones	39119	IT	Programmer
# Joy Rogers	81774	Manufacturing	Engineer
# The program should store the data in the three objects, then display the data for each employee on the screen.


# Define Employee class
class Employee:
    def __init__(self, name, id_number, department, job_title) -> None:
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__job_title = job_title

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_id_number(self):
        return self.__id_number

    def set_id_number(self, id_number):
        self.__id_number = id_number

    def get_department(self):
        return self.__department

    def set_department(self, department):
        self.__department = department

    def get_job_title(self):
        return self.__job_title

    def set_job_title(self, job_title):
        self.__job_title = job_title

    def __str__(self):
        return (
            f"{self.get_name()}: ID: {self.get_id_number()}, Dept.: "
            f"{self.get_department()}, Job Title: {self.get_job_title()}"
        )


employee_1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
employee_2 = Employee("Mark Jones", 39119, "IT", "Programmer")
employee_3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

print(employee_1)
print(employee_2)
print(employee_3)
