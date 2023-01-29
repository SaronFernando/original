from flask import Flask,render_template, request, redirect
import json_utils 

file="data/user.user.json"


app=Flask(__name__)
@app.route("/")
def index ():
    return render_template('homepage.html')

@app.route("/get_insurance",methods=["GET","POST"])
def register():
    return render_template("register.html")

@app.route("/register",methods=["GET","POST"])
def new_register():
    if request.methods=="POST":
        name=request.form["name"]
        email=request.form["email"]
        phone=request.form["phone"]
        password=request.form["password"]
        data=json_utils.read_json(file)
        user={
            "name":name,
            "email":email,
            "phone":phone,
            "password":password,
        }
        data["user"].append(user)
        print(data)
        json_utils.write_json(file,data)
    return redirect("/")

@app.route("/health_insurance#" , methods=["GET","POST"])     
def health_insurance():
    render_template("health_insurance.html")      
            
@app.route("/home_insurance#" , methods=["GET","POST"])     
def home_insurance():
    render_template("home_insurance.html")      

@app.route("/life_insurance.html" , methods=["GET","POST"])     
def life_insurance():
    render_template("life_insurance.html")      
            
@app.route("/property_insurance#" , methods=["GET","POST"])     
def property_insurance():
    render_template("property_insurance.html")      
            
@app.route("/vehicle_insurance#" , methods=["GET","POST"])     
def vehicle_insurance():
    render_template("vehicle_insurance.html")      
            
                                                                    
    
    
    

        

if __name__=="__main__"  :
    app.run(debug=True)
