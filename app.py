import streamlit as st 
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))

st.title("Image to Text Application")
user_input=st.text_input("Input Prompt")

uploaded_file=st.file_uploader("Upload the image...",type = ['jpg','jpeg','png'])

# Display the image on the page
from PIL import Image
img=""
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img,caption="Upload_Image",use_column_width=True)


# Function for evaluating the image and annotating

def gemini_response(user_input,img):
    model = genai.GenerativeModel("gemini-1.5-flash") # we are not using gemini-pro bc it is useful in text
    if user_input!="":
        response= model.generate_content([user_input,img])
    else:
        response = model.generate_content(img)
    return response.text

# Creating the button
submit = st.button("Submit")

if submit:
    response = gemini_response(user_input=user_input,img=img)
    st.subheader("The Response is:")
    st.write(response)