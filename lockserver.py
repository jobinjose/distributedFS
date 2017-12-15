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
                    lockdb = shelve.open('lock_db')
                    filekeys = list()
                    for name in lockdb.keys():
                        if lockdb[name] == 'U':
                            filekeys.append(name)
                    filekeys.sort()
                    availfiles = ""
                    for i in range(len(filekeys)):
                        availfiles = availfiles + str((i+1)) + "   " + str(filekeys[i] + "\n")
                except:
                    print("oops")
                finally:
                    lockdb.close()
                return availfiles
            else:
                try:
                    lockdb = shelve.open('lock_db')
                    if lockdb[filename] == 'U':
                        return 'The file is not locked...'
                    else:
                        return 'The file is in use...Access denied'
                except KeyError as err:
                    error = "Cannot find the mentioned file"
                    return error
                finally:
                    lockdb.close()
    def POST(self, filename):
        if not filename:
            msg = 'No input...'
            return msg
        else:
            try:
                lockdb = shelve.open('lock_db')
                if lockdb[filename] == 'U':
                    lockdb[filename] = 'L'
                    return str(filename) + ' locked...'
                else:
                    return 'The file ' + str(filename) +' is in use...Access denied'
            except KeyError as err:
                error = "Cannot find the mentioned file"
                return error
            finally:
                lockdb.close()

if __name__ == "__main__":
    app = customport.customport(urls, globals())
    app.run(port=8188)
