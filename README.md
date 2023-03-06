# Django OTP with TWILIO
### To use OTP authentication in your django project:
+ Prerequisites
+ Python 3.6
+ Basic knowledge in Django
+ Twilio account

Set up your Twilio account [Twilio account](https://www.twilio.com/try-twilio)
+ Choose SMS
+ Alerts & Notifications
+ With code
+ Python
+ Get a Twilio phone number
+ Add these to you <app_name>/settings.py file 
```
ACCOUNT_SID='YOUR ACCOUNT SID'
AUTH_TOKEN='YOUR AUTH TOKEN'
COUNTRY_CODE='+country code of your choice'
TWILIO_WHATSAPP_NUMBER='whatsapp:+14155238886'
TWILIO_PHONE_NUMBER='number you get from Twilio'
```

#### Clone the project 
+ [Django-otp](https://www.github.com/kofnet002/Django-otp.git)
+ Install requirements.txt file in the root directory ```pip install requirements.txt```
+ Navigate to /verification/settings, at the bottom, replace the Twilio configuration
+ Create migration ```python manage.py makemigrations```
+ Migrate ```python manage.py migrate```
+ Set DEBUG = True in the settings file
+ Replace SECRET_KEY
+ Run your project ```python manage.py runserver```
