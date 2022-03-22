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



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',threaded=True,port=5000)
