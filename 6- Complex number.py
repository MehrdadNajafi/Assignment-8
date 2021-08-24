def show_menu():
    print('1- Sum', '\n2- Submission', '\n3- Multiplication', '\n4- Exit')

def get_input():
    real_part = int(input('Enter the real part of the number: '))
    imaginary_part = int(input('Enter the imaginary part of the number: '))
    Complex_number = {'real' : real_part, 'imaginary' : imaginary_part}

    real_part_2 = int(input('Enter the real part of the number: '))
    imaginary_part_2 = int(input('Enter the imaginary part of the number: '))
    Complex_number_2 = {'real' : real_part_2, 'imaginary' : imaginary_part_2}

    return Complex_number , Complex_number_2

def show(num):
    print('Result is:', num['real'], '+', str(num['imaginary']) + 'i')

def SUM(num1,num2):
    result = {}
    result['real'] = num1['real'] + num2['real']
    result['imaginary'] = num1['imaginary'] + num2['imaginary']
    
    return result

def Submission(num1,num2):
    result = {}
    result['real'] = num1['real'] - num2['real']
    result['imaginary'] = num1['imaginary'] - num2['imaginary']

    return result

def Multiplication(num1,num2):
    result = {}
    result['real'] = ( num1['real'] * num2['real'] - num1['imaginary'] * num2['imaginary'] )
    result['imaginary'] = ( num1['real'] * num2['imaginary'] + num1['imaginary'] * num2['real'] )

    return result

while True:
    show_menu()
    user_choice = int(input('Please choose an option: '))

    if user_choice == 1:
        num1 , num2 = get_input()
        show(SUM(num1,num2))
        pass

    elif user_choice == 2:
        num1 , num2 = get_input()
        show(Submission(num1,num2))
        pass

    elif user_choice == 3:
        num1 , num2 = get_input()
        show(Multiplication(num1,num2))
        pass

    elif user_choice == 4:
        break