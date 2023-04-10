# realhealth

[How to start the app]

1. git clone https://github.com/Pushkar917/realhealth.git
2. python -m venv venv
3. source venv/bin/activate
4. cd src
5. pip install -r requirements.txt
4. python manage.py runserver


[ What it does? ]

This App is to create secure login and regisration process for any User.
Flow :

[ Login, Registration and forget password ]
1. User register with its [username, email, password, first_name, last_name]
2. If registered successfully, an activation mail is sent to registered mail.
3. User clicks on the link to activate his account.
4. If users forgets his password, he can reset his password.
5. A reset password link would be sent to his registered mail id
6. He or she can reset his password using the link.


[ Profiles ]

1. As soon as user is registered, a profile is created simulatneously for that specific user.



[How it's implemented?]

Login/Registration and forgot passwords are implemented using djoser/jwt and django-rest-framework.
Profile is implemented using django-signals.
Mail implementation is done using djoser and djoser smtp mail backend

[ API-END-POINT ]

1. API's end point 
   A. "To create JWT token with username and password"
   B. "To register new user with username and password 
   C. "To activate the user with id and uid and token"
   D. "To confirm the reset password with uid and token"
   E. "Send the link for password reset to the mail"
   F. "Get Profile of logged in person"
   G. "Update the profile by username".
   H. "Get all profile"
   I. "Get profile by name"


   A. http://127.0.0.1:8000/api/v1/auth/jwt/create/
   B. http://127.0.0.1:8000/api/v1/auth/users/
   C. http://127.0.0.1:8000/api/v1/auth/users/activation/
   D. http://127.0.0.1:8000/api/v1/auth/users/reset_password_confirm/
   E. http://127.0.0.1:8000/api/v1/auth/users/reset_password/
   F. http://127.0.0.1:8000/api/v1/profile/me/
   G. http://127.0.0.1:8000/api/v1/profile/update/Pushkar1/
   H. http://127.0.0.1:8000/api/v1/profile/getAllProfiles
   I. http://127.0.0.1:8000/api/v1/profile/getProfileOf/test/




