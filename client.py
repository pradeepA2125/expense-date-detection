import requests
import base64

# defining the api-endpoint
API_ENDPOINT = " http://127.0.0.1:5000/extract_date"

img_path = 'C:/Users/Pradeep kumar/desktop/receipts/0c60aa84.jpeg'
with open(img_path,'rb') as image:
    #print(image.read())
    base = base64.b64encode(image.read())

data = {'base_64_image_content' : base}

r = requests.post(url = API_ENDPOINT, data = data)
print(r.text)
