from flask import Flask
app=Flask(__name__)

@app.route('/ping')
def ping():
    print("Hello")
    return "ping called"
if __name__=='__main':
    app.run(debug=True)