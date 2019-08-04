# property Decorator
# 함수 혹은 메소드이지만 속성처럼 처리하는 방법을 의미한다.
# 간혹 속성을 직접 바꾸려는 것을 막기 위해 사용한다고 한다.

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # email 속성을 아래의 함수 혹은 메소드로 바꿔보자.
        # self.email = first +'.'+ last + '@email.com'
        # 이어서 속성 데코레이터(@property)를 부착하여보자.

    @property
    def email(self):
        # return self.first +'.'+ self.last + '@email.com'
        return '{}.{}@email.com'.format(self.first, self.last)

    # fullname을 속성으로 변신
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # 함수가 속성 데코레이터에 의해 속성이 되었을 때 그 속성의 내용을 바꾸려면
    @fullname.setter
    def fullname(self, name):
        first , last = name.split(' ') 
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('delete name! {}'.format(self.fullname))
        self.first = None
        self.last = None
        
emp_1 = Employee('John', 'Smith')

emp_1.first = 'Jim'

print(emp_1.first)
print(emp_1.last)

## 해당 함수 혹은 메소드에 @property가 붙으면 함수호출이 안된다.
## 아래의 오류가 발생
## TypeError: 'str' object is not callable 
# print(emp_1.email()) 
# print(emp_1.fullname()) 

print(emp_1.email)
print(emp_1.fullname)

## 당연히 속성 데코레이터가 붙어 있어서 속성이 된 것 뿐이지
## 본질은 함수 혹은 메소드이기 때문에 변형된 속성의 setter의
## 정의 없이 값의 배정이나 직접적인 변경이 불가능하다.
## 아래의 오류가 발생
## AttributeError: can't set attribute
# emp_1.fullname = "Juan.P Lee"

emp_1.fullname = "Juan.P Lee"
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
