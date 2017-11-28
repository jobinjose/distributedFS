import web
import os

urls = (
    '/(.*)/', 'redirect',
    '/(.*)', 'example'
)

class example:
    def GET(self,filename):
        return os.path.getsize(filename)
class redirect:
    def GET(self, path):
        web.seeother('/' + path)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
