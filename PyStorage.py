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


def upload_to_storage(path,filename):
    storage.child(path).put(filename)
    url = storage.child(path).get_url(filename)
    print('File uploaded at ',url)

def download_from_storage(path):
    filename = path.split('/')[-1]
    storage.child(path).download('',filename)

firebase = pyrebase.initialize_app(firebaseConfig)

storage = firebase.storage()
filename = 'nothing.png'
path = 'Pythonian/' + filename
# upload_to_storage(path,filename)
download_from_storage(path)