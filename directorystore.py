import shelve
import os
import sys

choice = sys.argv[1]
print(choice + "....")

if (choice == 'write'):
    s = shelve.open('dir_db')
    try:
        while (1):
            f_name = input("Filename? ")
            if (f_name == 'KILL'):
                break
            f_path = input("Filepath? ")
            s[f_name] = f_path
    finally:
        s.close()

elif (choice == 'display'):
    s = shelve.open('dir_db')
    try:
        f_name = input("Filename? ")
        existing = s[f_name]
    finally:
        s.close()
    print(existing)
