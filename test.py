from flask import Flask, render_template, json, request
from firebase import firebase

app = Flask(__name__)
firebase = firebase.FirebaseApplication('https://servx-f0d70.firebaseio.com/', None)


#mysql.init_app(app)
@app.route("/signuppage")
def SignUp():




    return render_template('signup.html')

@app.route("/homepage", methods=['POST'])
def HomePage():
    #r="HALO"
    #r= request.form.get('user',None)
    #r= request.form['pass']

    a=request.form.get('user', None)
    b=request.form.get('pass',None)
    unsuccessful = 'Mobile number or password is invalid.'


    r=firebase.get('/',None )
    # return "<h1>%s</h1>"%str(r)

    numbers=[]

    for numb in r['User']:
        numbers.append(numb)

    # r1=firebase.get("User/03230494883",None)

    if a in numbers:
        c=str(r['User'][a]["Password"])
        if(c==b):
            return render_template('btn.html')
        else:
            return render_template('login.html', us=unsuccessful)


    return render_template('login.html', us=unsuccessful)


    # return "<h1>%s</h1>"%str(r[a]["Password"])
    

@app.route("/homepage1", methods=['POST'])
def HomePage1():

    #r= request.form.get('user',None)
    # r= request.form['pass']


    err1='Incorrect Mobile Number.'
    err2='Please type your password again.'
    err3='Password length too short.'
    err4='Mobile number must consist of digits.'
    err5='Name must consist of alphabets.'
    err7='Enter your credentials to login now.'
    err6='Invalid email address was entered.'

    a=request.form.get('name', None)
    b=request.form.get('email',None)
    c=request.form.get('mobile', None)
    d=request.form.get('pass',None)
    e=request.form.get('confirmpass', None)


    # if(a.isalpha()==False):
    #     return render_template('signup.html', us=err5)

    if('1' in a) or ('2' in a) or ('3' in a) or ('4' in a) or ('5' in a) or ('6' in a) or ('7' in a) or ('8' in a) or ('9' in a) or ('0' in a ):
        return render_template('signup.html', us=err5)


    if len(c)!=11:
        return render_template('signup.html', us=err1)

    if ('@' not in b) or ('.' not in b):
        return render_template('signup.html', us=err6)

    if(d!=e):
        return render_template('signup.html', us=err2)

    if(d==e and len(d)<8):
        return render_template('signup.html', us=err3)

    if(c.isdigit()==False):
        return render_template('signup.html', us=err4)

    # data = {"User": {c: {'Name': a, 'Password': d, 'email': b}}}
    # sent = json.dumps(data)
    # # result = firebase.post("/User", c)
    # result = firebase.put("/", data)

    result = firebase.put("User",c,{'Name': a, 'Password': d, 'email': b})




    return render_template('login.html', us=err7)

@app.route("/")
def index():

    return render_template('login.html')


if __name__ == "__main__":
    #main()
    app.run(debug=True)