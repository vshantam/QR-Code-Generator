from lib import *

#setting scale_factor

scale_factor=6 #or choose as you like

class qrgenerator:
	
	def generate(self):
		qr=pyqrcode.create(raw_input("Please Enter the requred text for creation of the QR Code:\n"),encoding='utf-8',error='L',version=27)
		
		#or using qrcode : qrcode.make(contents)
		
		#saving image
		qr.png(os.getcwd()+str('/secret.png'),scale=scale_factor)

