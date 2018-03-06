# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
import tornado.websocket
# Generic imports
import base64
import web_cam as webcam
import time
import cv2
import multiprocessing
import operator
#import bjsdrone

#pippo = bjsdrone.SumoController()
pippo = webcam.Camera(0)
green_light = True

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        green_light = True
        print("WebSocket opened")
    #def on_message(self, message):
        while green_light:
            try:
                self.write_message({
                    'frame': pippo.get_frame(),
                })
            except Exception,e :
                print "Errore: %s" % e
        time.sleep(2)

    def on_close(self):
        green_light = False
        print("WebSocket closed")

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

def main():
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
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()


