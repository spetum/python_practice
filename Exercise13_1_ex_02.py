# Exercise13_1_ex_02.py

class Friend:

    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def get_name(self):
        #print(self.name)
        return self.name
    def get_phone(self):
        #print(self.phoneNumber)
        return self.phoneNumber

    def set_phone(self, phoneNumber):
        self.phoneNumber = phoneNumber

    def show_info(self):
        print("Name : ", self.name)
        print("Phone: ", self.phoneNumber)



def main():
    f1 = Friend("윤지민", "010-111-2222")
    f2 = Friend("이선준", "010-333-4444")
    f3 = Friend("장지우", "010-555-6666")
    f4 = Friend("윤지율", "010-777-8888")

    f_list = []
    f_list.append(f1)
    f_list.append(f2)
    f_list.append(f3)
    f_list.append(f4)

    for i in f_list:
        i.show_info()


main()
