import streamlit as st
import requests
import base64
import json
def get_prediction(image_data):
  url = 'https://askai.aiclub.world/39a4f3a3-e637-4981-a88c-b2597ab12be0'
  r = requests.post(url, data=image_data)
  response = r.json()['predicted_label']
  print(response)
  return response
def processFile(f):
  print("Got file upload")
  bytesData=f.getvalue()
  st.image(f)
  payload = base64.b64encode(bytesData)
  response = get_prediction(payload)
  print("Response is:",response)
  st.title("AI says:"+response)
st.title("Cats and Dogs")
uploadedFile=st.file_uploader("Choose file")
if uploadedFile is not None:
  processFile(uploadedFile)
