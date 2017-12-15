import web
import shelve
import os
import sys
import customport

urls = (
    '/(.*)', 'mainclass'
)

class mainclass:
    def GET(self,filename):
        print("reached direct")
        s = shelve.open('dir_db')
        print("entered directory server")
        try:
            (f_dir,f_port) = s[filename]
        finally:
            s.close()
        fullpath = os.path.join(f_dir, filename)
        fullpath = str(f_port)+fullpath
        return fullpath


if __name__ == "__main__":
    app = customport.customport(urls, globals())
    app.run(port=8186)
