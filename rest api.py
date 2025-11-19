import json
from flask import Flask, request, jsonify

app=Flask(__name__)

employees_company=[
    {'id':1, 'name':'Raghav'},
    {'id':2, 'name':'Pranit'},
    {'id':3, 'name':'Adi'},
]

nextEmployeeId=4

@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees_company)

@app.route('/employees/<int:id>', methods=['GET'])
def get_employees_by_id(id: int):
    employee=get_employee(id)
    if employee is None:
        return jsonify({'error: employee does not exist! try again!'}), 404
    return jsonify(employee)

def get_employee(id):
    return next((emp for emp in employees_company if emp['id']==id), None)

def employee_validation(employee):
    for key in employee.keys():
        if key!='name':
            return False
        else:
            return True

@app.route('/employees', methods=['POST'])
def create_employee():
    global nextEmployeeId
    employee=json.loads(request.data)
    if not employee_validation(employee):
        return jsonify({'error':'Invalid employee properties.'}), 400
    
    employee['id']=nextEmployeeId
    nextEmployeeId +=1
    employees_company.append(employee)

    return '', 201, {'location': f"/employees/{employee['id']}"}

@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id: int):
    employee=get_employee(id)
    if employee is None:
        return jsonify({'error: This employee does not exist!'}), 404
    
    update_employee=json.loads(request.data)
    if not employee_validation(update_employee):
        return jsonify({'error: employee has not been updated!'}), 404
    
    employee.update(update_employee)

    return jsonify(employee)

@app.route('/employees/<int:id>', methods=['DELETE'])
def employee_delete(id:int):
    global nextEmployeeId
    employee=get_employees_by_id(id)
    if employee is None:
        return jsonify({'error: employee has already been deleted and does not exist!'}), 404
    employees_company=[emp for emp in employees_company if emp['id']!=id]
    return jsonify(employee), 404

if __name__=="__main__":
    app.run(debug=True)
    


