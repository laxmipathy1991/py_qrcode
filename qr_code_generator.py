import streamlit as st
from streamlit_multi_menu import streamlit_multi_menu
import qrcode
from PIL import Image
import time

st.title("QR-Code Generator")
column1,column2=st.columns(2)
check1=None
check2=None
image=None
check3=False
col3,col4=st.columns(2)


name=st.text_input('Name for Your QR')
with column1:
    check1=st.checkbox('Generate QR for Image')
with column2:
    check2=st.checkbox('Generate QR for Non Image')
with col3:
    check3=st.checkbox('You need background??')
if check1==True:
    image_data=st.file_uploader('Give your Image to QR',['png','jpg'])
if check3==True:
        image=st.file_uploader('Give your logo',['png','jpg'])

if check2==True:    
    data=st.text_input("Give your content that need to be in a QR")
button=st.button('Generate QR')


class QRCODE_generator():
    def __init__(self,data,name,background_color='black'):
        self.data=data
        self.image=None
        self.name=name
        self.background_color=background_color
    def with_logo_generate(self,image):
        self.image=image
        qr=qrcode.QRCode(version=3,box_size=10,border=5)
        passed_data=self.data
        qr.add_data(passed_data)
        qr.make(fit=True)

        if self.image:
            try:
                img=qr.make_image(fill_color=self.background_color,back_color='white')
                logo=Image.open(self.image)
                logo=logo.resize((50,50))
                img_w,img_h=img.size 
                logo_w,logo_h=logo.size 
                pos=((img_w - logo_w) // 2,(img_h - logo_h) //2)
                img.paste(logo,pos)
                img.save(f"storage/{self.name}_with_logo.png")
            except:
                pass
    def generate(self):
        qr=qrcode.QRCode(version=3,box_size=10,border=5)
        passed_data=self.data
        qr.add_data(passed_data)
        qr.make(fit=True)
        img=qr.make_image(fill_color=self.background_color,back_color="white")
        img.save(f"storage/{self.name}.png")


if button==True:
    if check1==True and check3==False:
        image_data1=Image.open(image_data)

        qr=QRCODE_generator(image_data1,name)
        with st.spinner('Wait for it...'):
            time.sleep(5)
        st.success("Done!")
        img=qr.generate()

        st.image(f"storage/{name}.png")
    if check3==True and check1==True:
        image_data1=Image.open(image_data)
        qr=QRCODE_generator(image_data1,name)
          
        with st.spinner('Wait for it...'):
            time.sleep(5)
        st.success("Done!")
        qr.with_logo_generate(image)
        st.image(f"storage/{name}_with_logo.png")

    if check3==True and check2==True:
        qr=QRCODE_generator(data,name)
          
        with st.spinner('Wait for it...'):
            time.sleep(5)
        st.success("Done!")
        qr.with_logo_generate(image)
        st.image(f"storage/{name}_with_logo.png")
    if check2==True and check3==False:
        qr=QRCODE_generator(data,name)
        with st.spinner('Wait for it...'):
            time.sleep(5)
        st.success("Done!")
        qr.generate()
        st.image(f'storage/{name}.png')




        



    







    