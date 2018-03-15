# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
import tornado.websocket
# Generic imports
import web_cam as webcam
import time
import cv2
import threading
#import multiprocessing
import operator
#import bjsdrone

#pippo = bjsdrone.SumoController()
green_light = False

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def __init__(self, args, kwargs):
        tornado.websocket.WebSocketHandler.__init__(self, args, kwargs)
        print("ClientWebSocketHandler.init")
        pippo = webcam.Camera(0)
        green_light = True
        self.my_thread = threading.Thread(target = self.run)
        self.my_thread.start()

    def open(self):
        green_light = True
        print("WebSocket opened")

    def run(self):
    #def on_message(self, message):
        while green_light:
            try:
                self.write_message({
                    'frame': pippo.get_frame(),
                })
            except Exception,e :
                print "Errore: %s" % e
        time.sleep(1)

    def on_close(self):
        green_light = False
        pippo.close()
        print("WebSocket closed")

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

def launch():
    """ Run all the things.
    """
    #pippo.launch()
    settings = {
        'template_path': 'templates',
        'static_path': 'static'
    }
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': 'static'}),
        (r'/ws', WebSocketHandler),
        ], **settings)
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
    #tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
