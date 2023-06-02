from flask import Flask
from employee_profile import employee_profile
from employee_photo import employee_photo

app = Flask(__name__)

# Register profile routes
app.register_blueprint(employee_profile)

# # Register photo routes
app.register_blueprint(employee_photo)

if __name__ == "__main__":
   app.run(debug=True)


