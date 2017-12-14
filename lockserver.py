import web
import shelve
import os
import sys
import customport

urls = (
    '/(.*)/', 'redirect',
    '/(.*)', 'mainclass'
)

class mainclass:
    def GET(self, filename):
        if not filename:
            msg = 'No input...'
            return msg
        else:
            if filename == '*':
                try:
                    lockdb = shelve.open("lock_db.dat")
                    filekeys = list()
                    for name in lockdb.keys():
                        if lockdb[name] == 'U':
                            filekeys.append(name)
                    filekeys.sort()
                    availfiles = ""
                    for i in range(len(filekeys)):
                        availfiles = availfiles + str((i+1)) + "   " + str(filekeys[i] + "\n")
                finally:
                    lockdb.close()
                return availfiles
            else:
                try:
                    lockdb = shelve.open("lock_db.dat")
                    lock = lockdb[filename]
                    if "U" in lock:
                        lockdb[filename] = 'L'
                        return 'Locked the file...'
                    else:
                        return 'The file is in use...Access denied'
                except KeyError as err:
                    error = "Cannot find the mentioned file"
                    return error
                finally:
                    lockdb.close()

if __name__ == "__main__":
    app = customport.customport(urls, globals())
    app.run(port=8188)
