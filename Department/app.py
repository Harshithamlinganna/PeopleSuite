from flask import Flask
from department_list import department_list

app = Flask(__name__)

# Register profile routes
app.register_blueprint(department_list)

@app.route("/test")
def hello():
   return "Department container"

if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True, port=8000)


