import json

from flask import Flask, Response

from service import ActuatorService

app = Flask(__name__)

actuator_service = ActuatorService()

@app.route("/actuator")
def home():
    actuators = actuator_service.get_actuators()
    return Response(json.dumps(actuators, default=str),  mimetype='application/json')

def create_app():
   return app