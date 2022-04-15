import traceback

import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyCyhztJuQz4QNgR3cYkNCAKodHKNT3maC4",
    "authDomain": "enactus-sake.firebaseapp.com",
    "databaseURL": "https://enactus-sake-default-rtdb.firebaseio.com",
    "projectId": "enactus-sake",
    "storageBucket": "enactus-sake.appspot.com",
    "messagingSenderId": "920466632092",
    "appId": "1:920466632092:web:2e73db896459892ccaec59",
    "measurementId": "G-6E2KRGTTPV"
}


def signing_up():
    auth = firebase.auth()
    email = input('Enter Email : ')
    password = input('Enter Password : ')
    try:
        auth.create_user_with_email_and_password(email, password)
        print('Created user ', email)
    except Exception:
        traceback.print_exc()


def signing_in():
    auth = firebase.auth()
    email = input('Email : ')
    password = input('Password : ')
    try:
        auth.sign_in_with_email_and_password(email, password)
        print('Signed in as ', email)
    except Exception:
        traceback.print_exc()


firebase = pyrebase.initialize_app(firebaseConfig)
signing_in()

# db = firebase.database()

# storage = firebase.storage()
