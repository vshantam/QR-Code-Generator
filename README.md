# QR-Code-Generator
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/6bf84981ad0d4b24b4befe7243cb8a33)](https://www.codacy.com/app/vshantam/QR-Code-Generator?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=vshantam/QR-Code-Generator&amp;utm_campaign=Badge_Grade)

This application will create the QR code for the required textual content or url links using python.

This application was built on linux based platform

# Requirements:
    1.zbar
      To install zbar use the following command:
      apt-get install libzbar-dev
    2.pyqrcode
    3.qrcode
    4.pypng
    5.pillow
    6.matplotlib
    
# Installation:
<br>To install the above dependencies use the <b>pip</b> command</br>
eg:

    pip install pillow #for PIL
    
 Or you can run the command bellow:
                  
     pip install -r spec.txt 
     
This will install all the required packages into your system.

# How to run:
follow the steps:

    1.After cloning change the directory to QR-Code-Generator using bellow command:
      
        cd QR-Code-Generator
    2. python applic.py
    3. After running the above command you will be asked to enter the text to be encoded.Enter the text and you are good to go.
    
Your application should run perfectly.
Make sure your linux system is updated recently or you may face certain error.
Try to run the following command before you run the applcation #Good Practice.

    sudo apt-get update && apt-get dist-upgrade
    
# Output
If everything went perfectly as it suppose to the you will see the output like bellow named secret.png and it will be saved in the same working directory.

![alt_tag](secret.png)

The above Qr code is been encoded with the text "Hello zameer!" and if you scan it, you should probably get the same.


    
    
