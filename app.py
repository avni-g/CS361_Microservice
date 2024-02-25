from flask import Flask, request, jsonify, render_template 
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
import os 
import json

# To run locally, import Flask. 

## Init app 

##  curl -d '{\"sys_bp\":\"120\",\"dia_bp\":\"80\", \"weight_lbs\":\"150.0\", \"height_inches\":\"68\"}' -X POST http://localhost:5000/vitals/datastore -H"
##  curl -X GET http://localhost:5000/vitals/datastore -H "
##  curl -X GET http://localhost:5000/vitals/datastore/1 -H "

### DB Creation 

app = Flask(__name__) 

basedir = os.path.abspath(os.path.dirname(__file__))

## Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
## app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/HealthMetrics'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db= SQLAlchemy(app)

# Initialize ma 
ma = Marshmallow(app)

# Vitals Class/Model
class HealthMetrics(db.Model):
    metrics_id = db.Column(db.Integer, primary_key = True)
    patient_id = db.Column(db.Integer, default = None)
    sys_bp = db.Column(db.Integer, default = None)
    dia_bp = db.Column(db.Integer, default = None)
    weight_lbs = db.Column(db.Float, default = None)
    height_inches = db.Column(db.Integer, default = None)

    def __init__(self, patient_id, sys_bp, dia_bp, weight_lbs, height_inches):
        self.patient_id = patient_id 
        self.sys_bp = sys_bp
        self.dia_bp = dia_bp
        self.weight_lbs = weight_lbs
        self.height_inches = height_inches 

# Vitals schema 
class HealthMetricsSchema(ma.Schema):
    class Meta: 
        fields = ('metrics_id', 'patient_id', 'sys_bp', 'dia_bp', 'weight_lbs', 'height_inches')

# Initialize schema 
healthmetric_schema = HealthMetricsSchema()
healthmetrics_schema = HealthMetricsSchema(many=True)


with app.app_context():
    #db.drop_all() # Run if any changes are made. 
    db.create_all()



### Routing 

@app.route('/api/healthdata/post')
def postdata():
    return render_template('postdata.html')

@app.route('/')
def index():
    return render_template('index.html')

# Create a Vitals record
@app.route('/api/healthdata/post', methods=['POST'])
def add_vitals():
    patient_id = request.form['patient_id']
    sys_bp = request.form['sys_bp']
    dia_bp = request.form['dia_bp']
    weight_lbs = request.form['weight_lbs']
    height_inches = request.form['height_inches']

    new_vitals = HealthMetrics(patient_id, sys_bp, dia_bp, weight_lbs, height_inches)
    
    db.session.add(new_vitals)
    db.session.commit()

    result = healthmetric_schema.jsonify(new_vitals)
    return result

"""
with app.app_context():
    print(Product.query.all())
    all_products = Product.query.all() 
    result = products_schema.dump(all_products)
    print(result)
"""


# Get all vitals
@app.route('/api/healthdata', methods=['GET'])
def get_vitals():
    all_vitals = HealthMetrics.query.all()
    result = healthmetrics_schema.dump(all_vitals)
    #print(result)
    return jsonify(result)
    #jsonified = jsonify(result)
    #return render_template('index.html', jsonified = jsonified)
    #return jsonified


# Get single Vitals record 
@app.route('/api/healthdata/<id>', methods=['GET'])
def get_vitals_record(id):
    vitals_record = HealthMetrics.query.get(id)
    return healthmetric_schema.jsonify(vitals_record)

"""
# Update a Vitals record
@app.route('/vitals/<id>', methods=['PUT'])
def update_vitals(id):
    vitals_record = HealthMetrics.query.get(id)

    patient_id = request.json['patient_id']
    sys_bp = request.json['sys_bp']
    dia_bp = request.json['dia_bp']
    weight_lbs = request.json['weight_lbs']
    height_inches = request.json['height_inches']

    vitals_record.patient_id = patient_id 
    vitals_record.sys_bp = sys_bp
    vitals_record.dia_bp = dia_bp
    vitals_record.weight_lbs = weight_lbs
    vitals_record.height_inches = height_inches 

    db.session.commit()

    return healthmetric_schema.jsonify(vitals_record)

# Delete single Vitals Record
@app.route('/vitals/<id>', methods=['DELETE'])
def delete_vitals_record(id):
    vitals_record = HealthMetrics.query.get(id)
    db.session.delete(vitals_record)
    db.session.commit()
    return healthmetric_schema.jsonify(vitals_record)

"""

## Run Server 
if __name__ == '__main__':
    app.run(debug=True)