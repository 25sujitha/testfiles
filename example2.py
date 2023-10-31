from flask import Flask, request, jsonify

app=Flask(__name__)
secrets={
    "token1": "key1",
    "token2": "key2" }

@app.route('/authorize', methods=['POST'])
def authorize():
    auth_token=request.headers.get('Authorization')

    if auth_token:
        if auth_token in secrets:
            return jsonify({"message":"Authorization success"})
    return jsonify({"mesage":"Authorization failed"})
if __name__=='__main':
    app.run(debug=True)