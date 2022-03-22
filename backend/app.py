from dbConfig import *

@app.route('/addPending', methods=['POST'])
@connect_sql()
def addPending(cursor):
    data = request.json
    print("data =",data)
    title = data['title']
    description = data['description']
    information = data['information']
    timestamp = data['timestamp']
    update = data["update"]
    staus = data["staus"]
    sql =   """
            INSERT INTO nipa(title,description,information,timestamps,updates,staus) VALUES (%s, %s, %s, %s, %s, %s)
            """
    cursor.execute(sql,(title,description,information,timestamp,update,staus))
    return 'success'

@app.route('/getuser', methods=['GET'])
@connect_sql()
def getuser(cursor):
    sql = "SELECT * FROM nipa "
    cursor.execute(sql)
    columns = [column[0] for column in cursor.description]
    print(columns)
    result = toJson(cursor.fetchall(),columns)
    if result:
        return jsonify(result)
    else:
        return jsonify(None)

@app.route('/getAccepted', methods=['GET'])
@connect_sql()
def getAccepted(cursor):
    sql = "SELECT * FROM nipaaccepted "
    cursor.execute(sql)
    columns = [column[0] for column in cursor.description]
    print(columns)
    result = toJson(cursor.fetchall(),columns)
    if result:
        return jsonify(result)
    else:
        return jsonify(None)

@app.route('/getResolved', methods=['GET'])
@connect_sql()
def getResolved(cursor):
    sql = "SELECT * FROM nipa WHERE staus = 'Resolved'"
    cursor.execute(sql)
    columns = [column[0] for column in cursor.description]
    result = toJson(cursor.fetchall(),columns)
    if result:
        return jsonify(result)
    else:
        return jsonify(None)

@app.route('/getRejected', methods=['GET'])
@connect_sql()
def getRejected(cursor):
    sql = "SELECT * FROM niparejected "
    cursor.execute(sql)
    columns = [column[0] for column in cursor.description]
    print(columns)
    result = toJson(cursor.fetchall(),columns)
    if result:
        return jsonify(result)
    else:
        return jsonify(None)

@app.route('/rejected', methods=['POST'])
@connect_sql()
def rejected(cursor):
    data = request.json
    print("data =",data)
    title = data['title']
    description = data['description']
    information = data['information']
    timestamp = data['timestamps']
    update = data["updates"]
    staus = "Rejected"
    sql =   """
            INSERT INTO niparejected(title,description,information,timestamps,updates,staus) VALUES (%s, %s, %s, %s, %s, %s)
            """
    cursor.execute(sql,(title,description,information,timestamp,update,staus))
    return 'success'

@app.route('/editTicket', methods=['POST'])
@connect_sql()
def editTicket(cursor):
    data = request.json
    print(data)
    title = data['title']
    description = data['description']
    information = data['information']
    timestamp = data['timestamps']
    update = data['updates']
    staus = data['staus']
    id = data['id']
    sql = """
            UPDATE nipa SET title = %s, description = %s, information = %s, timestamps = %s, updates = %s, staus = %s WHERE nipa.id = %s
          """
    cursor.execute(sql,(title,description,information,timestamp,update,staus,id))
    return 'success'

@app.route('/accepted', methods=['POST'])
@connect_sql()
def accepted(cursor):
    data = request.json
    print("data =",data)
    title = data['title']
    description = data['description']
    information = data['information']
    timestamp = data['timestamps']
    update = data["updates"]
    staus = "Accepted"
    sql =   """
            INSERT INTO nipaaccepted(title,description,information,timestamps,updates,staus) VALUES (%s, %s, %s, %s, %s, %s)
            """
    cursor.execute(sql,(title,description,information,timestamp,update,staus))
    return 'success'

@app.route('/deletePending/<id>', methods=['DELETE'])
@connect_sql()
def deletePending(cursor,id):
    data = request.json
    print("data =",data)
    print("id =",id)
    sql =   "DELETE FROM nipa WHERE id = %s"
    cursor.execute(sql,(id))
    return 'deletePending'

# @app.route('/test', methods=['POST'])
# @connect_sql()
# def test(cursor):
#     data = request.json
#     print("data =",data)
#     title = data['title']
#     description = data['description']
#     information = data['information']
#     timestamp = data['timestamp']
#     update = data["update"]
#     sql =   "INSERT INTO nipa(title,description,information,timestamps,updates) VALUES ('" + title + "','" + description + "','" + information + "','" + timestamp + "','" + update + "')"
#     print(sql)
#     cursor.execute(sql)
#     return 'success'


# @app.route('/hello/<email>/<password>', methods=['GET'])
# @connect_sql()
# def hello(cursor, email, password):
#     sql = "SELECT * FROM userdb WHERE email = %s AND password = %s "
#     cursor.execute(sql,(email, password))
#     columns = [column[0] for column in cursor.description]
#     result = toJson(cursor.fetchall(),columns)
#     if result:
#         return jsonify(result)
#     else:
#         return jsonify(None)

# @app.route('/getuser', methods=['GET'])
# @connect_sql()
# def getuser(cursor):
#     sql = "SELECT * FROM userdb "
#     cursor.execute(sql)
#     columns = [column[0] for column in cursor.description]
#     print(columns)
#     result = toJson(cursor.fetchall(),columns)
#     if result:
#         return jsonify(result)
#     else:
#         return jsonify(None)

# @app.route('/adduser', methods=['POST'])
# @connect_sql()
# def adduser(cursor):
#     data = request.json
#     print("data =",data)
#     email = data['email']
#     password = data['password']
#     name = data['name']
#     department = data['department']
#     tel = data['tel']
#     role = data['role']
#     sql =   """
#             INSERT INTO userdb(email,password,name,department,tel,role) 
#             VALUES (%s, %s, %s, %s, %s, %s) 
#             """
#     cursor.execute(sql,(email,password,name,department,tel,role))
#     return 'success'

# @app.route('/find/<email>', methods=['GET'])
# @connect_sql()
# def find(cursor, email):
#     sql = "SELECT * FROM userdb WHERE email = %s"
#     cursor.execute(sql,(email))
#     columns = [column[0] for column in cursor.description]
#     result = toJson(cursor.fetchall(),columns)
#     if result:
#         return jsonify(result)
#     else:
#         return jsonify(None)

# @app.route('/delete/<Id>', methods=['DELETE'])
# @connect_sql()
# def delete(cursor, Id):
#     sql = "DELETE FROM userdb WHERE Id = %s"
#     cursor.execute(sql,(Id))
#     return 'success'

# @app.route('/edituser', methods=['POST'])
# @connect_sql()
# def edituser(cursor):
#     dataedit = request.json
#     print(dataedit)
#     email = dataedit['email']
#     password = dataedit['password']
#     name = dataedit['name']
#     department = dataedit['department']
#     tel = dataedit['tel']
#     role = dataedit['role']
#     Id = dataedit['Id']
#     sql = """
#             UPDATE userdb SET email = %s, password = %s, name = %s, department = %s, tel = %s, role = %s WHERE userdb.Id = %s
#           """
#     cursor.execute(sql,(email,password,name,department,tel,role,Id))
#     return 'success'

# @app.route('/getoder', methods=['GET'])
# @connect_sql()
# def getoder(cursor):
#     sql = "SELECT * FROM oderdb "
#     cursor.execute(sql)
#     columns = [column[0] for column in cursor.description]
#     result = toJson(cursor.fetchall(),columns)
#     if result:
#         return jsonify(result)
#     else:
#         return jsonify(None)

# @app.route('/youroder/<Id>', methods=['GET'])
# @connect_sql()
# def youroder(cursor,Id):
#     sql = "SELECT * FROM historydb WHERE Id = %s"
#     cursor.execute(sql,(Id))
#     columns = [column[0] for column in cursor.description]
#     result = toJson(cursor.fetchall(),columns)
#     if result:
#         return jsonify(result)
#     else:
#         return jsonify(None)

# @app.route('/addoder', methods=['POST'])
# @connect_sql()
# def addoder(cursor):
#     packdata = request.json
#     name = packdata['name']
#     nameoder = packdata['nameoder']
#     count = packdata['count']
#     days = packdata['days']
#     Id = packdata['Id']
#     sql =   """
#             INSERT INTO listoder(name,nameoder,count,days,Id) 
#             VALUES (%s, %s, %s, %s, %s) 
#             """
#     cursor.execute(sql,(name,nameoder,count,days,Id))
#     return 'success'

# @app.route('/getoderall', methods=['GET'])
# @connect_sql()
# def getoderall(cursor):
#     sql = "SELECT * FROM listoder"
#     cursor.execute(sql)
#     columns = [column[0] for column in cursor.description]
#     result = toJson(cursor.fetchall(),columns)
#     if result:
#         return jsonify(result)
#     else:
#         return jsonify(None)

# @app.route('/deleteoder/<oderid>', methods=['DELETE'])
# @connect_sql()
# def deleteoder(cursor, oderid):
#     sql = "DELETE FROM listoder WHERE oderid = %s"
#     cursor.execute(sql,(oderid))
#     return 'success'

# @app.route('/addhistory', methods=['POST'])
# @connect_sql()
# def addhistory(cursor):
#     datapreoder = request.json
#     oderid = datapreoder['oderid']
#     name = datapreoder['name']
#     nameoder = datapreoder['nameoder']
#     count = datapreoder['count']
#     days = datapreoder['days']
#     Id = datapreoder['Id']
#     sql =   """
#             INSERT INTO historydb(oderid,name,nameoder,count,days,Id) 
#             VALUES (%s, %s, %s, %s, %s, %s) 
#             """
#     cursor.execute(sql,(oderid,name,nameoder,count,days,Id))
#     return 'success'
    
# @app.route('/getdataproduct/<nameoder>', methods=['GET'])
# @connect_sql()
# def getdataduct(cursor, nameoder):
#     sql = "SELECT * FROM oderdb WHERE nameoder = %s"
#     cursor.execute(sql,(nameoder))
#     columns = [column[0] for column in cursor.description]
#     result = toJson(cursor.fetchall(),columns)
#     if result:
#         return jsonify(result)
#     else:
#         return jsonify(None)

# @app.route('/editproduct', methods=['POST'])
# @connect_sql()
# def editproduct(cursor):
#     aaa = request.json
#     countproduct = aaa['countproduct']
#     Idoder = aaa['Idoder']
#     sql = """
#             UPDATE oderdb SET countproduct = %s WHERE oderdb.Idoder = %s
#           """
#     cursor.execute(sql,(countproduct,Idoder))
#     return 'success'

# @app.route('/addcount', methods=['POST'])
# @connect_sql()
# def addcount(cursor):
#     aaa = request.json
#     countproduct = aaa['countproduct']
#     Idoder = aaa['Idoder']
#     sql = """
#             UPDATE oderdb SET countproduct = %s WHERE oderdb.Idoder = %s
#           """
#     cursor.execute(sql,(countproduct,Idoder))
#     return 'success'

# @app.route('/getyouroder/<Id>', methods=['GET'])
# @connect_sql()
# def getyouroder(cursor,Id):
#     sql = "SELECT * FROM listoder WHERE Id = %s"
#     cursor.execute(sql,(Id))
#     columns = [column[0] for column in cursor.description]
#     result = toJson(cursor.fetchall(),columns)
#     if result:
#         return jsonify(result)
#     else:
#         return jsonify(None)

# @app.route('/getid2/<idstudent2>', methods=['GET'])
# @connect_sql()
# def getid2(cursor,idstudent2):
#     sql = "SELECT * FROM userdbided WHERE idstudent2 = %s"
#     cursor.execute(sql,(idstudent2))
#     columns = [column[0] for column in cursor.description]
#     result = toJson(cursor.fetchall(),columns)
#     if result:
#         return jsonify(result)
#     else:
#         return jsonify(None)

# @app.route('/findmoney/<lineid>', methods=['GET'])
# @connect_sql()
# def findmoney(cursor, lineid):
#     sql = "SELECT * FROM userdbided WHERE lineid = %s"
#     cursor.execute(sql,(lineid))
#     columns = [column[0] for column in cursor.description]
#     result = toJson(cursor.fetchall(),columns)
#     print(result)
#     if result:
#         return jsonify(result)
#     else:
#         return jsonify(None)
    
# @app.route('/findlineid/<idstudent>', methods=['GET'])
# @connect_sql()
# def findlineid(cursor, idstudent):
#     sql = "SELECT * FROM userdbided WHERE idstudent = %s"
#     cursor.execute(sql,(idstudent))
#     columns = [column[0] for column in cursor.description]
#     result = toJson(cursor.fetchall(),columns)
#     print(result)
#     if result:
#         return jsonify(result)
#     else:
#         return jsonify(None)

# @app.route('/AddIdLine', methods=['POST'])
# @connect_sql()
# def AddIdLine(cursor):
#     datasend = request.json
#     lineid = datasend['userlineid']
#     idstudent = datasend['idstudent']
#     print(datasend)
#     print(lineid)
#     print(idstudent)
#     sql = """
#             UPDATE userdbided SET lineid = %s WHERE userdbided.idstudent = %s
#           """
#     cursor.execute(sql,(lineid,idstudent))
#     return 'success'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',threaded=True,port=5000)
