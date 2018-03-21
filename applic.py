from lib import *

#setting scale_factor
scale_factor=6 #or choose as you like

class qrgenerator(object):

	#creating the classmehod and defining generate function
	@classmethod
	def generate(self):

		#Creatng encoded qrcode with utf-8 encoding
		qr=pyqrcode.create(raw_input("Please Enter the requred text for creation of the QR Code:\n"),encoding='utf-8',error='L',version=27)
		#or using qrcode : qrcode.make(contents)
		#saving image
		result = qr.png(os.getcwd()+str('/secret.png'),scale=scale_factor)
		
		#returning the file pointer
		return result
	
	#defining classmethod and opening  saved barcode image
	@classmethod
	def openbarcode(self):
		
		#reading image with opencv
		img=cv2.imread(os.getcwd()+str('/secret.png'),cv2.IMREAD_COLOR)
		#plotting the pixels using matplotlib.pyplot
		img=plt.imshow(img,interpolation='bicubic')
		#removing x-axial coordinates
		plt.xticks(())
		#removing y-axial coordinates
		plt.yticks(())
		#saving image to temp variable
		showimg = plt.show()
		
		#returning the file pointer
		return showimg
	
	#creating classmethod and defining decoding function
	#@classmethod#remove this comment
	#def decode(self,path):#remove this comment

		#provide the path of existing qrcode image
		#creating the object
		#qr = qrtools.QR()#remove this comment
		#extracting the result
		#res = qr.decode(path)#remove this comment

		#returning the result
		#return res#remove this comment

	#creating clasmethod and creating the main function	
	@classmethod
	def main(self):

		#creating the object
		obj=qrgenerator()
		#calling the generate function using object
		obj.generate()
		
		#returning
		return obj.openbarcode()
	
#setting main varable to this program
if __name__=='__main__':
	
	#creating objects
	obj1 = qrgenerator()
	
	#exceptional handeling
	try:
		#Exception tracing
		obj1.main()

	except Exception as e:
		#response of error caught	
		print("Error Caught :{}".format(str(e)))

	print("Want to use decoding functon:{}".format("Yes/No"))
	ans = raw_input().strip().lower()[0]
	
	if ans == "y":
		path = "/secret.png"
		#res =  obj.decode(path)#remove comment
		#print("The decoded msg is :{}".format(res.data))#remove comment
		pass#comment this section

	else:

		#quitting the application
		print("Quitting Application...")

