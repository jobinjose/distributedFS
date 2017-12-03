import shelve
import os
import sys

choice = sys.argv[1]
print(choice + "....")

if (choice == 'write'):
    lockdb = shelve.open('lock_db')
    try:
        while (1):
            f_name = input("Filename? ")
            if (f_name == 'KILL'):
                break
            lockstatus = input("lock status? (L/U)")
            if(lockstatus in ("L","l","U","u")):
                lockdb[f_name] = lockstatus.upper()
    finally:
        lockdb.close()

elif (choice == 'display'):
    lockdb = shelve.open('lock_db')
    try:
        f_name = input("Filename? ")
        existing = lockdb[f_name]
    finally:
        lockdb.close()
    print(existing)

elif (choice == 'displayall'):
    lockdb = shelve.open('lock_db')
    try:
        klist = list(lockdb.keys())
        print(klist)
    finally:
        lockdb.close()
