''' Test opencv features by usb webcam Logitech C270 '''

#import collections
import cv2
import base64

class Camera():
	cap = None
	#_latest_pic = None
	device_number = 0

	def __init__(self, camera_number):
		self.cap = cv2.VideoCapture(camera_number)
		#self._latest_pic = collections.deque(maxlen=20)
		self.device_number = camera_number

	def get_frame(self):
		if not(self.cap.isOpened()):
			self.cap.open(self.device_number)
		ret, frame = self.cap.read()
		if ret :
			retval, buffer = cv2.imencode('.jpg', frame)
			return base64.b64encode(buffer)
			#image = cv2.imdecode(frame,cv2.CV_LOAD_IMAGE_COLOR)
			
			#self._latest_pic.append(base64.b64encode(image))
		else:
			print "No image from camera"
		print "Exiting from web_cam"
		self.cap.release()
