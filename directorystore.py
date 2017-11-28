import shelve
import os
import sys

choice = sys.argv[1]
print(choice + "....")

if (choice == 'write'):
    s = shelve.open('dir_db')
    try:
        s['key1'] = { 'int': 10, 'float':9.5, 'string':'Sample data' }
    finally:
        s.close()

elif (choice == 'display'):
    s = shelve.open('dir_db')
    try:
        existing = s['key1']
    finally:
        s.close()
    print(existing)
