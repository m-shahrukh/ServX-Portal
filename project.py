from firebase import firebase
from flask import Flask, render_template, json, request, session, escape,redirect, url_for
import pyrebase
import copy
from pusher_push_notifications import PushNotifications 


config={
    "apiKey": "AIzaSyDSc5--FWUQkRLp8WArAPxKtCJxMAYawPk",
    "authDomain": "servx-f0d70.firebaseapp.com",
    "databaseURL": "https://servx-f0d70.firebaseio.com",
    "projectId": "servx-f0d70",
    "storageBucket": "servx-f0d70.appspot.com",
    "messagingSenderId": "1048415000509"
}

beams_client = PushNotifications(
instance_id='ea347389-aee7-4445-9b14-15cd0fe885f4',
secret_key='9272AAB0EA36F577C6AA861B2BFB5C0A329DC8561382D4F16661ADFC9541C7B4'
)


def send_push_notifcation(users, title, message):
   response = beams_client.publish(
   #interests=['03369696969'],
  interests=copy.deepcopy(users),
  publish_body={
    'fcm': {
      'notification': {
        'title': title,
        'body': message,
      },
    },
  },
)

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
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

firebase1 = firebase.FirebaseApplication('https://servx-f0d70.firebaseio.com/', authentication=None)
firebase2= pyrebase.initialize_app(config)
user_tok=None








@app.route("/signuppage")
def signup():
    return render_template('signup.html')

@app.route("/requests")
def Requestpage():
  if 'user' in session:


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
            if j!='"0"' and (requests[mobile_keys[i]][j]['status']=='pending' or requests[mobile_keys[i]][j]['status']=='Pending'):
                a=requests[mobile_keys[i]][j]['date']
                numbers.append(mobile_keys[i])
                #req_ID= int(j[1:len(j)-1])
                req_ID= j.replace("'","")
                req_ID=req_ID.replace('"',"")
                req_ID=int(req_ID)
                req_IDs.append(req_ID)
                date.append(a)

    for i in range(len(mobile_keys)):

        keys_person= requests[mobile_keys[i]].keys()
        for j in keys_person:
            if j!='"0"' and (requests[mobile_keys[i]][j]['status']=='pending' or requests[mobile_keys[i]][j]['status']=='Pending'):

                a=requests[mobile_keys[i]][j]['time']
                #req.time=a
                time.append(a)

    length_numbers=len(date)
    #req.numbers=length_numbers

    for i in range(len(mobile_keys)):

        keys_person= requests[mobile_keys[i]].keys()
        for j in keys_person:
            if j!='"0"' and (requests[mobile_keys[i]][j]['status']=='pending' or requests[mobile_keys[i]][j]['status']=='Pending'):
                a=requests[mobile_keys[i]][j]['oil']
                #req.oil=a
                oil.append(a)


    for i in range(len(mobile_keys)):

        keys_person= requests[mobile_keys[i]].keys()
        for j in keys_person:
            if j!='"0"' and (requests[mobile_keys[i]][j]['status']=='pending' or requests[mobile_keys[i]][j]['status']=='Pending'):
                a=requests[mobile_keys[i]][j]['wash']
                #req.wash=a
                wash.append(a)

    for i in range(len(mobile_keys)):

        keys_person= requests[mobile_keys[i]].keys()
        for j in keys_person:
            if j!='"0"' and (requests[mobile_keys[i]][j]['status']=='pending' or requests[mobile_keys[i]][j]['status']=='Pending'):
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

    reqs.sort(key= lambda x: x.requestID, reverse=False)




    #return str(len(reqs))
    #return "<h1>%s</h1"%str(reqs[0].requestID)
    return render_template('requests.html',reqs=reqs, enumerate= enumerate,length_numbers=length_numbers)
    #return render_template('requests.html', numbers=numbers, time=time,length_numbers=length_numbers,date=date,oil=oil,wash=wash,location=location)
  else:
      return render_template('login.html')


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
    req_ID_strs={}
    dict_reqs={}

    for i in range(len(mobile_keys)):

        keys_person= requests[mobile_keys[i]].keys()
        for j in keys_person:
            if j!='"0"' and (requests[mobile_keys[i]][j]['status']=='pending' or requests[mobile_keys[i]][j]['status']=='Pending'):
                numbers.append(mobile_keys[i])
                #req_ID= int(j[1:len(j)-1])
                
                req_ID= j.replace("'","")
                req_ID=req_ID.replace('"',"")
                req_ID=int(req_ID)
                req_ID_strs[req_ID]=j
                re=req()
                re.requestID=(req_ID)
                re.numbers=mobile_keys[i]
                reqs.append(re)
                dict_reqs[mobile_keys[i]] =requests[mobile_keys[i]]



    decision=[]
    reqs.sort(key= lambda x:x.requestID, reverse=False)
    #req_ID_strs.sort(key= lambda x: x.keys(), reverse= False)
    #return str(dict_reqs)
    

    for i in range(len(reqs)):

      decision1=request.form.get('dec'+reqs[i].numbers+str(i), None)

      decision.append(decision1)


    #decision=request.form.get('dec'+"03215468623"+"0")

    #return "<h1>%s</h1>"%str(decision)
    #return render_template('home.html', msg="decisions sent!")
    numbers_to_send=[]
    message_to_send={}
    # for x in reqs:
    #     if x in numbers_to_send:
    #         message_to_send[x]={"title":"Your requests have been processed",
    #                             "message":"Please check Service History!"}
    #     else:
    #         numbers_to_send.append(x)
    #         message_to_send[x]={"title":"Your request have been processed",
    #                             "message":"Please check Service History!"}

        

    index=0
    for i in range(len(reqs)):
        if decision[i]!=None:
                    if reqs[i].numbers in numbers_to_send:
                        message_to_send[reqs[i].numbers]={"title":"Your requests have been processed",
                                "message":"Please check Service History!"}
                    else:
                      numbers_to_send.append(reqs[i].numbers)
                      message_to_send[reqs[i].numbers]={"title":"Your request have been processed",
                                "message":"Please check Service History!"}

                    # print req_ID_strs[i]
                    # return req_ID_strs[i]
                    #j='"%s"'%str(reqs[i].requestID)
                    j=req_ID_strs[reqs[i].requestID]
                    #return j
                    # firebase1.put('requests/'+reqs[i].numbers+'/'+j,'status',decision[i])
                    # return "<h1>%s</h1>"%str(dict_reqs[i])
                    dict_reqs[reqs[i].numbers][j]['status']=decision[i]
                    # return "<h1>%s</h1>"%str(dict_reqs[i])
                    
                    firebase1.put("requests", reqs[i].numbers, dict_reqs[reqs[i].numbers])
                    #send_push_notifcation([reqs[i].numbers])
        # keys_person= requests[reqs[i].numbers].keys()
    for x in numbers_to_send:
        send_push_notifcation([x], message_to_send[x]['title'], message_to_send[x]['message'])
        # for j in keys_person:
        #     if j!='"0"':
        #         if decision[i]!=None:
        #             firebase1.put('requests/'+str(mobile_keys[i])+'/'+str(j),'status',decision[index])
        #         index=index+1
            


    # return "<h1>%s</h1>"%str(decision)
    #return render_template('home.html', msg="Decisions sent!")
    # return dict_reqs[i] 
    return redirect(url_for('Requestpage'))
    # return render_template('requests.html',reqs=reqs, enumerate= enumerate)
    


@app.route("/homepage", methods=['GET','POST'])
def HomePage():
    
    unsuccessful = 'Mobile number or password is invalid.'

    if request.method== 'GET':
        if 'user' in session:
            return render_template('home.html')
        else:
            return render_template('login.html')
    a=request.form.get('user', None)
    b=request.form.get('pass',None)
    r=firebase1.get('/User',None )
    if a not in r:
        return render_template('login.html', us=unsuccessful )
        
    email= r[a]['email']
    
    auth= firebase2.auth()
    
    user=str(None)
    try:
     user= auth.sign_in_with_email_and_password(email, b)
     #user_tok=auth.get_account_info(user['idToken'])
     session['user']=a
     return render_template('home.html')
    except:
        user=None
        return render_template('login.html', us=unsuccessful )


    
@app.route("/logout")
def logout():
    session.pop('user',None)
    return render_template('login.html')

@app.route("/homepage1", methods=['POST'])
def HomePage1():

    #r= request.form.get('user',None)
    # r= request.form['pass']


    err1='Incorrect Mobile Number.'
    err2='Please type your password again.'
    err3='Password length too short, must be 8 digits'
    err4='Mobile number must consist of digits.'
    err5='Name must consist of alphabets.'
    err7='Enter your credentials to login now.'
    err6='Invalid email address was entered.'

    a=request.form.get('name', None)
    b=request.form.get('email',None)
    c=request.form.get('mobile', None)
    d=request.form.get('pass',None)
    e=request.form.get('confirmpass', None)
    admin_key= request.form.get('adminpass',None)



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
    auth= firebase2.auth()
    check=0

    try:
        user=auth.sign_in_with_email_and_password("admin@servx.pk", admin_key)
        check=1
    except:
        check=0


    if check==1:
     auth.create_user_with_email_and_password(b,d)
     result = firebase1.put("User",c,{'name': a, 'email': b, 'isAdmin':'1'})
     return render_template('login.html', us=err7)
    return render_template('signup.html', us='Please Enter the correct Admin Key')


@app.route("/")
def index():

    return render_template('login.html')
@app.route("/customers")
def customers():
    #post= firebase.get('/User', None)
    #return post.Name
    #return render_template('customers.html', posts=posts)
  
  if 'user' in session:
    posts  = []

            
    

    c=" "
    i=","
    j=0
    n=""
    q=firebase1.get("/User",None)
    for key in q.keys(): 
        if q[key].get('isAdmin')=='1': 
            continue
        n=q[key].get('Name')
        if n==None:
            n=q[key].get('name')
        e=q[key].get('email')
        v= q[key].get('vehicle')
        if v!=None: 
            for vkeys, value in v.items():
                j=j+1
                if j>1: 
                    c=c+" , "+ vkeys +"("+ value.get('vmake') + "," + value.get('vyear') +"," + value.get('vmodel') + ")"
                else: 
                    c=c+ vkeys + "("+ value.get('vmake') + "," + value.get('vyear') +"," + value.get('vmodel') + ")"
        if v==None: 
            c="Not added yet"
        m= key
        j=0

        posts.append({'customer_name': n, 'email':e, 'mobile_number':key, 'cars': c})
        c=""
        lsls=""

        
    newlist=sorted(posts, key=lambda k: k['customer_name'])  ##upper case listings first, and then the lower case ones. 
    return render_template('customers.html', posts=newlist)
  else:
      return render_template('login.html')
@app.route("/history")
def History():
  if 'user' in session:
    hists=[]
    r=firebase1.get('/requests',None)
    rkeys= r.keys()
    c=firebase1.get('/Packages',None)
    q=firebase1.get('/User',None)

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
    n=None
    for i in range(len(r)):

        keys_person= r[rkeys[i]].keys()
        for j in keys_person:
            for key in q.keys():
                if rkeys[i]==key: 
                    n= q[key].get('Name')
                    if n==None: 
                        n=q[key].get('name')
            #print n
            #if (j=="106"):
            #    return str(r[rkeys[i]][j].get('status'))
            stat=r[rkeys[i]][j].get('status')
            if j!='"0"' and (stat!='Pending' and stat!='Pending'):
                #return str(r[rkeys[i]][j]) 
                s= r[rkeys[i]][j].get('status')
                
                s1=r[rkeys[i]][j].get('date')
                s2=r[rkeys[i]][j].get('location')
                s3=r[rkeys[i]][j].get('oil')
                if s3=='Gold' or s3=='gold':
                  bill=oilgold
                if s3== "" :
                    s3="Not Selected"
                if s3=='Silver' or s3=='silver': 
                  bill= oilsilver
                if s3=='Bronze' or s3=='bronze': 
                  bill==oilbr
                s4=r[rkeys[i]][j].get('wash')
                if s4== "": 
                    s4="Not Selected"
                if s4=='Gold' or s4== 'gold':
                  bill1=washgold
                if s4=='Silver' or s4=='silver':
                  bill1=washsilver
                if s4=='Bronze' or s4=='bronze': 
                  bill1=washbr

                totalbill= int(bill)+ int(bill1)
                s5=r[rkeys[i]][j].get('time')
                #pos.append({'status': s})
                
                hists.append({'rID':j,'customer_name': n, 'total_cost':totalbill,'location':s2,'oil':s3,'wash':s4,'date':s1,'time':s5, 'status': s})
                bill1=0
                bill=0
                totalbill=0
    newlist=sorted(hists, key=lambda k: k.get('rID'), reverse=True)   
    #return str(len(newlist))
    return render_template('history.html', posts=newlist)
  else:
      return render_template('login.html')




if __name__ == "__main__":
    #main()
    app.run(debug=False)
