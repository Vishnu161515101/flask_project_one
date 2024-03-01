from flask import Flask,redirect 
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
        return "<script>alert('success'); window.location.href = '/vishnu1';</script>"
        # return redirect("/vishnu1")

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
                data_with_serial = [(i+1, item) for i, item in enumerate(data)]
                return render_template('report.html',d=data_with_serial)
                # return 'succefully inserted'

            except Exception:
                return "error is accure"
                # return fname+' '+Number+' '+Id_e  
            


@app.route("/edit/<num>")
def edit(num):
            #edit_no=request.form['num']
            # return num
            try:
                db_mysql=pymysql.connect(host='localhost',user='root',password='',db='vishnu')
                db1=db_mysql.cursor()
                sql1="select * from flask_table where id={}".format(num)
                db1.execute(sql1)
                data=db1.fetchall()
                data_with_serial = [(i+1, item) for i, item in enumerate(data)]
                return render_template('edit_templates.html',d=data_with_serial)
                # return num

            except Exception:
                return "error is accure"
                # return fname+' '+Number+' '+Id_e  


@app.route("/update" ,methods=["POST"])
def update():
    fname=request.form['f_name']
    Number=request.form['Number']
    Id_e=request.form['Id_e']
    Id_e2=request.form['Id_e1']
    try:
        db_mysql=pymysql.connect(host='localhost',user='root',password='',db='vishnu')
        db1=db_mysql.cursor()
        sql="update flask_table set name='{}',number='{}',id_f='{}' where id='{}'".format(fname,Number,Id_e,Id_e2)
        db1.execute(sql)
        db_mysql.commit()
        # return '<script>alert("Date Updated success"); window.location.href = "/report";</script>'
        return "<script>alert('Date Updated success'); window.location.href = '/report';</script>"
        # return 'succefully Updated
        # '
        # return redirect("/report")
        # return sql

    except Exception:
        return "error is accure"
    # return fname+' '+Number+' '+Id_e



@app.route("/delete/<num>")
def delete(num):
            #edit_no=request.form['num']
            # return num
            try:
                db_mysql=pymysql.connect(host='localhost',user='root',password='',db='vishnu')
                db1=db_mysql.cursor()
                sql1="delete from flask_table where id={}".format(num)
                db1.execute(sql1)
                db_mysql.commit()
                return "<script>alert('Data Deleted success'); window.location.href = '/report';</script>"
                # return num

            except Exception:
                return "error is accure"


if __name__== '__main__':
    app.run(debug=True)