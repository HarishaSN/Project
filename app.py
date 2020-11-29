from flask import Flask,render_template,request
# import functions

app=Flask(__name__)

# dbconn={"host":"localhost","user":"dbms_project","password":"passwd","database":"mini_project"} #sql user and database details
# ldetail=[]



@app.route("/")
def hello():
    return render_template('home.html',the_title='beds4meds')

@app.route('/home')
def h():
        return render_template('beds4meds.html',the_title='search')

@app.route("/login")
def login():
    return render_template('loginpage.html',the_title='login')

@app.route("/register")
def register():
    return render_template('register.html',the_title='register')

@app.route("/success" ,methods=['post'])
def success():
    return "success"

@app.route("/hsearch",methods=['POST'])
def hsearch():
    l=('hospital_id','ward_no','hospital_name','hospital_address','contact_no','no_of_beds','cost_per_day')
    ldetail.clear()
    req = request.form

    missing = list()

    for k, v in req.items():
        if v == "":
            missing.append(k)                                #checking if all details are entered

    if missing:
        return 'please enter all details'

    
    pname=request.form['name']
    Age=request.form['age']
    cno=request.form['cno']
    wardno=request.form['wardno']                            #taking all details filled in form
    gender=request.form.getlist('gender')
    g =gender[0]
    ldetail.extend([pname,Age,cno,wardno,g])
    
    contents=functions.search_hospital_in_ward_without_v(wardno)
    if len(contents)==0:                                                   #checking if hospital is present or not
        return render_template('hsearch_no_hospital.html',the_name=pname,the_age=Age,the_wardno=wardno,the_gender=g,the_contno=cno)
    elif int(Age)<60:                                                      #checking age ,if age>60 then recommend hospital with ventilators
        return render_template('hsearch_in_ward.html',the_name=pname,the_age=Age,the_wardno=wardno,the_gender=g,the_contno=cno,row_titles=l,the_data=contents)

@app.route('/confirm',methods=['POST'])
def confirm():
    return ldetail[0]
    
if __name__=="__main__":
    app.run(debug=True)