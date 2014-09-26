import tornado.ioloop
import tornado.web
from tornado import template

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        loader = tornado.template.Loader('views/')
        self.write(loader.load("index.html").generate(user="liujie"))
        # self.render('views/index.html')

application = tornado.web.Application([
    (r"/", MainHandler),
], debug=True)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()