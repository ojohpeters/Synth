from flask_wtf import FlaskForm
from wtforms.fields import DateField
from wtforms import StringField, TelField, EmailField, IntegerField, SubmitField, PasswordField, TextAreaField
from wtforms_alchemy import PhoneNumberField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import DataRequired, InputRequired, EqualTo, email, length, ValidationError, NumberRange, InputRequired

class ApplicationForm(FlaskForm):
    Fullname = StringField('Full Name', validators=[DataRequired()])
    Email = EmailField('Email Adress', validators=[DataRequired(), email() ], render_kw={"placeholder": "JohnDoe@gmail.com"})
    PhoneNumber = PhoneNumberField('Phone Number', region='US', display_format='national',  validators=[DataRequired()], render_kw={"autocomplete":"tel"})
    DOB = DateField('Date Of Birth', validators=[DataRequired()])
    PersonnelID = StringField('PersoneID', validators=[DataRequired()], render_kw={"placeholder":"Enter the ID given To you by any of our Personnel"})
    Street = StringField('Address', validators=[DataRequired(), length(min=8, max=70)], render_kw={"autocomplete":"street-address"})
    SSN = PasswordField('Social Security Number', validators=[DataRequired(), length(min=9, max=9)])
    Confirm_SSN = PasswordField('Confirm Social Security Number', validators=[DataRequired(), EqualTo('SSN')])
    FrontID = FileField('Upload a valid ID(Front)')
    BackID = FileField('Upload a valid ID(Back)')
    Submit = SubmitField('Apply Now')

class Contactus(FlaskForm):
    Subject = StringField('Subject', render_kw={"placeholder":"Subject"})
    Message = TextAreaField('Message', validators=[DataRequired()], render_kw={"placeholder":"Your Message","cols":"30",
            "rows":"10"}) 
    Submit = SubmitField('Submit')      