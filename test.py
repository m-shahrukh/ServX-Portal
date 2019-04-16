from flask import Flask, render_template, json, request

app = Flask(__name__)

#mysql.init_app(app)
@app.route("/signuppage")
def SignUp():
    return render_template('signup.html')

@app.route("/homepage", methods=['POST'])
def HomePage():
    #r="HALO"
    #r= request.form.get('user',None)
    r= request.form['pass']
    return "<h1>%s</h1>"%r
    # return render_template('signup.html')

@app.route("/homepage1", methods=['POST'])
def HomePage1():
    #r="HALO"
    #r= request.form.get('user',None)
    # r= request.form['pass']
    # return "<h1> fffff </h1>"
    return render_template('home.html')

@app.route("/")
def index():
    return render_template('login.html')


if __name__ == "__main__":
    #main()
    app.run(debug=True)