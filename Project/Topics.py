import datetime
import pickle
from Mymodules import *
import datetime
from QuestionBank import *

tn = 0
def inputtn(tn):
    co = datetime.datetime.now().strftime('%x')
    print('Created On: ', co)
    print()
    cb = inpany('Created by: ', '')
    print()
    tp = inpany('Topic     : ', '')
    print()
    return [tn, co, cb, tp, 0]

def printtn(rc):
    tn, co, cb, tp, nq = rc               
    print('Paper no.   :', tn)
    print('Created on  :', co)
    print('Created by  :', cb)
    print('Topic       :', tp)
    print('No.Questions:', nq)
    print('\n')

def find_next_tn():
    tn = 0
    with open('topic.dat', 'ab+') as fl:
        fl.seek(0)
        while True:
            try:
                tn, co, cb, tp, nq = pickle.load(fl)
            except EOFError:
                break
    return tn+1

def searchtn(op = ''):
    global tn
    tn = inpany('Topic No.: ', 0)
    print()
    flag = False
    with open('topic.dat', 'ab+') as fl:
        fl.seek(0)
        while True:
            try:
                rc = pickle.load(fl)
                if tn == rc[0]:
                    flag = True
                    return rc
            except EOFError:
                break
    if not flag and op == '':
        print('Invalid Test Paper Number !\n')
    return False

def update_qpaper_nq(no):
    recs = []
    with open('topic.dat', 'rb') as fl:
        while True:
            try:
                tn, co, cb, tp, nq = pickle.load(fl)
                if tn == no:
                    nq += 1
                recs.append([tn, co, cb, tp, nq])
            except EOFError:
                break
    with open('topic.dat', 'wb') as fl:
        for rec in recs:
            pickle.dump(rec, fl)
    
def create_topic():
    rc = searchtn('a')
    if not rc:
        rc = inputtn(tn)
        print()
        if input('Save(y/n): ').lower() == 'y':
            with open('topic.dat', 'ab') as fl:
                pickle.dump(rc, fl)
    else:
        printtn(rc)
        print('Details Already Entered !')
                
def updatefile(rc, rs):
    with open('topic.dat', 'wb') as fl:
        for rc in rs: 
            pickle.dump(rc, fl)
            
def edit_topic():
    print('EDIT TOPIC\n')
    rc = searchtn()
    print()
    if rc:
        with open('topic.dat', 'rb') as fl:
            rs = []
            while True:
                try:
                    rc = pickle.load(fl)                    
                    if tn == rc[0]:
                        printtn(rc)
                        print('Edit Info...')
                        tt, co, cb, tp, nq = rc
                        cb = inpany('Created by  :', '')
                        tp = inpany('Topic       :', '')
                        rc = [tt, co, cb, tp, nq]
                    rs.append(rc)                         
                except EOFError:
                    break
                    
        print()
        if input('Confirm Edit(y/n): ').lower() == 'y':
            updatefile(rc, rs)
            print('Edited !')
        else:
            print('Editing Cancelled !')            

def delete_topic():
    print('REMOVE TOPIC\n')

    rc = searchtn()
    if rc:
        with open('topic.dat', 'rb') as fl:
            rs = []
            while True:
                try:
                    rc = pickle.load(fl)
                    tt, co, cb, tp, nq = rc
                    if tn == rc[0]:
                        print('Current Info...')
                        printtn(rc)
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

def list_topic():
    with open('topic.dat', 'ab+') as fl:
        fl.seek(0)
        c = 0
        while True:
            try:
                tn, co, cb, tp, nq = pickle.load(fl)
                if c == 0:
                    print('%-10s %-15s %-20s %-20s %-10s' %
                          ('Paper no.', 'Created on', 'Created by', 'Topic', 'No.Questions'))
                print('%-10s %-15s %-20s %-20s %-10s' %
                      (tn, co, cb, tp, nq))
                c += 1                
            except EOFError:
                break

to = ''' TOPICS

1. Create Topic
2. Edit Topic
3. Delete Topic
4. List Topic
5. Return to Main Menu

Enter Choice(1-5): '''

def topics_menu():
    while True:
        op = inpany(to, '')
        print()
        if op == '1':
            create_topic()
        elif op == '2':
            edit_topic()
        elif op == '3':
            delete_topic()
        elif op == '4':
            list_topic()
        elif op == '5':
            break
        else:
            print('Invalid Choice')
        print('\n')
        
