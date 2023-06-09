#!/bin/bash
from flask import Flask
from employee_profile import employee_profile
from employee_photo import employee_photo

app = Flask(__name__)

# Register profile routes
app.register_blueprint(employee_profile)

# # Register photo routes
app.register_blueprint(employee_photo)

@app.route("/e")
def hello():
   return "Employee container"

if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True, port=5000)


