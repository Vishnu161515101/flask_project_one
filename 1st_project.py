from flask import Flask,redirect 
from flask import render_template 
from flask import request
import pymysql
import pandas as pd
import bcrypt
import re


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
     
# @app.route('/upload', methods=['POST'])
# def upload():
#     if request.method == 'POST':
#         print(request.files['file'])
#         f = request.files['file']
#         data_xls = pd.read_excel(f)
#         return data_xls.to_html()

# @app.route('/upload', methods=['POST'])
# def upload():
#     if request.method == 'POST':
#         file = request.files['file']
#         if file:
#             # Read Excel file into a DataFrame
#             df = pd.read_excel(file)
            
#             column1_value = row['Column1'].strip()
            
#             # Iterate over rows in the DataFrame and insert data into the database
#             for index, row in df.iterrows():
#                  return  row['column1_value']
            
              
            
#             return 'Data inserted successfully into the database.'
    
#     return 'No file uploaded or something went wrong.'

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            # Read Excel file into a DataFrame
            df = pd.read_excel(file)
            
            # Iterate over rows in the DataFrame
            for index, row in df.iterrows():
                #  result = "The value is: " + row
                 result1 = "The value is: " + str(index)
                 return result1
                # Access and assign values from each row to variables
                # column1_value = row['Column1']
                # column2_value = row['Column2']
                # column3_value = row['Column3']
                # # Continue with other columns as needed
                
                # # Print or use the assigned values as needed
                # print(f"Row {index + 1}: Column1={column1_value}, Column2={column2_value}, Column3={column3_value}")
                
                # You can also use these values to perform further processing
                
            # return 'Data printed successfully.'
    
    return 'No file uploaded or something went wrong.'

@app.route("/Register")
def Register():
    #  return 'this is Register from'
     return render_template('registoer_from.html')



#----------------------this main code i am doing --------------------
# @app.route("/create_user_name",methods=['POST'])
# def create_user_name():
     
#     #  return 'this is create_user_name'
#      Name=request.form['f_name']
#      Email=request.form['E_mail']
#      Password=request.form['Passwordss']
#      password1 = Password
#      hashed_password = bcrypt.hashpw(password1.encode('utf-8'), bcrypt.gensalt())
    
#      try:
        
 
#     #  except Exception:
#     #       return 'it has been filed'
#         db_cursor.execute("SELECT email_id FROM login WHERE email_id = '{}'".format(Email))
#         user = db_cursor.fetchone()
#         if user:
#                 # data = user[0] 
#                 # return data
#                 return "<script>alert('Already Email Id Execisted please try another email id');window.location.href='/Register';</script>"
#         else:
#             sql = "INSERT INTO login (name, email_id, password) VALUES (%s, %s, %s)"
#             # Execute the SQL query with parameters
#             db_cursor.execute(sql, (Name, Email, hashed_password.decode('utf-8')))
#             # Commit the changes
#             db_mysql.commit()
#             return "<script>alert('data succefully connectd');window.location.href='/Register';</script>"
#      except Exception as e:
#         # Log the exception for debugging purposes
#         print("An error occurred:", str(e))
#         # You can also raise the exception to propagate it further
#         # raise
#         return 'An error occurred: {}'.format(str(e))

@app.route("/create_user_name",methods=['POST'])
def create_user_name():
     
    #  return 'this is create_user_name'
     Name=request.form['f_name']
     Email=request.form['E_mail']
     Password=request.form['Passwordss']
     password1 = Password
     hashed_password = bcrypt.hashpw(password1.encode('utf-8'), bcrypt.gensalt())

     try:
        db_cursor.execute("SELECT email_id FROM login WHERE email_id = '{}'".format(Email))
        user = db_cursor.fetchone()
        if user:
                data = user[0] 
                return data
                # return "<script>alert('Already Email Id Execisted please try another email id');window.location.href='/Register';</script>"
        else:
            sql = "INSERT INTO login (name, email_id, password) VALUES (%s, %s, %s)"
            # Execute the SQL query with parameters
            db_cursor.execute(sql, (Name, Email, hashed_password.decode('utf-8')))
            # Commit the changes
            db_mysql.commit()
            return "<script>alert('User already exists');</script>"
          
          
     except Exception as e:
            # Log the exception for debugging purposes
        print("An error occurred:", str(e))
        # You can also raise the exception to propagate it further
        # raise
        return 'An error occurred: {}'.format(str(e))

if __name__== '__main__':
    app.run(debug=True)