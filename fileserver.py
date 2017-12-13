import web
import shelve
import os
import sys

urls = (
    '/(.*)/', 'redirect',
    '/(.*)', 'mainclass'
)

class FilServer(web.application):
    def run(self, port=8080, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))

class mainclass:
    def GET(self,filename):
        s = shelve.open('dir_db')
        try:
            f_dir = s[filename]
        finally:
            s.close()
        fullpath = os.path.join(f_dir[0], filename)
        f = open(fullpath,"r")
        return f.read()
        return fullpath
class redirect:
    def GET(self, path):
        web.seeother('/' + path)

if __name__ == "__main__":
    port1 = int(sys.argv[1])
    app = FilServer(urls, globals())
    app.run(port=port1)
