# Exercise13_1_ex_03.py

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

    print("윤씨 성을 가진 사람들의 명단을 출력하시오.")
    for i in f_list:
        if i.get_name().startswith('윤'):
            i.show_info()


main()
