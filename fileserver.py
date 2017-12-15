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
        f = open(filename,"r")
        return f.read()
        #return fullpath

    def POST(self,filename):
        f = open(filename,"w")
        f.write(web.data().decode())
        return "Write success"

class redirect:
    def GET(self, path):
        web.seeother('/' + path)

if __name__ == "__main__":
    port1 = int(sys.argv[1])
    app = customport.customport(urls, globals())
    app.run(port=port1)
