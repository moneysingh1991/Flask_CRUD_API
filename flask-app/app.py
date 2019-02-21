from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to CRUD API Demo \n \n <br>\
    1: Get All user List : Go to URl: localhost:5000/users  \n \n<br>\
    2: Get user by id : URL: localhost:5000/user , Request = GET, param = {"id":"3"} \n\n<br>\
    3: UPDATE user by id : URL: localhost:5000/user , Request = PUT, param = {\
	"name":"Samsung", \
	"id":"3", \
	"email":"samsung@gmail.com",\
	"pwd":"fsvdcs"\
    } \n\n<br>\
    4: DELETE user by id : URL: localhost:5000/delete , Request = DELETE, param = {"id":"3"} \n\n <br>\
    '