# this file is used for Accessing code of another module in src
# accessing one code in a file into another file code is modular coding
from src.person import Person


obj=Person("Pavan","Kumar")
obj.display()

from src.car import car
obj= car("BMW","Black")
obj.drive()
#OTHER forms
"""import src

obj=src.person.Person()"""