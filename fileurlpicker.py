import web

urls = (
  '/(.*)', 'example'
)

class example:
    def GET(self,filename):
        return "Hello," + str(filename)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
