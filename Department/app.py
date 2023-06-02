from flask import Flask
from department_list import department_list

app = Flask(__name__)

# Register profile routes
app.register_blueprint(department_list)


if __name__ == "__main__":
   app.run(debug=True)


