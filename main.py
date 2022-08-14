import pymysql
from app import app
from config import mysql 
from flask import jsonify
from flask import flash, request
import json


@app.route('/createplot',methods=['POST'])
def create_plot():
	try:
		_json = request.json
		_projectname = _json['projectname']
		_plotno = _json['plotno']
		_plotarea = _json['plotarea']
		_ratesqft = _json['ratesqft']
		_status = _json['status']
		_id = _json['id']
		print(_json)
		if _projectname and _plotno and _plotarea and _ratesqft and _status and request.method == 'POST':
			sqlQuery = "INSERT INTO addplots(projectname, plotno, plotarea, ratesqft, status, id) VALUES(%s, %s, %s, %s, %s, %s)"
			bindData = (_projectname, _plotno, _plotarea, _ratesqft, _status, _id)
			conn = mysql.connect()
			cursor = conn.cursor(pymysql.cursors.DictCursor)
			cursor.execute(sqlQuery, bindData)
			conn.commit()
			response = jsonify("Plots added successfully!")
			response.status_code = 200
			cursor.close()
			conn.close()	
		else:
			response = jsonify("Body not found")
			response.status_code = 400
	except Exception as e:
		print(e)
		response = jsonify("Failed to plots not added")
		response.status_code = 400
	finally:
		return response
		
		

@app.route('/plots',methods=['GET'])
def plot():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM addplots")
		plotRows = cursor.fetchall()
		response = json.dumps(plotRows, indent=2)
		response.status_code = 200
		cursor.close()
		conn.close()
		
	except Exception as e:
		print(e)
	finally:
		return response
		

@app.route('/plot/<int:plot_id>',methods=['GET'])
def plot_details(plot_id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM addplots WHERE id =%s", plot_id)
		plotRow = cursor.fetchone()
		response = json.dumps(plotRow, indent=2)
		return response
		respone.status_code = 200
		cursor.close()
		conn.close()
	except Exception as e:
		print(e)
	finally:
		return response
		
		


@app.route('/updateplot/<int:plot_id>',methods=['PUT'])
def update_plot(plot_id):
	try:
		_json = request.json
		_projectname = _json['projectname']
		_plotno = _json['plotno']
		_plotarea = _json['plotarea']
		_ratesqft = _json['ratesqft']
		_status = _json['status']
		_id = _json['id']
		print(_json)
		if _projectname and _plotno and _plotarea and _ratesqft and _status and request.method == 'PUT':
			sqlQuery = "UPDATE addplots SET projectname=%s, plotno=%s, plotarea=%s, ratesqft=%s, status=%s WHERE id=%s"
			bindData = (_projectname, _plotno, _plotarea, _ratesqft, _status, _id)
			conn = mysql.connect()
			cursor = conn.cursor(pymysql.cursors.DictCursor)
			cursor = conn.cursor()
			cursor.execute(sqlQuery, bindData)
			conn.commit()
			response = jsonify("Plots update successfully!")
			response.status_code = 200
			cursor.close()
			conn.close()
		else:
			return showmessage()
	except Exception as e:
		print(e)
	finally:
		return response
		



@app.route('/plotdelete/<int:id>', methods=['DELETE'])
def delete_plot(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM addplots WHERE id =%s", (id))
		conn.commit()
		response = jsonify('Plots deleted successfully!')
		response.status_code = 200
		return response
		cursor.close()
		conn.close()
		
	except:
		print(e)
	finally:
		return response

@app.errorhandler(404)
def showmessage(error=None):
	message = {
		'status': 404,
		'message': 'Record not found:' + request.url,	
		}
	response = jsonify(message)
	response.status_code = 404
	return response




############################################ PROJECT CRUD###########################################################






@app.route('/createproject',methods=['POST'])
def create_project():
	try:
		_json = request.json
		_projectimage = _json['projectimage']
		_pname = _json['pname']
		_paddress = _json['paddress']
		_tarea = _json['tarea']
		_nplots = _json['nplots']
		_aplots = _json['aplots']
		_splots = _json['splots']
		_slider1 = _json['slider1']
		_slider2 = _json['slider2']
		_certificate = _json['certificate']
		_inp = _json['inp']
		_comment = _json['comment']
		if _projectimage and _pname and _paddress and _tarea and _nplots and _aplots and _splots and _slider1 and _slider2 and _certificate and _inp and _comment and request.method == 'POST':
			sqlQuery2 = "INSERT INTO addproject(projectimage, pname, paddress, tarea, nplots, aplots, splots, slider1, slider2, certificate, inp, comment) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
			bindData2 = (_projectimage, _pname, _paddress, _tarea, _nplots, _aplots, _splots, _slider1, _slider2, _certificate, _inp, _comment)
			conn = mysql.connect()
			cursor = conn.cursor(pymysql.cursors.DictCursor)
			cursor.execute(sqlQuery2, bindData2)
			conn.commit()
			response = jsonify("Project added successfully!")
			response.status_code = 200
			cursor.close()
			conn.close()	
		else:
			response = jsonify("Body not found")
			response.status_code = 400
	except Exception as e:
		print(e)
		response = jsonify("Failed to projects not added")
		response.status_code = 400
	finally:
		return response




@app.route('/projects',methods=['GET'])
def project():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM addproject")
		projectRows = cursor.fetchall()
		response = json.dumps(projectRows, indent=2)
		response.status_code = 200
		cursor.close()
		conn.close()
		
	except Exception as e:
		print(e)
	finally:
		return response
		

@app.route('/project/<int:project_id>',methods=['GET'])
def project_details(project_id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM addproject WHERE id =%s", project_id)
		projectRow = cursor.fetchone()
		response = json.dumps(projectRow, indent=2)
		return response
		respone.status_code = 200
		cursor.close()
		conn.close()
	except Exception as e:
		print(e)
	finally:
		return response



@app.route('/updateproject/<int:project_id>',methods=['PUT'])
def update_project(project_id):
	try:
		_json = request.json
		_projectimage = _json['projectimage']
		_pname = _json['pname']
		_paddress = _json['paddress']
		_tarea = _json['tarea']
		_nplots = _json['nplots']
		_aplots = _json['aplots']
		_splots = _json['splots']
		_slider1 = _json['slider1']
		_slider2 = _json['slider2']
		_certificate = _json['certificate']
		_inp = _json['inp']
		_comment = _json['comment']
		_id = _json['id']
		print(_json)
		if _projectimage and _paddress and _pname and _tarea and _nplots and _aplots and _splots and _slider1 and _slider2 and _certificate and _inp and _comment and request.method == 'PUT':
			sqlQuery2 = "UPDATE addproject SET projectimage=%s, pname=%s, paddress=%s, tarea=%s, nplots=%s, aplots=%s, splots=%s, slider1=%s, slider2=%s, certificate=%s, inp=%s, comment=%s WHERE id=%s"
			bindData2 = (_projectimage, _pname, _paddress, _tarea, _nplots, _aplots, _splots, _slider1, _slider2, _certificate, _inp, _comment, _id)
			conn = mysql.connect()
			cursor = conn.cursor(pymysql.cursors.DictCursor)
			cursor = conn.cursor()
			cursor.execute(sqlQuery2, bindData2)
			conn.commit()
			response = jsonify("Project update successfully!")
			response.status_code = 200
			cursor.close()
			conn.close()
		else:
			return showmessage()
	except Exception as e:
		print(e)
	finally:
		return response


@app.route('/deleteproject/<int:id>', methods=['DELETE'])
def delete_project(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM addproject WHERE id =%s", (id))
		conn.commit()
		response = jsonify('Project deleted successfully!')
		response.status_code = 200
		return response
		cursor.close()
		conn.close()
		
	except:
		print(e)
	finally:
		return response



@app.errorhandler(404)
def showmessage(error=None):
	message = {
		'status': 404,
		'message': 'Record not found:' + request.url,	
		}
	response = jsonify(message)
	response.status_code = 404
	return response





################################################ADVISORY CRUD####################################################################



@app.route('/createadvisory',methods=['POST'])
def create_advisory():
	try:
		_json = request.json
		_name = _json['name']
		_address = _json['address']
		_contact = _json['contact']
		_email = _json['email']
		_adharcard = _json['adharcard']
		_designation = _json['designation']
		_password = _json['password']
		print(_json)
		if _name and _address and _contact and _email and _adharcard and _designation and _password and request.method == 'POST':
			sqlQuery3 = "INSERT INTO advisory(name, address, contact, email, adharcard, designation, password) VALUES(%s, %s, %s, %s, %s, %s, %s)"
			bindData3 = (_name, _address, _contact, _email, _adharcard, _designation, _password)
			conn = mysql.connect()
			cursor = conn.cursor(pymysql.cursors.DictCursor)
			cursor.execute(sqlQuery3, bindData3)
			conn.commit()
			response = jsonify("Advisory added successfully!")
			response.status_code = 200
			cursor.close()
			conn.close()	
		else:
			response = jsonify("Body not found")
			response.status_code = 400
	except Exception as e:
		print(e)
		response = jsonify("Failed to advisory not added")
		response.status_code = 400
	finally:
		return response
		
		

@app.route('/advisorys',methods=['GET'])
def advisory():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM advisory")
		advisoryRows = cursor.fetchall()
		response = json.dumps(advisoryRows, indent=2)
		response.status_code = 200
		cursor.close()
		conn.close()
		
	except Exception as e:
		print(e)
	finally:
		return response
		

@app.route('/advisory/<int:id>',methods=['GET'])
def advisory_details(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM advisory WHERE id =%s", id)
		advisoryRow = cursor.fetchone()
		response = json.dumps(advisoryRow, indent=2)
		return response
		respone.status_code = 200
		cursor.close()
		conn.close()
	except Exception as e:
		print(e)
	finally:
		return response
		
		


@app.route('/updateadvisory/<int:id>',methods=['PUT'])
def update_advisory(id):
	try:
		_json = request.json
		_name = _json['name']
		_address = _json['address']
		_contact = _json['contact']
		_email = _json['email']
		_adharcard = _json['adharcard']
		_designation = _json['designation']
		_password = _json['password']
		_id = _json['id']
		print(_json)
		if _name and _address and _contact and _email and _adharcard and _designation and _password and request.method == 'PUT':
			sqlQuery3 = "UPDATE advisory SET name=%s, address=%s, contact=%s, email=%s, adharcard=%s, designation=%s, password=%s WHERE id=%s"
			bindData3 = (_name, _address, _contact, _email, _adharcard, _designation, _password, _id)
			conn = mysql.connect()
			cursor = conn.cursor(pymysql.cursors.DictCursor)
			cursor = conn.cursor()
			cursor.execute(sqlQuery3, bindData3)
			conn.commit()
			response = jsonify("Advisory update successfully!")
			response.status_code = 200
			cursor.close()
			conn.close()
		else:
			return showmessage()
	except Exception as e:
		print(e)
	finally:
		return response
		



@app.route('/deleteadvisory/<int:id>', methods=['DELETE'])
def delete_advisory(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM advisory WHERE id =%s", (id))
		conn.commit()
		response = jsonify('Advisory deleted successfully!')
		response.status_code = 200
		return response
		cursor.close()
		conn.close()
		
	except:
		print(e)
	finally:
		return response

@app.errorhandler(404)
def showmessage(error=None):
	message = {
		'status': 404,
		'message': 'Record not found:' + request.url,	
		}
	response = jsonify(message)
	response.status_code = 404
	return response


####################################################BARGRAPH CRUD#####################################################



@app.route('/createbargraph',methods=['POST'])
def create_graph():
	try:
		_json = request.json
		_x = _json['x']
		_y = _json['y']
		_id = _json['id']
		print(_json)
		if _x and _y and request.method == 'POST':
			sqlQuery4 = "INSERT INTO bargraph(x, y, id) VALUES(%s, %s, %s)"
			bindData4 = (_x, _y, _id)
			conn = mysql.connect()
			cursor = conn.cursor(pymysql.cursors.DictCursor)
			cursor.execute(sqlQuery4, bindData4)
			conn.commit()
			response = jsonify("Bargraph added successfully!")
			response.status_code = 200
			cursor.close()
			conn.close()	
		else:
			response = jsonify("Body not found")
			response.status_code = 400
	except Exception as e:
		print(e)
		response = jsonify("Failed to Bargraph not added")
		response.status_code = 400
	finally:
		return response
		
		

@app.route('/bargraph',methods=['GET'])
def graph():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM bargraph")
		graphRows = cursor.fetchall()
		response = json.dumps(graphRows, indent=2)
		response.status_code = 200
		cursor.close()
		conn.close()
		
	except Exception as e:
		print(e)
	finally:
		return response
		

@app.route('/bargraph/<int:id>',methods=['GET'])
def graph_details(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM bargraph WHERE id =%s", id)
		graphRow = cursor.fetchone()
		response = json.dumps(graphRow, indent=2)
		return response
		respone.status_code = 200
		cursor.close()
		conn.close()
	except Exception as e:
		print(e)
	finally:
		return response
		
		


@app.route('/updatebargraph/<int:id>',methods=['PUT'])
def update_graph(id):
	try:
		_json = request.json
		_x = _json['x']
		_y = _json['y']
		_id = _json['id']
		print(_json)
		if _x and _y and request.method == 'PUT':
			sqlQuery4 = "UPDATE bargraph SET x=%s, y=%s WHERE id=%s"
			bindData4 = (_x, _y, _id)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor = conn.cursor(pymysql.cursors.DictCursor)
			cursor.execute(sqlQuery4, bindData4)
			conn.commit()
			response = jsonify("Bargraphs update successfully!")
			response.status_code = 200
			cursor.close()
			conn.close()
		else:
			return showmessage()
	except Exception as e:
		print(e)
	finally:
		return response
		



@app.route('/deletebargraph/<int:id>', methods=['DELETE'])
def delete_graph(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM bargraph WHERE id =%s", (id))
		conn.commit()
		response = jsonify('Bargraphs deleted successfully!')
		response.status_code = 200
		return response
		cursor.close()
		conn.close()
		
	except:
		print(e)
	finally:
		return response

@app.errorhandler(404)
def showmessage(error=None):
	message = {
		'status': 404,
		'message': 'Record not found:' + request.url,	
		}
	response = jsonify(message)
	response.status_code = 404
	return response



#############################################################BOOKING CRUD############################################################



@app.route('/createbooking',methods=['POST'])
def create_book():
	try:
		_json = request.json
		_fname = _json['fname']
		_mname = _json['mname']
		_lname = _json['lname']
		_address = _json['address']
		_city = _json['city']
		_state = _json['state']
		_pincode = _json['pincode']
		_phoneno = _json['phoneno']
		_idproof = _json['idproof']
		_email = _json['email']
		_dob = _json['dob']
		_projectname = _json['projectname']
		_mouza = _json['mouza']
		_plotno = _json['plotno']
		_plotarea = _json['plotarea']
		_ratesqft = _json['ratesqft']
		_advisoryname = _json['advisoryname']
		_reference = _json['reference']
		_bookingdate = _json['bookingdate']
		_status = _json['status']
		#_id = _json['id']
		print(_json)
		if _fname and _mname and _lname and _address and _city and _state and _pincode and _phoneno and _idproof and _email and _dob and _projectname and _mouza and _plotno and _plotarea and _ratesqft and _advisoryname and _reference and _bookingdate and _status and request.method == 'POST':
			sqlQuery5 = "INSERT INTO booking(fname, mname, lname, address, city, state, pincode, phoneno, idproof, email, dob, projectname, mouza, plotno, plotarea, ratesqft, advisoryname, reference, bookingdate, status) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
			bindData5 = (_fname, _mname, _lname, _address, _city, _state, _pincode, _phoneno, _idproof, _email, _dob, _projectname, _mouza, _plotno, _plotarea, _ratesqft, _advisoryname, _reference, _bookingdate, _status)
			conn = mysql.connect()
			cursor = conn.cursor(pymysql.cursors.DictCursor)
			cursor.execute(sqlQuery5, bindData5)
			conn.commit()
			response = jsonify("Booking added successfully!")
			response.status_code = 200
			cursor.close()
			conn.close()	
		else:
			response = jsonify("Body not found")
			response.status_code = 400
	except Exception as e:
		print(e)
		response = jsonify("Failed to booking not added")
		response.status_code = 400
	finally:
		return response
		
		

@app.route('/bookings',methods=['GET'])
def book():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM booking")
		bookRows = cursor.fetchall()
		response = json.dumps(bookRows, indent=2)
		response.status_code = 200
		cursor.close()
		conn.close()
		
	except Exception as e:
		print(e)
	finally:
		return response
		

@app.route('/booking/<int:book_id>',methods=['GET'])
def book_details(book_id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM booking WHERE id =%s", book_id)
		bookRow = cursor.fetchone()
		response = json.dumps(bookRow, indent=2)
		return response
		respone.status_code = 200
		cursor.close()
		conn.close()
	except Exception as e:
		print(e)
	finally:
		return response
		
		


@app.route('/updatebooking/<int:book_id>',methods=['PUT'])
def update_book(book_id):
	try:
		_json = request.json
		_fname = _json['fname']
		_mname = _json['mname']
		_lname = _json['lname']
		_address = _json['address']
		_city = _json['city']
		_state = _json['state']
		_pincode = _json['pincode']
		_phoneno = _json['phoneno']
		_idproof = _json['idproof']
		_email = _json['email']
		_dob = _json['dob']
		_projectname = _json['projectname']
		_mouza = _json['mouza']
		_plotno = _json['plotno']
		_plotarea = _json['plotarea']
		_ratesqft = _json['ratesqft']
		_advisoryname = _json['advisoryname']
		_reference = _json['reference']
		_bookingdate = _json['bookingdate']
		_status = _json['status']
		_id = _json['id']
		print(_json)
		if _fname and _mname and _lname and _address and _city and _state and _pincode and _phoneno and _idproof and _email and _dob and _projectname and _mouza and _plotno and _plotarea and _ratesqft and _advisoryname and _reference and _bookingdate and _status and request.method == 'PUT':
			sqlQuery5 = "UPDATE booking SET fname=%s, mname=%s, lname=%s, address=%s, city=%s, state=%s, pincode=%s, phoneno=%s, idproof=%s, email=%s, dob=%s, projectname=%s, mouza=%s, projectname=%s, plotno=%s, plotarea=%s, ratesqft=%s, advisoryname=%s, reference=%s, bookingdate=%s, status=%s WHERE id=%s"
			bindData5 = (_fname, _mname, _lname, _address, _city, _state, _pincode, _phoneno, _idproof, _email, _dob, _projectname, _mouza, _projectname, _plotno, _plotarea, _ratesqft, _advisoryname, _reference, _bookingdate, _status, _id)
			conn = mysql.connect()
			cursor = conn.cursor(pymysql.cursors.DictCursor)
			cursor = conn.cursor()
			cursor.execute(sqlQuery5, bindData5)
			conn.commit()
			response = jsonify("Booking update successfully!")
			response.status_code = 200
			cursor.close()
			conn.close()
		else:
			return showmessage()
	except Exception as e:
		print(e)
	finally:
		return response
		



@app.route('/deletebooking/<int:id>', methods=['DELETE'])
def delete_book(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM booking WHERE id =%s", (id))
		conn.commit()
		response = jsonify('Booking deleted successfully!')
		response.status_code = 200
		return response
		cursor.close()
		conn.close()
		
	except:
		print(e)
	finally:
		return response

@app.errorhandler(404)
def showmessage(error=None):
	message = {
		'status': 404,
		'message': 'Record not found:' + request.url,	
		}
	response = jsonify(message)
	response.status_code = 404
	return response


############################################################# MYTB CRUD #######################################################




@app.route('/createmytb',methods=['POST'])
def create_mytb():
	try:
		_json = request.json
		_uname = _json['uname']
		_password = _json['password']
		_email = _json['email']
		_phone = _json['phone']
		print(_json)
		if _uname and _password and _email and _email and _phone and request.method == 'POST':
			sqlQuery6 = "INSERT INTO mytb(uname, password, email, phone) VALUES(%s, %s, %s, %s)"
			bindData6 = (_uname, _password, _email, _phone)
			conn = mysql.connect()
			cursor = conn.cursor(pymysql.cursors.DictCursor)
			cursor.execute(sqlQuery6, bindData6)
			conn.commit()
			response = jsonify("Mytb added successfully!")
			response.status_code = 200
			cursor.close()
			conn.close()	
		else:
			response = jsonify("Body not found")
			response.status_code = 400
	except Exception as e:
		print(e)
		response = jsonify("Failed to mytb not added")
		response.status_code = 400
	finally:
		return response
		
		

@app.route('/mytbs',methods=['GET'])
def mytb():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM mytb")
		mytbRows = cursor.fetchall()
		response = json.dumps(mytbRows, indent=2)
		response.status_code = 200
		cursor.close()
		conn.close()
		
	except Exception as e:
		print(e)
	finally:
		return response
		

@app.route('/mytb/<int:mytb_id>',methods=['GET'])
def mytb_details(mytb_id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM mytb WHERE id =%s", mytb_id)
		mytbRow = cursor.fetchone()
		response = json.dumps(mytbRow, indent=2)
		return response
		respone.status_code = 200
		cursor.close()
		conn.close()
	except Exception as e:
		print(e)
	finally:
		return response
		
		


@app.route('/updatemytb/<int:mytb_id>',methods=['PUT'])
def update_mytb(mytb_id):
	try:
		_json = request.json
		_uname = _json['uname']
		_password = _json['password']
		_email = _json['email']
		_phone = _json['phone']
		_id = _json['id']
		print(_json)
		if _uname and _password and _email and _phone and request.method == 'PUT':
			sqlQuery6 = "UPDATE mytb SET uname=%s, password=%s, email=%s, phone=%s WHERE id=%s"
			bindData6 = (_uname, _password, _email, _phone, _id)
			conn = mysql.connect()
			cursor = conn.cursor(pymysql.cursors.DictCursor)
			cursor = conn.cursor()
			cursor.execute(sqlQuery6, bindData6)
			conn.commit()
			response = jsonify("Mytbs update successfully!")
			response.status_code = 200
			cursor.close()
			conn.close()
		else:
			return showmessage()
	except Exception as e:
		print(e)
	finally:
		return response
		



@app.route('/deletemytb/<int:id>', methods=['DELETE'])
def delete_mytb(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM mytb WHERE id =%s", (id))
		conn.commit()
		response = jsonify('Mytbs deleted successfully!')
		response.status_code = 200
		return response
		cursor.close()
		conn.close()
		
	except:
		print(e)
	finally:
		return response

@app.errorhandler(404)
def showmessage(error=None):
	message = {
		'status': 404,
		'message': 'Record not found:' + request.url,	
		}
	response = jsonify(message)
	response.status_code = 404
	return response



########################################################  OZEN CRUD #########################################################




@app.route('/createozen',methods=['POST'])
def create_ozen():
	try:
		_json = request.json
		_fname = _json['fname']
		_mname = _json['mname']
		_lname = _json['lname']
		_phonenumber = _json['phonenumber']
		_adharcard = _json['adharcard']
		_email = _json['email']
		_password = _json['password']
		print(_json)
		if _fname and _mname and _lname and _phonenumber and _adharcard and _email and _password and request.method == 'POST':
			sqlQuery7 = "INSERT INTO ozen(fname, mname, lname, phonenumber, adharcard, email, password) VALUES(%s, %s, %s, %s, %s, %s, %s)"
			bindData7 = (_fname, _mname, _lname, _phonenumber, _adharcard, _email, _password)
			conn = mysql.connect()
			cursor = conn.cursor(pymysql.cursors.DictCursor)
			cursor.execute(sqlQuery7, bindData7)
			conn.commit()
			response = jsonify("Ozen added successfully!")
			response.status_code = 200
			cursor.close()
			conn.close()	
		else:
			response = jsonify("Body not found")
			response.status_code = 400
	except Exception as e:
		print(e)
		response = jsonify("Failed to ozen not added")
		response.status_code = 400
	finally:
		return response
		
		

@app.route('/ozens',methods=['GET'])
def ozen():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM ozen")
		ozenRows = cursor.fetchall()
		response = json.dumps(ozenRows, indent=2)
		response.status_code = 200
		cursor.close()
		conn.close()
		
	except Exception as e:
		print(e)
	finally:
		return response
		

@app.route('/ozen/<int:ozen_id>',methods=['GET'])
def ozen_details(plot_id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM ozen WHERE id =%s", ozen_id)
		ozenRow = cursor.fetchone()
		response = json.dumps(ozenRow, indent=2)
		return response
		respone.status_code = 200
		cursor.close()
		conn.close()
	except Exception as e:
		print(e)
	finally:
		return response
		
		


@app.route('/updateozen/<int:ozen_id>',methods=['PUT'])
def update_ozen(ozen_id):
	try:
		_json = request.json
		_fname = _json['fname']
		_mname = _json['mname']
		_lname = _json['lname']
		_phonenumber = _json['phonenumber']
		_adharcard = _json['adharcard']
		_email = _json['email']
		_password = _json['password']
		_id = _json['id']
		print(_json)
		if _fname and _mname and _lname and _phonenumber and _adharcard and _email and _password and request.method == 'PUT':
			sqlQuery7 = "UPDATE ozen SET fname=%s, mname=%s, lname=%s, phonenumber=%s, adharcard=%s, email=%s, password=%s WHERE id=%s"
			bindData7 = (_fname, _mname, _lname, _phonenumber, _adharcard, _email, _password, _id)
			conn = mysql.connect()
			cursor = conn.cursor(pymysql.cursors.DictCursor)
			cursor = conn.cursor()
			cursor.execute(sqlQuery7, bindData7)
			conn.commit()
			response = jsonify("Ozen update successfully!")
			response.status_code = 200
			cursor.close()
			conn.close()
		else:
			return showmessage()
	except Exception as e:
		print(e)
	finally:
		return response
		



@app.route('/deleteozen/<int:id>', methods=['DELETE'])
def delete_ozen(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM ozen WHERE id =%s", (id))
		conn.commit()
		response = jsonify('Ozen deleted successfully!')
		response.status_code = 200
		return response
		cursor.close()
		conn.close()
		
	except:
		print(e)
	finally:
		return response

@app.errorhandler(404)
def showmessage(error=None):
	message = {
		'status': 404,
		'message': 'Record not found:' + request.url,	
		}
	response = jsonify(message)
	response.status_code = 404
	return response





##################################################################   PLOTS CRUD ###################################################


@app.route('/createplt',methods=['POST'])
def create_plt():
	try:
		_json = request.json
		_projectname = _json['projectname']
		_plotno = _json['plotno']
		_plotarea = _json['plotarea']
		_ratesqft = _json['ratesqft']
		print(_json)
		if _projectname and _plotno and _plotarea and _ratesqft and request.method == 'POST':
			sqlQuery8 = "INSERT INTO plots(projectname, plotno, plotarea, ratesqft) VALUES(%s, %s, %s, %s)"
			bindData8 = (_projectname, _plotno, _plotarea, _ratesqft)
			conn = mysql.connect()
			cursor = conn.cursor(pymysql.cursors.DictCursor)
			cursor.execute(sqlQuery8, bindData8)
			conn.commit()
			response = jsonify("Plts added successfully!")
			response.status_code = 200
			cursor.close()
			conn.close()	
		else:
			response = jsonify("Body not found")
			response.status_code = 400
	except Exception as e:
		print(e)
		response = jsonify("Failed to plts not added")
		response.status_code = 400
	finally:
		return response
		
		

@app.route('/plts',methods=['GET'])
def plt():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM plots")
		plotRows = cursor.fetchall()
		response = json.dumps(plotRows, indent=2)
		response.status_code = 200
		cursor.close()
		conn.close()
		
	except Exception as e:
		print(e)
	finally:
		return response
		

@app.route('/plt/<int:plt_id>',methods=['GET'])
def plt_details(plt_id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM plots WHERE id =%s", plt_id)
		pltRow = cursor.fetchone()
		response = json.dumps(pltRow, indent=2)
		return response
		respone.status_code = 200
		cursor.close()
		conn.close()
	except Exception as e:
		print(e)
	finally:
		return response
		
		


@app.route('/updateplt/<int:plt_id>',methods=['PUT'])
def update_plt(plt_id):
	try:
		_json = request.json
		_projectname = _json['projectname']
		_plotno = _json['plotno']
		_plotarea = _json['plotarea']
		_ratesqft = _json['ratesqft']
		_id = _json['id']
		print(_json)
		if _projectname and _plotno and _plotarea and _ratesqft and request.method == 'PUT':
			sqlQuery8 = "UPDATE plots SET projectname=%s, plotno=%s, plotarea=%s, ratesqft=%s WHERE id=%s"
			bindData8 = (_projectname, _plotno, _plotarea, _ratesqft, _id)
			conn = mysql.connect()
			cursor = conn.cursor(pymysql.cursors.DictCursor)
			cursor = conn.cursor()
			cursor.execute(sqlQuery8, bindData8)
			conn.commit()
			response = jsonify("Plots update successfully!")
			response.status_code = 200
			cursor.close()
			conn.close()
		else:
			return showmessage()
	except Exception as e:
		print(e)
	finally:
		return response
		



@app.route('/deleteplt/<int:id>', methods=['DELETE'])
def delete_plt(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM plots WHERE id =%s", (id))
		conn.commit()
		response = jsonify('Plots deleted successfully!')
		response.status_code = 200
		return response
		cursor.close()
		conn.close()
		
	except:
		print(e)
	finally:
		return response

@app.errorhandler(404)
def showmessage(error=None):
	message = {
		'status': 404,
		'message': 'Record not found:' + request.url,	
		}
	response = jsonify(message)
	response.status_code = 404
	return response



#################################################### ADDteam CRUD #####################################################



@app.route('/createteam',methods=['POST'])
def create_team():
	try:
		_json = request.json
		_teamname = _json['teamname']
		_teamleader = _json['teamleader']
		_teammembers = _json['teammembers']
		print(_json)
		if _teamname and _teamleader and _teammembers and request.method == 'POST':
			sqlQuery9 = "INSERT INTO team(teamname, teamleader, teammembers) VALUES(%s, %s, %s)"
			bindData9 = (_teamname, _teamleader, _teammembers)
			conn = mysql.connect()
			cursor = conn.cursor(pymysql.cursors.DictCursor)
			cursor.execute(sqlQuery9, bindData9)
			conn.commit()
			response = jsonify("Team and Team members added successfully!")
			response.status_code = 200
			cursor.close()
			conn.close()	
		else:
			response = jsonify("Body not found")
			response.status_code = 400
	except Exception as e:
		print(e)
		response = jsonify("Failed to teams not added")
		response.status_code = 400
	finally:
		return response
		
		

@app.route('/teams',methods=['GET'])
def team():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM team")
		teamRows = cursor.fetchall()
		response = json.dumps(teamRows, indent=2)
		response.status_code = 200
		cursor.close()
		conn.close()
		
	except Exception as e:
		print(e)
	finally:
		return response
		

@app.route('/team/<int:team_id>',methods=['GET'])
def team_details(team_id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM team WHERE id =%s", team_id)
		teamRow = cursor.fetchone()
		response = json.dumps(teamRow, indent=2)
		return response
		respone.status_code = 200
		cursor.close()
		conn.close()
	except Exception as e:
		print(e)
	finally:
		return response
		
		


@app.route('/updateteam/<int:team_id>',methods=['PUT'])
def update_team(team_id):
	try:
		_json = request.json
		_teamname = _json['teamname']
		_teamleader = _json['teamleader']
		_teammembers = _json['teammembers']
		_id = _json['id']
		print(_json)
		if _teamname and _teamleader and _teammembers and request.method == 'PUT':
			sqlQuery9 = "UPDATE team SET teamname=%s, teamleader=%s, teammembers=%s WHERE id=%s"
			bindData9 = (_teamname, _teamleader, _teammembers, _id)
			conn = mysql.connect()
			cursor = conn.cursor(pymysql.cursors.DictCursor)
			cursor = conn.cursor()
			cursor.execute(sqlQuery9, bindData9)
			conn.commit()
			response = jsonify("Team and team members update successfully!")
			response.status_code = 200
			cursor.close()
			conn.close()
		else:
			return showmessage()
	except Exception as e:
		print(e)
	finally:
		return response
		



@app.route('/deleteteam/<int:id>', methods=['DELETE'])
def delete_team(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM team WHERE id =%s", (id))
		conn.commit()
		response = jsonify('Team deleted successfully!')
		response.status_code = 200
		return response
		cursor.close()
		conn.close()
		
	except:
		print(e)
	finally:
		return response

@app.errorhandler(404)
def showmessage(error=None):
	message = {
		'status': 404,
		'message': 'Record not found:' + request.url,	
		}
	response = jsonify(message)
	response.status_code = 404
	return response


################################################### VISITORS CRUD ###############################################3



@app.route('/createvisitor',methods=['POST'])
def create_visitor():
	try:
		_json = request.json
		_nameofvisitor = _json['nameofvisitor']
		_address = _json['address']
		_city = _json['city']
		_state = _json['state']
		_pin = _json['pin']
		_mobileno = _json['mobileno']
		_dateofvisit = _json['dateofvisit']
		_projectname = _json['projectname']
		_nameofadvisory = _json['nameofadvisory']
		_plotno = _json['plotno']
		print(_json)
		if _nameofvisitor and _address and _city and _state and _pin and _mobileno and _dateofvisit and _projectname and _nameofadvisory and _plotno and request.method == 'POST':
			sqlQuery10 = "INSERT INTO visitors(nameofvisitor, address, city, state, pin, mobileno, dateofvisit, projectname, nameofadvisory, plotno) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
			bindData10 = (_nameofvisitor, _address, _city, _state, _pin, _mobileno, _dateofvisit, _projectname, _nameofadvisory, _plotno)
			conn = mysql.connect()
			cursor = conn.cursor(pymysql.cursors.DictCursor)
			cursor.execute(sqlQuery10, bindData10)
			conn.commit()
			response = jsonify("Visitors added successfully!")
			response.status_code = 200
			cursor.close()
			conn.close()	
		else:
			response = jsonify("Body not found")
			response.status_code = 400
	except Exception as e:
		print(e)
		response = jsonify("Failed to visitors not added")
		response.status_code = 400
	finally:
		return response
		
		

@app.route('/visitors',methods=['GET'])
def visitor():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM visitors")
		visitorRows = cursor.fetchall()
		response = json.dumps(visitorRows, indent=2)
		response.status_code = 200
		cursor.close()
		conn.close()
		
	except Exception as e:
		print(e)
	finally:
		return response
		

@app.route('/visitor/<int:visitor_id>',methods=['GET'])
def visitor_details(visitor_id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM visitors WHERE id =%s", visitor_id)
		visitorRow = cursor.fetchone()
		response = json.dumps(visitorRow, indent=2)
		return response
		respone.status_code = 200
		cursor.close()
		conn.close()
	except Exception as e:
		print(e)
	finally:
		return response
		
		


@app.route('/updatevisitor/<int:visitor_id>',methods=['PUT'])
def update_visitor(visitor_id):
	try:
		_json = request.json
		_nameofvisitor = _json['nameofvisitor']
		_address = _json['address']
		_city = _json['city']
		_state = _json['state']
		_pin = _json['pin']
		_mobileno = _json['mobileno']
		_dateofvisit = _json['dateofvisit']
		_projectname = _json['projectname']
		_nameofadvisory = _json['nameofadvisory']
		_plotno = _json['plotno']
		_id = _json['id']
		print(_json)
		if _nameofvisitor and _address and _city and _state and _pin and _mobileno and _dateofvisit and _projectname and _nameofadvisory and _plotno and request.method == 'PUT':
			sqlQuery = "UPDATE visitors SET nameofvisitor=%s, address=%s, city=%s, state=%s, pin=%s, mobileno=%s, dateofvisit=%s, projectname=%s, nameofadvisory=%s, plotno=%s WHERE id=%s"
			bindData = (_nameofvisitor, _address, _city, _state, _pin, _mobileno, _dateofvisit, _projectname, _nameofadvisory, _plotno, _id)
			conn = mysql.connect()
			cursor = conn.cursor(pymysql.cursors.DictCursor)
			cursor = conn.cursor()
			cursor.execute(sqlQuery, bindData)
			conn.commit()
			response = jsonify("visitor update successfully!")
			response.status_code = 200
			cursor.close()
			conn.close()
		else:
			return showmessage()
	except Exception as e:
		print(e)
	finally:
		return response
		



@app.route('/deletevisitor/<int:id>', methods=['DELETE'])
def delete_visitor(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM visitors WHERE id =%s", (id))
		conn.commit()
		response = jsonify('Visitors deleted successfully!')
		response.status_code = 200
		return response
		cursor.close()
		conn.close()
		
	except:
		print(e)
	finally:
		return response

@app.errorhandler(404)
def showmessage(error=None):
	message = {
		'status': 404,
		'message': 'Record not found:' + request.url,	
		}
	response = jsonify(message)
	response.status_code = 404
	return response


if __name__ == "__main__":
	app.run(debug=True)






	