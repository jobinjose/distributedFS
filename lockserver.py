import web
import shelve
import os
import sys
import customport

urls = (
    '/unlock/(.*)', 'mainclassUnlock',
    '/(.*)', 'mainclass'

)
class mainclassUnlock:
    def GET(self, filename):
        print("Entered unlock")
        print("filename:",filename)
        try:
            lockdb = shelve.open('lock_db')
            print(filename)
            lockdb[filename] = 'U'
            return 'The file is unlocked'
        except KeyError as err:
            error = "Cannot find the mentioned file"
            return error
        finally:
            lockdb.close()
class mainclass:
    def GET(self, filename):
        print("Entered lock server")
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
