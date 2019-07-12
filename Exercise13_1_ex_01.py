# Exercise13_1_ex_01.py

class Friend:

    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def get_name(self):
        print(self.name)
    def get_phone(self):
        print(self.phoneNumber)

    def set_phone(self, phoneNumber):
        self.phoneNumber = phoneNumber

    def show_info(self):
        print("Name : ", self.name)
        print("Phone: ", self.phoneNumber)



def main():
    f = Friend("Lee", "121-3312-9894")
    #f.get_name()
    f.show_info()


main()
