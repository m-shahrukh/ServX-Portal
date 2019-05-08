from flask import Flask, render_template, json, request
from firebase import firebase
import copy



class req:
    
    def  __init__(self):
        self.numbers=None
        self.date=None
        self.time=None
        self.oil=None
        self.wash=None
        self.location=None
        self.requestID=None


app = Flask(__name__)
firebase1 = firebase.FirebaseApplication('https://servx-f0d70.firebaseio.com/', None)


global length_requests
posts  = []
hists=[]


@app.route("/signuppage")
def signup():
    return render_template('signup.html')

@app.route("/requests")
def Requestpage():

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
    #keys_person= requests[mobile_keys[0]].keys()


    date=[]
    time=[]
    oil=[]
    wash=[]
    location=[]
    #reqs= req()
    req_IDs=[]

    for i in range(len(mobile_keys)):

        keys_person= requests[mobile_keys[i]].keys() #requestIds
        for j in keys_person:
            if j!='"0"' and requests[mobile_keys[i]][j]['status']=='pending':
                a=requests[mobile_keys[i]][j]['date']
                numbers.append(mobile_keys[i])
                req_ID= int(j[1:len(j)-1])
                req_IDs.append(req_ID)
                date.append(a)

    for i in range(len(mobile_keys)):

        keys_person= requests[mobile_keys[i]].keys()
        for j in keys_person:
            if j!='"0"' and requests[mobile_keys[i]][j]['status']=='pending':

                a=requests[mobile_keys[i]][j]['time']
                #req.time=a
                time.append(a)

    length_numbers=len(date)
    #req.numbers=length_numbers

    for i in range(len(mobile_keys)):

        keys_person= requests[mobile_keys[i]].keys()
        for j in keys_person:
            if j!='"0"' and requests[mobile_keys[i]][j]['status']=='pending':
                a=requests[mobile_keys[i]][j]['oil']
                #req.oil=a
                oil.append(a)


    for i in range(len(mobile_keys)):

        keys_person= requests[mobile_keys[i]].keys()
        for j in keys_person:
            if j!='"0"' and requests[mobile_keys[i]][j]['status']=='pending':
                a=requests[mobile_keys[i]][j]['wash']
                #req.wash=a
                wash.append(a)

    for i in range(len(mobile_keys)):

        keys_person= requests[mobile_keys[i]].keys()
        for j in keys_person:
            if j!='"0"' and requests[mobile_keys[i]][j]['status']=='pending':
                a=requests[mobile_keys[i]][j]['location']
                #req.location=a
                location.append(a)

    reqs=[req() for i in range(length_numbers)]

    for i in range(length_numbers):
        reqs[i].numbers=numbers[i]
        reqs[i].date=date[i]
        reqs[i].time=time[i]
        reqs[i].oil=oil[i]
        reqs[i].wash=wash[i]
        reqs[i].location=location[i]
        reqs[i].requestID=req_IDs[i]
        #req_IDs[i]=reqs[i].requestID

    reqs.sort(key= lambda x: x.requestID, reverse=True)





    #return "<h1>%s</h1"%str(reqs[0].requestID)
    return render_template('requests.html',reqs=reqs, enumerate= enumerate)
    #return render_template('requests.html', numbers=numbers, time=time,length_numbers=length_numbers,date=date,oil=oil,wash=wash,location=location)

@app.route("/requests1", methods=['POST'])
def Requestpage1():

    # decision=request.form.get('dec', None)

    # firebase1.put('requests/03215468623/0','status',decision)
    # return "<h1>%s</h1>"%decision

    numbers=[]

    requests=firebase1.get('requests',None)
    mobile_keys=requests.keys()
    # keys_person= requests[mobile_keys[0]].keys()
    reqs=[]

    for i in range(len(mobile_keys)):

        keys_person= requests[mobile_keys[i]].keys()
        for j in keys_person:
            if j!='"0"' and requests[mobile_keys[i]][j]['status']=='pending':
                numbers.append(mobile_keys[i])
                req_ID= int(j[1:len(j)-1])
                re=req()
                re.requestID=(req_ID)
                re.numbers=mobile_keys[i]
                reqs.append(re)



    decision=[]
    reqs.sort(key= lambda x:x.requestID, reverse=True)

    for i in range(len(reqs)):

      decision1=request.form.get('dec'+reqs[i].numbers+str(i), None)

      decision.append(decision1)


    #decision=request.form.get('dec'+"03215468623"+"0")

    #return "<h1>%s</h1>"%str(decision)
    #return render_template('home.html', msg="decisions sent!")


    index=0
    for i in range(len(reqs)):
        if decision[i]!=None:
                    j='"%s"'%str(reqs[i].requestID)
                    firebase1.put('requests/'+reqs[i].numbers+'/'+j,'status',decision[i])
        # keys_person= requests[reqs[i].numbers].keys()
        # for j in keys_person:
        #     if j!='"0"':
        #         if decision[i]!=None:
        #             firebase1.put('requests/'+str(mobile_keys[i])+'/'+str(j),'status',decision[index])
        #         index=index+1
            


    #return "<h1>%s</h1>"%str(decision)
    return render_template('home.html', msg="Decisions sent!")
    


@app.route("/homepage", methods=['GET','POST'])
def HomePage():
    #r="HALO"
    #r= request.form.get('user',None)
    #r= request.form['pass']
    
    if request.method== 'GET':
        return render_template('home.html')
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
@app.route("/customers",methods=['GET', 'POST'])
def customers():
    #post= firebase.get('/User', None)
    #return post.Name
    #return render_template('customers.html', posts=posts)

    c=" "
    i=","
    j=0
    q=firebase1.get("/User",None)
    for key in q.keys(): 
        n=q[key].get('Name')
        if n==None:
            n=q[key].get('name')
        e=q[key].get('email')
        v= q[key].get('vehicle')
        if v!=None: 
            for keys in v.keys():
                j=j+1
                if j>1: 
                    c=c+" , "+ keys
                else: 
                    c=c+ keys
        m= key
        j=0

        posts.append({'customer_name': n, 'email':e, 'mobile_number':key, 'cars': c})
        c=""
        lsls=""



    return render_template('customers.html', posts=posts)

@app.route("/history", methods=['GET', 'POST'])
def History():
    r=firebase1.get('/requests',None)
    rkeys= r.keys()
    c=firebase1.get('/Packages',None)

    costs=[]
    rkeys= r.keys()
    ckey= c.keys()
    oilbr=0
    oilgold=0
    oilsilver=0
    washbr=0
    washgold=0
    washsilver=0
    bill=0
    bill1=0
    totalbill=0



  
    for i in range(len (c)):
        a=ckey[i]
    #print a - the categories of oil change and car wash
        ck= c[ckey[i]].keys()
        for j in ck: 
          s= c[ckey[i]][j].get('Cost')
          if (j=='Gold' or j=='gold') and  a=='CarWash': 
            washgold=s
          if (j=='Silver' or j=='silver') and  a=='CarWash': 
            washsilver=int (s)
          if (j=='Bronze' or j=='bronze') and  a=='CarWash': 
            washbr=int (s)
          if (j=='Gold' or j=='gold') and  a=='OilChange': 
            oilgold=s
          if (j=='Silver' or j=='silver') and  a=='OilChange': 
            oilsilver=int (s)
          if (j=='Bronze' or j=='bronze') and  a=='OilChange': 
            oilbr=int (s) 
          













  #pos=[{'status':''}]
    for i in range(len(r)):

        keys_person= r[rkeys[i]].keys()
        for j in keys_person:
            if j!='"0"': 
                s= r[rkeys[i]][j].get('status')
                s1=r[rkeys[i]][j]['date']
                s2=r[rkeys[i]][j]['location']
                s3=r[rkeys[i]][j]['oil']
                if s3=='Gold' or s3=='gold':
                  bill=oilgold
                if s3=='Silver' or s3=='silver': 
                  bill= oilsilver
                if s3=='Bronze' or s3=='bronze': 
                  bill==oilbr
                s4=r[rkeys[i]][j]['wash']
                if s4=='Gold' or s4== 'gold':
                  bill1=washgold
                if s4=='Silver' or s4=='silver':
                  bill1=washsilver
                if s4=='Bronze' or s4=='bronze': 
                  bill1=washbr

                totalbill= int(bill)+ int(bill1)
                s5=r[rkeys[i]][j]['time']
                #pos.append({'status': s})
                
                hists.append({'customer_name': 'dummy name', 'total_cost':totalbill,'location':s2,'oil':s3,'wash':s4,'date':s1,'time':s5, 'status': s})
                #bill1=0
                #bill=0
                #totalbill=0

    return render_template('history.html', posts=hists)



if __name__ == "__main__":
    #main()
    app.run(debug=True)
