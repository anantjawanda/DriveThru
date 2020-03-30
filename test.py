import qrcode
DOMAIN = "http://127.0.0.1:8080/"
user_information = "random/random"
img = qrcode.make('Some data here')
print(type(img))
img.save("qrcode.jpg")

# # import requests
# requests.get(https://api.qrserver.com/v1/create-qr-code/?data=[URL-encoded-text]&size=[pixels]x[pixels])
# if response.status_code == 200:
#     print('Success!')
# elif response.status_code == 404:
#     print('Not Found.')
