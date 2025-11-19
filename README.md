## JSON, FLASK AND JSONIFY
Firstly, we import json built-in library in python, a format to represent structured data, easy to parse in programming languages
I imported Flask to create an API app, request to parse HTTP scripts, and jsonify to produce json content.

app=Flask(__name__) creates a Flask object, and __name__ tells us where the app is defined.

Then, we create an employees_company dictionary, storing data of employees, i.e. their name and their id numbers.

Next, we use a decorator. A decorator tells the Flask object, that whenever a request comes to this url, run this function.
Whenever the API program gets a 'GET' request, it runs get_employees(), get_employees_by_id() and employee_validation() functions.

## GET METHOD
The first decorator returns the entire list of employees, if you send a request- "GET http://localhost:5000/employees" to the API.
The second decorator returns the name of the employee with a certain id number. 
Eg: if we send request- "GET http://localhost:5000/employees/2" to API, it looks for employee with id=2. If found, it returns employee name, else it returns error 404.

## POST METHOD
The route decorator with 'post' method, sends a post request to the employee and runs the create_employee() function.
The global nextEmployeeId is a variable that is used to modify the value of the next employee id.

request.data contains the raw request body which should be posted in the server by API.
json.loads() converts request.data into a python dictionary.
Eg: if client sends 4:'Sam'
the server adds the following key-value pair to the dictionary.

## PUT REQUEST
Next, the HTTP Put request, updates the existing dictionary, and does not add anything new to it.
It receives a PUT request by the client, to update an employee by id.
It checks if the employee exists, else it returns error 404.
Then, it parses the json request and converts it to a dictionary key-value pair, and thus, updates employee's data.

## DELETE REQUEST
The route decorator with 'delete' method, accepts an employee id from the client, which should be deleted.
It looks up the employee's name using the get_employees_by_id() function. If employee doesn't exist, 404 error is returned.
If the employee exists, it removes it from the dictionary and returns deleted employee as json.

This was the output of the code, when I typed: 127.0.0.1:5000/employees
Click here ---> http://localhost:5000/employees

This was the output of the code, when I typed: 127.0.0.1:5000/employees/1







