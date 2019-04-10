from flask import Flask, render_template, json, request

app = Flask(__name__)

#mysql.init_app(app)
@app.route("/signuppage")
def SignUp():
    return "<h1> SIGN-UP page</h1>"

@app.route("/homepage", methods=['POST'])
def HomePage():
    #r="HALO"
    #r= request.form.get('user',None)
    r= request.form['pass']
    return "<h1>%s</h1>"%r

@app.route("/")
def index():
    return render_template('Sign-Up.html')


if __name__ == "__main__":
    #main()
    app.run(debug=True)

