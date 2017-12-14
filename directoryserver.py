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
    def GET(self,filename):
        s = shelve.open('dir_db')
        try:
            f_dir = s[filename]
        finally:
            s.close()
        fullpath = os.path.join(f_dir, filename)
        return fullpath

class redirect:
    def GET(self, path):
        web.seeother('/' + path)

if __name__ == "__main__":
    app = customport.customport(urls, globals())
    app.run(port=8888)
