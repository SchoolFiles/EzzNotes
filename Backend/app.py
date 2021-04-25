from flask import Flask, request, render_template, jsonify
#from flask_core import CORS
import hashlib


app = Flask(__name__)
#CORS(app)

# --------------------------------------------------- Landing Page ----------------------------------------------------
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return "Landing Page"
    

# --------------------------------------------------- Login Page ----------------------------------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = hashlib.md5(request.form.get('password'))

        login = access_site(username, email, password)

    








if __name__ == '__main__':
    app.run(debug=True)