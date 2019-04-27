from flask import Flask, render_template, json, request
from firebase import firebase

app = Flask(__name__)
firebase1 = firebase.FirebaseApplication('https://servx-f0d70.firebaseio.com/', None)

def make_list(problematic_values):
    #known values is already a tuple. problematic values is a list.
    list_of_tuples=[]

    for x in problematic_values:
        list_of_tuples.append(x)

    return list_of_tuples



@app.route("/requests")
def Requestpage():

    r=firebase1.get("requests",None)
    numbers=[]

    for numb in r:
        numbers.append(numb)

    length_numbers=len(numbers)

    a=0
    date=[]
    for numb in range(len(numbers)):
        b=r[numbers[a]][0]['date']
        a=a+1
        date.append(b)


    a=0
    status=[]
    for numb in range(len(numbers)):
        b=r[numbers[a]][0]['status']
        a=a+1
        status.append(b)


    a=0
    time=[]
    for numb in range(len(numbers)):
        b=r[numbers[a]][0]['time']
        a=a+1
        time.append(b)



    return render_template('requests.html', numbers=numbers, time=time,length_numbers=2,date=date)

@app.route("/requests1", methods=['POST'])
def Requestpage1():

    decision=request.form.get('dec', None)
    # firebase.put('servx-f0d70/requests/0/090078601','status',decision)  
    # fire = firebase.FirebaseApplication('https://servx-f0d70.firebaseio.com/servx-f0d70/requests/0/090078601/status', None)
    # fire.put(fire,decision) 
    # return "<h1>%s</h1>"%decision
    # firebase.FirebaseApplication('https://servx-f0d70.firebaseio.com/servx-f0d70/requests/0', None).put('/090078601','status',decision)
    # return "<h1>%s</h1>"%decision
    firebase1.put('requests/03215468623/0','status',decision)
    return "<h1>%s</h1>"%decision
    


@app.route("/homepage", methods=['POST'])
def HomePage():
    #r="HALO"
    #r= request.form.get('user',None)
    #r= request.form['pass']

    a=request.form.get('user', None)
    b=request.form.get('pass',None)
    unsuccessful = 'Mobile number or password is invalid.'


    r=firebase1.get('/',None )
    # return "<h1>%s</h1>"%str(r)

    numbers=[]

    for numb in r['User']:
        numbers.append(numb)

    # r1=firebase.get("User/03230494883",None)

    if a in numbers:
        c=str(r['User'][a]["Password"])
        if(c==b):
            return render_template('home.html')
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


    if('1' in a) or ('2' in a) or ('3' in a) or ('4' in a) or ('5' in a) or ('6' in a) or ('7' in a) or ('8' in a) or ('9' in a) or ('0' in a ):
        return render_template('signup.html', us=err5)


    if len(c)!=11:
        return render_template('signup.html', us=err1)

    if ('@' not in b) or ('.' not in b):
        return render_template('signup.html', us=err6)

    if(c.isdigit()==False):
        return render_template('signup.html', us=err4)

    if(d!=e):
        return render_template('signup.html', us=err2)

    if(d==e and len(d)<8):
        return render_template('signup.html', us=err3)



    # data = {"User": {c: {'Name': a, 'Password': d, 'email': b}}}
    # sent = json.dumps(data)
    # # result = firebase.post("/User", c)
    # result = firebase.put("/", data)

    result = firebase1.put("User",c,{'Name': a, 'Password': d, 'email': b})
    return render_template('login.html', us=err7)


@app.route("/")
def index():

    return render_template('login.html')


if __name__ == "__main__":
    #main()
    app.run(debug=True)