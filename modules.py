# modules and packages
# modules - pieces of code split into logical sections. these python files can be imported and reused
# packages - a collection of modules

#Example:
from classes import Employee

chiya = Employee('chiya', 2000, 5)
print(f'Employee name: {chiya.name}')
print(f'Salary: {chiya.salary}')
print(f'time spent at work: {chiya.duration}')
print(chiya.time_spent())


#Package
#setup:
# create folder
# add __init__.py file
#add other py files in folder