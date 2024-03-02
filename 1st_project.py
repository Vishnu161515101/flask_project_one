from flask import Flask,redirect 
from flask import render_template 
from flask import request
import pymysql
import pandas as pd



app = Flask(__name__)  

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# Create a single time database connection object
db_mysql = pymysql.connect(host='localhost', user='root', password='', db='vishnu')

# Create a cursor object from the connection
db_cursor = db_mysql.cursor()


# @app.route("/data_conncetion")
# def data_conncetion():
#      db=pymysql.connect(host='localhost',user='root',password='',db='vishnu')
#      db1=db.cursor()

@app.route("/dashboard")
def dashboard():
     return render_template('dashboard.html')

@app.route("/vishnu")
def vishnu():
    return "hello vishnu vardhan how are you"


@app.route("/vishnu1")
def vishnu1():
     return render_template('1st_templates.html')


@app.route("/employee_entry")
def employee_entry():
     return render_template('employee_entry_page.html')


@app.route("/upload_data1")
def upload_data1():
     return render_template('upload_data.html')




@app.route("/store" ,methods=["POST"])
def store():
    fname=request.form['f_name']
    Number=request.form['Number']
    Id_e=request.form['Id_e']
    try:
        
        sql="insert into flask_table(name,number,id_f)values('{}','{}','{}')".format(fname,Number,Id_e)
        db_cursor.execute(sql)
        db_mysql.commit()
        return "<script>alert('success'); window.location.href = '/vishnu1';</script>"
        # return redirect("/vishnu1")

    except Exception:
        return "error is accure"
    # return fname+' '+Number+' '+Id_e
    
 
@app.route("/report")
def report():
            try:
              
                sql1="select * from flask_table"
                db_cursor.execute(sql1)
                data=db_cursor.fetchall()
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
                
                sql1="select * from flask_table where id={}".format(num)
                db_cursor.execute(sql1)
                data=db_cursor.fetchall()
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
        
        sql="update flask_table set name='{}',number='{}',id_f='{}' where id='{}'".format(fname,Number,Id_e,Id_e2)
        db_cursor.execute(sql)
        db_mysql.commit()
        # return '<script>alert("Date Updated success"); window.location.href = "/report";</script>'
        return "<script>alert('Data Updated success'); window.location.href = '/report';</script>"
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
                
                sql1="delete from flask_table where id={}".format(num)
                db_cursor.execute(sql1)
                db_mysql.commit()
                return "<script>alert('Data Deleted success'); window.location.href = '/report';</script>"
                # return num

            except Exception:
                return "error is accure"


@app.route("/employee_store",methods=['POST'])
def employee_store():
    #  return  'successfull'
     
     f_name=request.form['f_name']
     S_name=request.form['S_name']
     T_name=request.form['T_name']
     Id_e=request.form['Id_e']
     department=request.form['department']
     try:
       
        sql="insert into all_the_employee_name(fname,mname,lname,empl_ids,department)values('{}','{}','{}','{}','{}')".format(f_name,S_name,T_name,Id_e,department)
        db_cursor.execute(sql)
        db_mysql.commit()
        return "<script>alert('data succefully connectd');window.location.href='/employee_entry';</script>"
     except Exception:
                return "error is accure"
     
@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            # Read Excel file into a DataFrame
           
                df = pd.read_excel(file)
                 # Access columns by index using iloc method
                column1_index = 0  # Index of Column1
                column2_index = 1  # Index of Column2
                column3_index = 2  # Index of Column3
                
                # Get column values as separate variables
                column1 = df.iloc[:, column1_index].tolist()
                column2 = df.iloc[:, column2_index].tolist()
                column3 = df.iloc[:, column3_index].tolist()
                
                #Concatenate values from the columns
                concatenated_values = column1 + column2 + column3
                # sql="insert into all_the_employee_name(fname,mname,lname)values('{}','{}','{}')".format(column1,column2,column3)
                return concatenated_values
                # return f"Column 1: {column1}"
        
                # return str(concatenated_values)  # Convert to string to return as response
    return 'No file uploaded or something went wrong.'


if __name__== '__main__':
    app.run(debug=True)