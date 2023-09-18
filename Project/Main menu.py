from Mymodules import *
from User import *
from QuestionBank import *
from Topics import *

mn = '''QUIZ PROGRAM

1. Introduction
2. Register
3. Login
4. Take a Test
5. Score sheet
6. Administrator
7. Exit Program

Enter Choice(1-7): '''

ut = ''

ad = '''ADMINISTRATOR

1. Users
2. Topics
3. Question Bank
4. Return to main menu

Enter Choice(1-3): '''

def admin_menu():
    while True:
        co = inpany(ad, '')
        print()
        if co == '1':
            reg_menu()
        elif co == '2':
            topics_menu()
        elif co == '3':
            question_menu()
        elif co == '4':
            break
        else:
            print('Invalid Choice !')
        print('\n')
            
while True:
    ch = inpany(mn, '')
    print()
    if ch == '1':
        intro()
    elif ch == '2':
        register()
    elif ch == '3':
        ut = reg_login()
    elif ch == '6':
        if ut == 'reg':
            print('Only Administrator can use this Option !')
        elif ut == 'sup':
            admin_menu()
        else:
            print('Please Login as Administrator !')
    elif ch == '7':
        break
    else:
        print('Invalid Choice !')
    print('\n')

