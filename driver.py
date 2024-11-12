from bbb import person
class driver(person):

   def __init__(self,first_name,last_name):
       self.first_name = first_name
       self.last_name = last_name

def get_license_level(self,licence):


        if licence == "a":
            print(f"dhe driver allow to use only motorcycle")
        elif  licence == "b":
            print(f'dhe driver allow to use only a truck')
        elif licence == "c":
            print(f'dhe driver allow to use only a car')
        else:
            print("אחי אין לך רישיון שחרר")
