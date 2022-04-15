from firebase import firebase

firebase = firebase.FirebaseApplication('https://enactus-sake-default-rtdb.firebaseio.com/',None)
data = {
    'Name' : 'Thermometer',
    'Cost' : '500',
    'Availability' : '5'
}

result = firebase.post('https://enactus-sake-default-rtdb.firebaseio.com/Pythonian',data)
print(result)