from flask import Flask
app = Flask(__name__)

def mysql_test():
    import mysql.connector
    mysql.connector.connect(host='database',database='mysql',user='root',password='root')

@app.route('/')
def hello_world():
    mysql_test()
    return 'Flask Dockerized'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)