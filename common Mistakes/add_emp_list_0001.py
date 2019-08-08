
## default argument의 life cycle
## emp_list=[]로 하면 계속 살아있음.
def add_employee(emp, emp_list=[]):
    emp_list.append(emp)
    print(emp_list)

emps = ['John', 'Jane']

#add_employee('corey', emps)
add_employee('corey')
add_employee('John')
add_employee('Jane')


def add_emp_list(emp, emp_list=None):
    if emp_list is None:
        emp_list = []
    
    emp_list.append(emp)
    print(emp_list)

add_emp_list('corey')
add_emp_list('John')
add_emp_list('Jane')

employees = [] 
add_emp_list('Conray', employees)
add_emp_list('Johan', employees)
add_emp_list('Janett', employees)
