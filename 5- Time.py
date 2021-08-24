def get_input():
    time_1 = input('Please enter first time (hh:mm:ss): ')
    time_1 = time_1.split(':')
    first_time = {'h' : int(time_1[0]), 'm' : int(time_1[1]), 's' : int(time_1[2])}
    
    time_2 = input('Please enter second time (hh:mm:ss): ')
    time_2 = time_2.split(':')
    second_time = {'h' : int(time_2[0]), 'm' : int(time_2[1]), 's' : int(time_2[2])}

    return first_time , second_time

def show_menu():
    print('1- Sum', '\n2- Submission', '\n3- Convert seconds to time', '\n4- Convert time to seconds', '\n5- Exit')

def show(time):
    print(f"{time['h']}:{time['m']}:{time['s']}")


def SUM(time1,time2):
    result = {}
    result['h'] = time1['h'] + time2['h']
    result['m'] = time1['m'] + time2['m']
    result['s'] = time1['s'] + time2['s']

    if result['s'] >=60 :
        result['m'] += (result['s'] // 60)
        result['s'] = result['s'] % 60
        
    if result['m'] >=60 :
        result['h'] += (result['m'] // 60)
        result['m'] = result['m'] % 60
        
    return result
    
def Submission(time1,time2):
    result = {}
    result['h'] = time1['h'] - time2['h']
    result['m'] = time1['m'] - time2['m']
    result['s'] = time1['s'] - time2['s']

    if result['s'] < 0:
        while result['s'] < 0:
            result['m'] -= 1
            result['s'] += 60
    
    if result['m'] < 0:
        while result['m'] < 0:
            result['h'] -= 1
            result['m'] += 60

    if result['h'] < 0:
        return 'This can not be calculated'

    else:
        return result
    

def seconds_to_time():
    seconds = int(input('Pls enter seconds: '))
    if seconds >= 60:
        min = seconds // 60
        seconds = seconds % 60
    if min >= 60:
        hour = min // 60
        min = min % 60
    time = {'h' : hour, 'm' : min, 's' : seconds}

    return time

def time_to_seconds():
    time = input('Pls enter time (hh:mm:ss): ')
    time = time.split(':')
    my_time = {'h' : int(time[0]), 'm' : int(time[1]), 's' : int(time[2])}
    seconds = 0
    seconds += my_time['s']
    seconds += (my_time['m'] * 60)
    seconds += (my_time['h'] * 3600)

    return seconds


while True:
    show_menu()
    user_choice = int(input('Please choose an option: '))

    if user_choice == 1:
        time1 , time2 = get_input()
        show(SUM(time1,time2))
    
    elif user_choice == 2:
        time1 , time2 = get_input()
        try:
            show(Submission(time1,time2))
        except:
            print(Submission(time1,time2))

    elif user_choice == 3:
        show(seconds_to_time())

    elif user_choice == 4:
        print(time_to_seconds())

    elif user_choice == 5:
        break