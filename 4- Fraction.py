def get_input():
    s = int(input('Please enter The numerator:'))
    m = int(input('Please enter Denominator:'))
    a = {'s':s, 'm':m}

    s_2 = int(input('Please enter The numerator:'))
    m_2 = int(input('Please enter Denominator:'))
    b = {'s':s_2, 'm':m_2}
    
    return a,b

def show(x):
    print(x['s'], '/', x['m'])

def show_menu():
    print('1- sum', '\n2- Submission', '\n3- Multiplication', '\n4- Division', '\n5- Exit')

def SUM(x,y):
    result = {}
    
    if x['m'] == y['m']:
        result['s'] = x['s'] + y['s']
        result['m'] = x['m']
    
    else:
        result['s'] = (x['s'] * y['m']) + (y['s'] * x['m'])
        result['m'] = x['m'] * y['m']
    
    return result

def Submission(x,y):
    result = {}
    result['s'] = x['s'] - y['s']
    result['m'] = x['m'] - y['m']

    if result['s'] < 0 and result['m'] < 0:
        result['m'] = abs(result['m'])

    return result

def Multiplication(x,y):
    result = {}
    result['s'] = x['s'] * y['s']
    result['m'] = x['m'] * y['m']

    return result

def Division(x,y):
    result = {}
    result['s'] = x['s'] * y['m']
    result['m'] = x['m'] * y['s']

    return result

while True:
    show_menu()

    user_choice = int(input('Please choose an option: '))

    if user_choice == 1:
        a,b = get_input()
        show(SUM(a,b))

    elif user_choice == 2:
        a,b = get_input()
        show(Submission(a,b))

    elif user_choice == 3:
        a,b = get_input()
        show(Multiplication(a,b))

    elif user_choice == 4:
        a,b = get_input()
        show(Division(a,b))

    elif user_choice == 5:
        break