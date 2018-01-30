from lib import *
#setting scale_factor
scale_factor=6 #or choose as you like
class qrgenerator(object):
	
	@classmethod
	def generate(self):
		
		qr=pyqrcode.create(raw_input("Please Enter the requred text for creation of the QR Code:\n"),encoding='utf-8',error='L',version=27)
		#or using qrcode : qrcode.make(contents)
		#saving image
		result = qr.png(os.getcwd()+str('/secret.png'),scale=scale_factor)
		
		return result
		
	@classmethod
	def openbarcode(self):
		
		img=cv2.imread(os.getcwd()+str('/secret.png'),cv2.IMREAD_COLOR)
		img=plt.imshow(img,interpolation='bicubic')
		plt.xticks(())
		plt.yticks(())
		showimg = plt.show()
		
		return showimg
		
	@classmethod
	def main(self):
		
		obj=qrgenerator()
		obj.generate()
		
		return obj.openbarcode()
		
if __name__=='__main__':
	
	obj1 = qrgenerator()
	obj1.main()
	print("Quitting Application...")
