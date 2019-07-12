# ctor2.py

class Const:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    def show_data(self):
        print (self.n1, self.n2)

def main():
    o1 = Const(1, 2)
    o2 = Const(3, 4)

    o1.show_data()
    o2.show_data()
    
main()
