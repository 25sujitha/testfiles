from flask import Flask, request,jsonify
import sqlite3
from Flask_Caching import Cache

app=Flask(__name__)
app.config['CACHE_TYPE'] = 'simple'
cache=Cache(app)
@app.route('/save', methods=['POST'])
def savedata():
    try:
        key=request.json['key']
        value=request.json['value']

        cache_data=cache.get(key)
        if cache_data is not None:
            return jsonify({"message":"Data already saved"})
        con=sqlite3.connect('datatry.db')
        cursor=con.cursor()
        query='INSERT INTO datatable (key, value) VALUES (?,?)', (key,value)
        cursor.execute(query)
        con.commit()
        con.close()
        cache.set(key,value)
        return jsonify({'message':"Data saved success"})
    except Exception as e:
        return jsonify({'error': str(e)}),500

@app.route('/getdata', methods=['GET'])
def getdata():
    try:
        key=request.args.get('key')
        cached_data=cache.get(key)
        if cached_data is not None:
            return jsonify({'data':cached_data,'source':'cache'})

        con=sqlite3.connect('datatry.db')
        cursor=con.cursor()
        query='SELECT * FROM datatable'
        cursor.execute(query)
        data=cursor.fetchone()
        con.commit()
        con.close()
        if data:
            data=data[0]
            cache.set(key,data)
        return jsonify({'data':data,'source':'database'})
    except Exception as e:
        return jsonify({'error': str(e)}),500
