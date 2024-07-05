from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import datetime

app = Flask(__name__)

# MySQL Configuration
db_config = {
    'host': 'localhost',
    'user': 'sqluser',
    'password': 'password',
    'database': 'prg',
}
@app.route('/')
def home():
    return render_template('blood.html')

@app.route('/submit',methods=['POST'])
def Submit_data():
    if request.method=='POST':
        name=request.form['name']
        agegroup=request.form['agegroup']
        gender=request.form['gender']
        bloodgroup=request.form['bloodgroup']
        ph_no=request.form['ph_no']
        date=datetime.datetime.today().strftime('%Y-%m-%d')

        connection=mysql.connector.connect(**db_config)
        cursor=connection.cursor()

        Y='INSERT INTO blood_donation2(name,agegroup,gender,bloodgroup,ph_no,date) VALUES (%s,%s,%s,%s,%s,%s)'
        data=(name,agegroup,gender,bloodgroup,ph_no,date)
        cursor.execute(Y,data)

        connection.commit()
        cursor.close()
        connection.close()
        
        return render_template('index.html')
    else:
        return redirect(url_for('home'))
if __name__ == '__main__':
    app.run(debug=True)

