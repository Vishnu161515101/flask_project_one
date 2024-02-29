from flask import Flask 
from flask import render_template 
from flask import request
import pymysql



app = Flask(__name__)  

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"



@app.route("/vishnu")
def vishnu():
    return "hello vishnu vardhan how are you"


@app.route("/vishnu1")
def vishnu1():
     return render_template('1st_templates.html')


@app.route("/store" ,methods=["POST"])
def store():
    fname=request.form['f_name']
    Number=request.form['Number']
    Id_e=request.form['Id_e']
    try:
        db_mysql=pymysql.connect(host='localhost',user='root',password='',db='vishnu')
        db1=db_mysql.cursor()
        sql="insert into flask_table(name,number,id_f)values('{}','{}','{}')".format(fname,Number,Id_e)
        db1.execute(sql)
        db_mysql.commit()
        return 'succefully inserted'

    except Exception:
        return "error is accure"
    # return fname+' '+Number+' '+Id_e
    
 
@app.route("/report")
def report():
            try:
                db_mysql=pymysql.connect(host='localhost',user='root',password='',db='vishnu')
                db1=db_mysql.cursor()
                sql1="select * from flask_table"
                db1.execute(sql1)
                data=db1.fetchall()
                return render_template('reprot.html',d=data)
                # return 'succefully inserted'

            except Exception:
                return "error is accure"
                # return fname+' '+Number+' '+Id_e  

if __name__== '__main__':
    app.run(debug=True)