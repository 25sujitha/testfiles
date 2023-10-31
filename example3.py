from flask import Flask, request, jsonify
import sqlite3

app=Flask(__name__)

@app.route('/save', methods=['POST'])
def savedata():
    try:
        key=request.json['key']
        value=request.json['value']
        con=sqlite3.connect('datatry.db')
        cursor=con.cursor()
        query='INSERT INTO datatable (key, value) VALUES (?,?)', (key,value)
        cursor.execute(query)
        con.commit()
        con.close()
        return jsonify({'message':"Data saved success"})
    except Exception as e:
        return jsonify({'error': str(e)}),500
    
@app.route('/getdata', methods=['GET'])
def getdata():
    try:
        
        con=sqlite3.connect('datatry.db')
        cursor=con.cursor()
        query='SELECT * FROM datatable'
        cursor.execute(query)
        data=cursor.fetchall()
        con.commit()
        con.close()
        return jsonify({'data':data,'source':'database'})
    except Exception as e:
        return jsonify({'error': str(e)}),500

@app.route('/delete', methods=['POST'])
def deletedata():
    try:
        key=request.json['key']
        
        con=sqlite3.connect('datatry.db')
        cursor=con.cursor()
        query='DELETE FROM datatable WHERE key=?',(key)
        cursor.execute(query)
        con.commit()
        con.close()
        return jsonify({'message':"Data deleted successfully"})
    except Exception as e:
        return jsonify({'error': str(e)}),500
if __name__=='__main':
    app.run(debug=True)
