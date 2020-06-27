# Importing 3rd party classes
from flask import Flask, request, Response, jsonify
# Importing custom functions
import src.utils.log as log
import src.utils.parser as parser
# Importing custom class
from src.api.api_services import api_services

# Initialize logger
logger = log.setup_custom_logger('root')

# Welcome
logger.debug('Welcome to flask scaffold')

# Parse arguments
config = parser.arg_parser()

# Initialize Flask server
app = Flask(__name__)

# Initialize API
api = api_services()

# API
@app.route('/', methods=['GET'])
def fun_1():
    return api.welcome()

@app.route('/image', methods=['POST'])
def fun_2():
    new_image = request.files["image"].read()
    # result = api.return_image(new_image)
    return Response(response=new_image, status=200, mimetype="image/jpeg")

# Entrypoint
if __name__ == '__main__':
    # Start app
    # app.debug = True
    app.run(port=config.port, host=config.host)