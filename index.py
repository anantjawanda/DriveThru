from flask import Flask, render_template, send_from_directory, jsonify, request
import pandas as pd
import requests
import qrcode

app = Flask(__name__)

@app.route('/')
def test():
    df = pd.read_excel("User_Data.xlsx")
    usr = list(df["Users"])
    qr = list(df["QR"])
    USER = "Username"  # Will deal with this later
    # if USER in usr:
        # return qr[usr.index(USER)]
    return render_template('home.html')

@app.route('/login.html')
def login():
    # df = pd.read_excel("User_Data.xlsx")
    # usr = list(df["Users"])
    # USER = "New User"
    # if not USER in usr:
    #     usrs = usr + USER
    #     df = pd.DataFrame(usrs, columns=["Users"])
    #     df.to_excel("User_Data.xlsx", index=False)
    return render_template('login.html')

@app.route('/signup.html')
def signup():
    return render_template('signup.html')

@app.route('/user_info/<string:value1>/<string:value2>')
def qr_code(value1, value2):
    pass

if __name__ == '__main__':
    img = qrcode.make('Some data here')
    print(type(img))


    # r = requests.get("http(s)://api.qrserver.com/v1/create-qr-code/?data=[Example]&size=[100]x[100]")
    # r = requests.get(url = URL)
    app.run(host='127.0.0.1', port=8080, debug=True)


