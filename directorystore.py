import shelve
import os
import sys

choice = sys.argv[1]
print(choice + "....")

if (choice == 'write'):
    s = shelve.open('dir_db')
    lockdb = shelve.open('lock_db')
    try:
        while (1):
            f_name = input("Filename? ")
            if (f_name == 'KILL'):
                break
            f_path = input("Filepath? ")
            f_port = input("Fileport? ")
            s[f_name] = (f_path,f_port)
            lockdb[f_name] = "U"
    finally:
        s.close()
        lockdb.close()

elif (choice == 'display'):
    s = shelve.open('dir_db')
    try:
        f_name = input("Filename? ")
        existing = s[f_name]
    finally:
        s.close()
    print(existing)

elif (choice == 'displayall'):
    lockdb = shelve.open('dir_db')
    try:
        for key in lockdb:
            print(key, lockdb[key])
    finally:
        lockdb.close()
