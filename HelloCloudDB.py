from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

#Init app
app = Flask(__name__)

#Database
#app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://webadmin:TIHnin12529@node8584-advweb-14.app.ruk-com.cloud:11094/CloudDB'
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://webadmin:TIHnin12529@10.100.2.181:5432/CloudDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Init db
db = SQLAlchemy(app)
#Init ma
ma = Marshmallow(app)

#Student Class/Model
class Students(db.Model):
    id = db.Column(db.String(15), primary_key=True, unique=True)
    name = db.Column(db.String(50))
    phone = db.Column(db.String(25))
    roomID = db.Column(db.String(10))
    
    def __init__(self, id, name, phone, roomID):
        self.id = id
        self.name = name
        self.phone = phone
        self.roomID = roomID

# Student Schema
class StudentSchema(ma.Schema):
    class Meta:
        fields =('id', 'name', 'phone', 'roomID')

# Init Schema 
student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

# Get All 
@app.route('/student', methods=['GET'])
def get_Students():
    all_students = Students.query.all()
    result = students_schema.dump(all_students)
    return jsonify(result)

# Create a Staff
@app.route('/staff', methods=['POST'])
def add_staff():
    id = request.json['id']
    name = request.json['name']
    email = request.json['email']
    phone = request.json['phone']

    new_staff = Staffs(id, name, email, phone)

    db.session.add(new_staff)
    db.session.commit()

    return staff_schema.jsonify(new_staff)

# Update a Staff
@app.route('/staff/<id>', methods=['PUT'])
def update_staff(id):
    staff = Staffs.query.get(id)
    
    name = request.json['name']
    email = request.json['email']
    phone = request.json['phone']

    staff.name = name
    staff.email = email
    staff.phone = phone

    db.session.commit()

    return staff_schema.jsonify(staff)

# Web Root Hello
@app.route('/', methods=['GET'])
def get():
    return jsonify({'ms': 'Hello Cloud DB1'})

# Run Server
if __name__ == "__main__":
    app.run()