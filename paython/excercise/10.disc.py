student = {
    "name": "Rathod Virendra siha",
    "age": 20,
    "gender": "Male",
    "dob": "27/05/2006",
    "pincode": 364002,
    "email": "virendra.rathod@email.com",
    "phone": "9737547566",
    "address": "Bhavnagar",
    "nationality": "Indian",
    "marital_status": "Single",
    "occupation": "Software Engineer",
    "company": "none",
    "education": "B.C.A",
    "hobbies": ["Reading", "Traveling", "Music"],
    "favorite_food": "pizz",
    "favorite_color": "Blue",
    "blood_group": "O+",
    "height_cm": 175,
    "weight_kg": 60,
    "favorite_tourist_destinations": [
        "Goa",
        "Manali",
        "Paris",
        "Dubai",
        "Bali"
    ]
}

#print dictionary
print(student)

#print name, age, gender, dob
print(student['name'])
print(student['age'])
print(student['gender'])
print(student['dob'])

#add key value pair pincode into dictionary 
student.update({'pincode':364002})
print(student['pincode'])

#add key value pair to store your 5 favourite touriest destination 
student.update({'favorite_tourist_destinations':['goa','manali','paris','dubai','bali']})

#print all the favourite touriest destination 
print(student['favorite_tourist_destinations'])

#use update method to add new key value pair in dictionary
student.update({'favorite_tourist_destinations':['goa','manali','paris','dubai','bali']})
print(student['favorite_tourist_destinations'])

#use pop method to remove dob 
student.pop('dob')
print(student)

#use popitem item method to remove last item 
student.popitem()
print(student)

#display all value
print(student.value())

#display all key
print(student.key())

#copy dictionary to another dictionary using copy function 
std=student.copy()
print(std)
#clear newly create dictionary. 
