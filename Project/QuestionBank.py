import pickle
from Mymodules import *
import datetime
from Topics import *
tn = 0
qn = 0
def find_next_qn(tr):
    qq = 1
    with open('questions.dat', 'ab+') as fl:
        fl.seek(0)
        while True:
            try:
                tn, qn, qe, o1, o2, o3, o4, aw  = pickle.load(fl)
                if tr == tn:
                    qq = qn + 1
            except EOFError:
                break
    return qq

def inputqn(tn, qn):
    qe = inpany('Question : ', '')
    print()
    o1 = inpany('Option a): ', '')
    o2 = inpany('Option b): ', '')
    o3 = inpany('Option c): ', '')
    o4 = inpany('Option d): ', '')
    print()
    aw = inpany('Answer(a/b/c/d): ', '')
    return [tn, qn, qe, o1, o2, o3, o4, aw]

def printqn(rc):
    tn, qn, qe, o1, o2, o3, o4, aw = rc
    print('Question No:', qn)
    print('Question   :', qe)
    print('Option a)  :', o1)
    print('Option b)  :', o2)
    print('Option c)  :', o3)
    print('Option d)  :', o4)
    print('Answer(a/b/c/d):', aw)
    print('\n')

def searchqn(tr, op = ''):
    global tn, qn
    qn = inpany('Question No: ', 0)
    flag = False
    with open('questions.dat', 'ab+') as fl:
        fl.seek(0)
        while True:
            try:
                rc = pickle.load(fl)
                if tr == rc[0] and qn == rc[1]:
                    flag = True
                    return rc
            except EOFError:
                break
    if not flag and op == '':
        print('Invalid Question Number !\n')
    return False

def updatefile(rc, rs):
    with open('questions.dat', 'wb') as fl:
        for rc in rs: 
            pickle.dump(rc, fl)
            
def create_qbank():
    global tn
    tp = searchtn()
    if tp:
        tn = tp[0]
        printtn(tp)
        qn = find_next_qn(tn)
        while True:
            print('Question No: ', qn, '\n')
            rc = inputqn(tn, qn)
            if input('Save(y/n): ').lower() == 'y':
                update_qpaper_nq(tn)
                with open('questions.dat', 'ab') as fl:
                    pickle.dump(rc, fl)
                print('\nSaved !\n')
                qn += 1
                if input('More Questions(y/n): ').upper() != 'Y':
                    break
            else:
                print('\nCancelled !')
                
def edit_Question():
    print('EDIT QUESTION\n')
    global tn
    tp = searchtn()
    if tp:
        tn = tp[0]
        rc = searchqn(tn)
        print()
        if rc:
            with open('questions.dat', 'rb') as fl:
                rs = []
                while True:
                    try:
                        rc = pickle.load(fl)                    
                        if tn == rc[0] and qn == rc[1]:
                            print('Current Info...')
                            printqn(rc)
                            print('\n')
                            print('Edit Info...')
                            rc = inputqn(tn, qn)
                        rs.append(rc)                         
                    except EOFError:
                        break
                        
            print()
            if input('Confirm Edit(y/n): ').lower() == 'y':
                updatefile(rc, rs)
                print('Edited !')
            else:
                print('Editing Cancelled !')            

    
def delete_question():
    print('REMOVE QUESTION\n')
    global tn
    tp = searchtn()
    tn = tp[0]
    if tp:
        rc = searchqn(tn)
        if rc:    
            with open('questions.dat', 'rb') as fl:
                rs = []
                while True:
                    try:
                        rc = pickle.load(fl)
                        if tn == rc[0] and qn == rc[1]:
                            print('Current Info...')
                            printqn(rc)
                        else:
                            rs.append(rc)           
                    except EOFError:
                        break
            print()
            if input('Confirm Remove(y/n): ').lower() == 'y':
                updatefile(rc, rs)
                print('Removed!')
            else:
                print('Removing Cancelled !')
                        
def list_question():
    with open('questions.dat', 'ab+') as fl:
        fl.seek(0)
        while True:
            try:
                tn, qn, qe, o1, o2, o3, o4, aw = pickle.load(fl)
                print('Topic No.', tn, '\t', 'Question No.', qn, '\n')
                print('Question:', qe, '\n')
                print('a)', o1)
                print('b)', o2)
                print('c)', o3)
                print('d)', o4)
                print('Ans:', aw, '\n')              
            except EOFError:
                break
    
qm = '''QUESTION BANK MENU

1. Create Question
2. Edit Question
3. Delete Question
4. List Question
5. Return to Main Menu

Enter Choice(1-5): '''

def question_menu():
    while True:
        op = inpany(qm, '')
        print()       
        if op == '1':
            create_qbank()
        elif op == '2':
            edit_Question()
        elif op == '3':
            delete_question()
        elif op == '4':
            list_question()
        elif op == '5':
            break
        else:
            print('Invalid Choice')
        print('\n')
            
    

