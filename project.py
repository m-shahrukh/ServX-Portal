from flask import Flask, render_template, json, request
from firebase import firebase
import copy

app = Flask(__name__)
firebase1 = firebase.FirebaseApplication('https://servx-f0d70.firebaseio.com/', None)

global length_requests

@app.route("/signuppage")
def signup():
	return render_template('signup.html')

@app.route("/requests")
def Requestpage():

    # r=firebase1.get("requests",None)
    # numbers=[]

    # for numb in r:
    #     numbers.append(numb)


    # length_numbers=len(numbers)

    # length_requests=length_numbers


    # mobile_keys=firebase1.get('/requests',None).keys()

    # for i in range(len(mobile_keys)):
    # 	j=firebase1.get('/requests/'+ str(numbers[i]),None).keys()






    # a=0
    # date=[]
    # for numb in range(len(numbers)):
    #     b=r[numbers[a]][0]['date']
    #     a=a+1
    #     date.append(b)


    # a=0
    # status=[]
    # for numb in range(len(numbers)):
    #     b=r[numbers[a]][0]['status']
    #     a=a+1
    #     status.append(b)


    # a=0
    # time=[]
    # for numb in range(len(numbers)):
    #     b=r[numbers[a]][0]['time']
    #     a=a+1
    #     time.append(b)





    r=firebase1.get("requests",None)
    r1=firebase1.get("requestID",None)
    r1=int(r1)
    numbers=[]

    # for numb in r:
    #     numbers.append(numb)



    random=[]
    c=1
    requests=firebase1.get('requests',None)
    mobile_keys=requests.keys()
    keys_person= requests[mobile_keys[0]].keys()


    date=[]
    time=[]
    oil=[]
    wash=[]
    location=[]

    for i in range(len(mobile_keys)):

    	keys_person= requests[mobile_keys[i]].keys()
    	for j in keys_person:
    		a=requests[mobile_keys[i]][j]['date']
    		numbers.append(mobile_keys[i])
    		date.append(a)

    for i in range(len(mobile_keys)):

    	keys_person= requests[mobile_keys[i]].keys()
    	for j in keys_person:
    		a=requests[mobile_keys[i]][j]['time']
    		time.append(a)

    length_numbers=len(date)

    for i in range(len(mobile_keys)):

    	keys_person= requests[mobile_keys[i]].keys()
    	for j in keys_person:
    		a=requests[mobile_keys[i]][j]['oil']
    		oil.append(a)


    for i in range(len(mobile_keys)):

    	keys_person= requests[mobile_keys[i]].keys()
    	for j in keys_person:
    		a=requests[mobile_keys[i]][j]['wash']
    		wash.append(a)

    for i in range(len(mobile_keys)):

    	keys_person= requests[mobile_keys[i]].keys()
    	for j in keys_person:
    		a=requests[mobile_keys[i]][j]['location']
    		location.append(a)




    return render_template('requests.html', numbers=numbers, time=time,length_numbers=length_numbers,date=date,oil=oil,wash=wash,location=location)

@app.route("/requests1", methods=['POST'])
def Requestpage1():

    # decision=request.form.get('dec', None)

    # firebase1.put('requests/03215468623/0','status',decision)
    # return "<h1>%s</h1>"%decision

    numbers=[]

    requests=firebase1.get('requests',None)
    mobile_keys=requests.keys()
    # keys_person= requests[mobile_keys[0]].keys()

    for i in range(len(mobile_keys)):

    	keys_person= requests[mobile_keys[i]].keys()
    	for j in keys_person:
    		numbers.append(mobile_keys[i])



    decision=[]
    for i in range(len(numbers)):

      decision1=request.form.get('dec'+str(i),None)
      decision.append(decision1)

    # respond=[]
    # waiting=[]
    # numbers_copy=copy.deepcopy(numbers)
    # for i in range(len(numbers)):

    # 	if decision[i]!=None:
    # 		firebase1.put('requests/'+str(numbers[i])+'/0/','status',decision[i])
    # 		numbers_copy.remove(numbers[i])

    # 	if decision[i]==None:
    # 		waiting.append(numbers[i])
    		
    index=0
    for i in range(len(mobile_keys)):

    	keys_person= requests[mobile_keys[i]].keys()
    	for j in keys_person:
    		firebase1.put('requests/'+str(mobile_keys[i])+'/'+str(j),'status',decision[index])
    		index=index+1
    		




    return "<h1>%s</h1>"%str(decision)
    


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
    # r= firebase1.get('/Packages',None).keys()
    # r=len(r)
    # return "<h1> %s</h1>"%str(r)






    # r=firebase1.get("requests",None)
    # r1=firebase1.get("requestID",None)
    # r1=int(r1)
    # numbers=[]

    # for numb in r:
    #     numbers.append(numb)


    # length_numbers=len(numbers)

    # random=[]
    # c=1
    # requests=firebase1.get('requests',None)
    # mobile_keys=requests.keys()
    # keys_person= requests[mobile_keys[0]].keys()


    # date=[]
    # time=[]

    # for i in range(len(mobile_keys)):

    # 	keys_person= requests[mobile_keys[i]].keys()
    # 	for j in keys_person:
    # 		a=requests[mobile_keys[i]][j]['date']
    # 		date.append(a)

    # for i in range(len(mobile_keys)):

    # 	keys_person= requests[mobile_keys[i]].keys()
    # 	for j in keys_person:
    # 		a=requests[mobile_keys[i]][j]['time']
    # 		date.append(a)










    # for i in range(len(mobile_keys)):
    # 	for j in range(r1):
    # 		a=r[mobile_keys[i]][j]['date']
    # 		if(a):
    # 			random.append(a)


    # for i in mobile_keys.keys():
    # 	a=mobile_keys[i].get()
    # 	random.append(a)

    # j=firebase1.get('/requests/'+ str(mobile_keys[0]),None).keys()
    # j=mobile_keys[0]
    # r=r[numbers[0]].keys()

    # date=[]

    # for i in range(len(numbers)):
    # 	j=firebase1.get('/requests/'+ str(numbers[i]),None).keys()
    # 	j=len(j)

    # 	a=1
    # 	for x in j:
    # 		b=r[numbers[i]][a]['date']
    # 		date.append(b)
    # 		a=a+1

    # return "<h1> %s</h1>"%str(date)

    return render_template('login.html')


if __name__ == "__main__":
    #main()
    app.run(debug=True)