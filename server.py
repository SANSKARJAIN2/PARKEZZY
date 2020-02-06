from flask import Flask,request,redirect,url_for,render_template
from firebase_admin import credentials, db
import firebase_admin
#import firebase_data
app = Flask(__name__)

################################################################################
##################### FIREBASE CREDENTIALS #####################################
cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "aacharyabitrebels",
  "private_key_id": "9364d644863e276129c4ab27540f13a4270d3ab1",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCQJ2IZAUOhVL2Z\nAxttUPPvIz/TvkPN2/oGXMSqlDfAvU5aFEigXkrOLGz8MbiyUH1wCoJD/h2k63hp\no85kx0MxFz5Z2FxDJcD25xwjzwjV3iyRzGwLiPcoM0WzMHYoodIX+E0XtEn7a42j\nr67k2GOUYmgRydbf4pZ6WUv/bJHgCbbwXxM1Hv48SuAHywS+QcnqKaSk8Igr+LnI\nRMUkVAVyoeuZc6dlcy/qYfH/Us5gohK+K1bL5uRUPPXiPBYi9veOKLcRzRdcmq0M\nb/Xr2dVhcNwZuh6kr1dlDPuMGvJIE7WHCtccODVt9r4LGYP0nA0u88u6BUyc4K9+\n0n8HDh5HAgMBAAECggEAA/HP8WHjeTVZwCd28gArwfjI9QED10zprpA4oXek1EAE\ni4UlPPOCQIS0BsKljIY/UyLhJah9JIInrVxaIs/WZYV+o0lpsjyvkbyz5xbx5Z2g\nF+1BbPS2hAHDKoAXpkz8nsNLTha/ii2169YRhxmUv/62slCU8f4VTWEcKe/NSMAb\ndKQyokZM8XbrwBSgckkUvrcbIXbSYsFZZYgCPtX9mawBxCCClhTjdPio17b6Cb7y\nUHjziYchklqI5Uw1rHzguuxT4pS5aIwfKeFHG/btvFgGcBcjy+5mdngYlOuPrcCp\nkuM5fZ6ld2OSJGeZyrxVRs25u5Tqp4MTM0e22eznwQKBgQDAiid8ywGJU7guypz/\nZevhs8ily6sCz7BwJThO+89OXknbbamFH/RIrs8ev/551f0/k1Rdi9AvofpZaf/3\nLaZEXNU6I/GnXw/8b933V9iDuHOCTZSUzfiZ/rfeY3wUMRcR9FMMiKkvezeRkKCW\naFMPNkXwbh64nKk12vhS6GcO3wKBgQC/qpjC+wRA+w4LylqsnTV/jrck1ZEa7bxe\nu8gpzwcINc3FKP2EfqvK/O/UhrsNEB4/7msNc9wFYGaxDLp1prk1ymT6g/G1R+86\nUYP1dH/Wzs4hoduDsLbHXQV/zBj6El7B5oqgxcmWHyMSNznNzyt9DDxXNUDbsh98\nih8mXbAlmQKBgFgQGGV8mHROJWTJaStrW4r85t3mHI6JncJ9U5bUl4nZmGBTdQCd\nj+aahcMjv2nMVSt54FF0/EB9DntM/zT33R9RcnlILWQHF9G2/Mf/ltkQSUyk3Tt+\nRaFxnnmJ+RtnJI0iucV20CMWcWETzE9e4faINU71nvmDNeWbBI8vGsvzAoGBAK/6\npeoYaY50NDBVKi3k5jLpSXTTdjigYV0l0yG4CT/bjsPg3+ygFYH5/QZIckQLMYsH\nkFk4sKJrIb6b7jOJ0fH2lAKD1RDaLGeCYsOipKIJHbA5mYBvZ1LjMOJm9ePdrA0i\nbNQy5eUlT6Ew/aze85IMAvcbWSKeiFRjyTgDu3C5AoGBAIJeDesWDXR5mr07STvF\nYBDEOvBE2G+BefPwbOucuTWOOnGdkynyehkyhFSdpmhk6GRk0Sb/baTVvl3z6d0J\nC6bVcRx7t6u1p11+sCP3klW6STJRfW2OjhGngUygQv4YOo+v34u6RdfcO8ZtSFj/\nULHwxJaw+u5MX56nLTtsLVXU\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-b42s8@aacharyabitrebels.iam.gserviceaccount.com",
  "client_id": "116769742458900521850",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-b42s8%40aacharyabitrebels.iam.gserviceaccount.com"
}
)

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://aacharyabitrebels.firebaseio.com/'
})

####################FIREBASE CREDENTIALS########################################
################################################################################



def upload_data(*data):
    input(str(data[0])+str(data[1]))
    ref = db.reference("temp")
    child=ref.child(str(data[0]))
    child.set({
        "email": str(data[0]),
        "password": str(data[1]),
        "username": str(data[2]),
        "number": str(data[3]),
        "dl_no": str(data[4]),
        "address": str(data[5])
    })


    
def check_cred(email,password):
    ref=db.reference("temp")
    if str(ref.child(str(email)).get()) != "None":
        child=ref.child(str(email))
        data=child.get()
        if data["password"] == str(password):
            return True
        else:
            return False
    else:
        return False
    

@app.route("/")
def index():
    return render_template( "homestart.html")


@app.route("/newregister", methods = ["GET"])
def newregister():
    return render_template( "b (2).html")

@app.route("/register", methods = ["GET","POST"])
def register():
    email=request.form.get("email")
    password=request.form.get("password")
    username=request.form.get("name")
    number=request.form.get("contact_no")
    dl_no=request.form.get("dl_no")
    address=request.form.get("address")
    input(str(email)+str(password))
    upload_data(email,password,username,number,dl_no,address)
    return render_template( "login.html")



@app.route("/nishant")
def nishant():
    return render_template( "login.html")


@app.route("/noaccount")
def noaccount():
    return render_template( "register.html")
@app.route("/haveaccount")
def haveaccount():
    return render_template( "login.html")

@app.route('/login', methods = ["POST","GET"])
def login():

    email=request.form.get("email")
    password = request.form.get("password")
    login_type= check_cred(email,password)
    input(str(login_type))
    if login_type:
        return render_template("options.html")
    else:
#        return render_template("a(1).html")
        return render_template( "login.html")
#        return "invalid credentials"

if __name__=="__main__":
    app.run(debug=True)
