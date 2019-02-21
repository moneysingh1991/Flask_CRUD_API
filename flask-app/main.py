import pymysql
from app import app
from flask import jsonify
from flask import Flask, request
from werkzeug import generate_password_hash, check_password_hash

import pymysql

host = "localhost"
user = "root"
password = "9872476129Mm$"
db = "flask"


def buildConnection():

	return pymysql.connect(host='localhost',user='root',password='',db='flask',cursorclass=pymysql.cursors.DictCursor, autocommit=True)
	




@app.route('/add', methods=['POST'])
def addUser():
	conn = buildConnection()
	cursor = conn.cursor()

	try:
		
		name = request.json['name']
		email = request.json['email']
		password = request.json['pwd']

		# validate the received values
		if name and email and password and request.method == 'POST':
			#do not save password as a plain text
			hashed_password = generate_password_hash(password)
			# save edits
			sql = "INSERT INTO tbl_user(user_name, user_email, user_password) VALUES('%s', '%s', '%s')" % (name, email, hashed_password)
			
		
			try:
				affected_count = cursor.execute(sql)
				conn.commit()
				print("response sql : %d", affected_count)
			except Exception as e:
				print(e)
			
			resp = jsonify('User added successfully!')
			resp.status_code = 200
			return resp
		else:
			
			return notFound()
			
	except Exception as e:
		
		print(e)
	finally:
		cursor.close() 
		conn.close()
	
		
@app.route('/users')
def getUsers():
	try:
		

		conn = buildConnection()
		cursor = conn.cursor()
		cursor.execute("SELECT user_name,user_email FROM tbl_user")
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/user')
def getUser():
	
	userId = request.json['id']

	try:
		conn = buildConnection()
		cursor = conn.cursor()
		cursor.execute("SELECT user_name,user_email FROM tbl_user WHERE user_id=%s", userId)
		row = cursor.fetchone()
		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/update', methods=['PUT'])
def updateUser():

	conn = buildConnection()
	cursor = conn.cursor()

	if request.method != 'PUT':
		return notFound()

	try:
		json = request.json
		userId = json['id']
		name = json['name']
		email = json['email']
		password = json['pwd']		
		# validate the received values
		if name and email and password and userId and request.method == 'PUT':
			#do not save password as a plain text
			hashed_password = generate_password_hash(password)
			# save edits
			sql = "UPDATE tbl_user SET user_name=%s, user_email=%s, user_password=%s WHERE user_id=%s"
			data = (name, email, hashed_password, userId,)
			
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('User updated successfully!')
			resp.status_code = 200
			return resp
		else:
			return notFound()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
	

@app.route('/delete',  methods=['DELETE'])
def deleteUser():
	userId = request.json['id']

	if request.method != 'DELETE':
		return notFound()
	try:
		conn = buildConnection()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM tbl_user WHERE user_id=%s", (userId))
		conn.commit()
		resp = jsonify('User deleted successfully!')
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.errorhandler(404)
def notFound(error=None):
    message = {
        'status': 404,
        'message': 'Not Found url: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp
		
if __name__ == "__main__":
    app.run()