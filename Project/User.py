import os
import datetime
import pickle
from Mymodules import *

def create_admin():
    if not os.path.exists('Users.dat'):
        with open('Users.dat', 'ab') as fl:
            dt = datetime.datetime.now().strftime('%x %I:%M %p')
            rc = ['admin', 'admin', 'administrator', 'admin@gmail.com', 'sup', dt]
            pickle.dump(rc, fl)
            
            
def reg_login():
    create_admin()
    global ut
    ud = inpany('User ID : ', '')
    ps = inpany('Password: ', '')
    with open('Users.dat', 'rb') as fl:
        fg = 0    
        while True:
            try:
                ui, pw, nm, ml, ty, tm = pickle.load(fl)
                if ud == ui and ps == pw:
                    if ty == 'reg':
                        ut = 'reg'
                    else:
                        ut = 'sup'
                    fg = 1
                    break               
            except EOFError:
                    break
    if fg == 1:
        if ut == 'reg':
            print('You have sucessfully Logged in as a Regular User !')
        else:
            print('You Have Sucessfully Logged in as an Administrator !')
    else:
        print('Invaild User ID or Password !')
    return ut
    
def userlist():
    print('\nUSER LIST\n')
    if not os.path.exists('Users.dat'):
        print('No User Created !')
    else:
        with open('Users.dat', 'rb') as fl:
            print('%-6s %-15s %-15s %-25s %-8s %-20s' %
                  ('SNo.', 'User ID', 'Name', 'Mail', 'Type', 'Time'))
            sl = 1
            while True:
                try:
                    ui, pw, nm, ml, ty, tm = pickle.load(fl)                    
                    if ty == 'reg':
                        ty = 'Regular'
                    else: ty = 'Admin'
                    print('%-6s %-15s %-15s %-25s %-8s %-20s' %
                              (sl, ui, nm, ml, ty, tm))
                    sl += 1
                except EOFError:
                    break
            
def register():
    print('New User Details...\n')

    ud = inpany('User ID : ', '')
    pw = inpany('Password: ', '')
    nm = inpany('Name    : ', '')
    ma = inpany('Mail    : ', '')
    tp = 'reg'
    print()
    if input('Add User(y/n): ').lower() == 'y':
        dt = datetime.datetime.now().strftime('%x %I:%M %p')
        with open('users.dat', 'ab') as fl:
            pickle.dump([ud, pw, nm, ma, tp, dt], fl)
        print('\nUser Added !')
    else:
        print('\nCancelled !')
        
def edit_user():
    print('EDITING USER\n')

    ud = input('User ID: ')
    print()

    with open('users.dat', 'rb') as fl:
        flag = False
        rs = []
        while True:
            try:
                ui, pw, nm, ml, ty, tm = pickle.load(fl)               
                if ud == ui:
                    flag = True
                    print('Current Info...')
                    print('User ID :', ui)
                    print('Password:', pw)
                    print('Name    :', nm)
                    print('Mail    :', ml)
                    print('\n')
                    print('Edit Info...')
                    pw = inpany('Password: ', '')
                    nm = inpany('Name    : ', '')
                    ml = inpany('Mail    : ', '')   
                rs.append([ui, pw, nm, ml, ty, tm])
                         
            except EOFError:
                break
                    
    if flag:
        print()
        if input('Confirm Edit(y/n): ').lower() == 'y':
            fl = open('users.dat', 'wb')
            for rc in rs:
                pickle.dump(rc, fl)
            fl.close()
            print('Edited !')
        else:
            print('Editing Cancelled !')
            
    else:
        print('Given User ID Not Found !')

def remove_user():        
    print('REMOVE USER\n')

    ud = input('User ID : ')
    ps = input('Password: ')
    print()
    with open('users.dat', 'rb') as fl:
        flag = False
        rs = []
        while True:
            try:
                ui, pw, nm, ml, ty, tm = pickle.load(fl)               
                if ud == ui and ps == pw:
                    flag = True
                    print('Current Info...')
                    print('User ID :', ui)
                    print('Password:', pw)
                    print('Name    :', nm)
                    print('Mail    :', ml)
                else:
                    rs.append([ui, pw, nm, ml, ty, tm])                    
            except EOFError:
                break
    if flag:
        print()
        if input('Confirm Remove(y/n): ').lower() == 'y':
            with open('users.dat', 'wb') as fl:
                for rc in rs:
                   pickle.dump(rc, fl)
            print('Removed!')
        else:
            print('Removing Cancelled !')
            
    else:
        print('Given password Not Found !')
                
def reg_menu():    
    rg = '''
    REGISTER
    
    1. New Registeration
    2. Users List
    3. Edit User Details
    4. Remove User
    5. Return to Main Menu

    Enter Choice(1-5): '''

    while True:
        nu = input(rg)
        print()
        
        if  nu == '1':
            register()
        elif nu == '2':
            userlist()
        elif nu == '3':
            edit_user()
        elif nu == '4':
            remove_user()
        elif nu == '5':
            break
        else:
            print('Invalid Choice !')

