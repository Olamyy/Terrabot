import os

import chatterbot

import datetime

from flask import request
from flask.views import MethodView
from flask_api import FlaskAPI
from werkzeug import secure_filename
import config
from bot import Bot
from handlers import ServiceHandler, UserHandler, handle_error
from utils import utils

app = FlaskAPI(__name__)
url = "{0}/{1}".format((config.api_url + config.api_version), "")
service_handler = ServiceHandler()
user_handler = UserHandler()

app.config['UPLOAD_FOLDER'] = 'uploads/'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = {'json', 'csv'}


# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route(url, methods=['GET'])
def bot():
    """
    Bot base route.
    Really does nothing for now.
    Might populate it with some functions later.
    :return:
    """
    if request.method == "GET":
        return {"status": "success",
                "response": {
                    "time": datetime.datetime.now(),
                    "message": config.default_message,
                }}


@app.route(url + "listen", methods=['POST'])
def listen():
    """
    Listening url.
    Listens for incoming request(conversation) from the provided service id and user_id.

    :return:
    """
    if not request.data:
        return
        return utils.get_response_data(status="failure", error_or_sucess_message="Incomplete data sent.")
    else:
        return
        return utils.get_response_data(status="failure", error_or_sucess_message=request.data["message"])


@app.route(url + "create-service", methods=["POST"])
def create_service():
    """
    Creates a service.
    :return: service_id
    """
    if not request.data:
        response = handle_error(error_type="NO_DATA")
        return response
    else:
        response = service_handler.create_service(request.data)
        return response


@app.route(url + "get-service", methods=["GET"])
def get_service():
    response = service_handler.get_service(id=request.args.get("service_id"))
    return response


@app.route(url + "create-user", methods=["POST"])
def create_user():
    """
       Creates a service.
       :return: service_id
       """
    if not request.data:
        response = handle_error(error_type="NO_DATA")
        return response
    else:
        response = user_handler.create_user(request.data)
        return response


class FileTraining(MethodView, Bot):
    def __init__(self):
        super(FileTraining, self).__init__()

    def get(self):
        return handle_error(error_type="INVALID_METHOD")

    def post(self):
        if not request.files:
            response = handle_error(error_type="NO_DATA")
            return response
        else:
            training_file = request.files['file']
            if training_file and allowed_file(training_file.filename):
                filename = secure_filename(training_file.filename)
                training_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return self.init_training_file(training_file)


app.add_url_rule(url + "file-training", view_func=FileTraining.as_view('file-train'))


class ChatTrainer(MethodView, Bot):
    def __init__(self):
        super(ChatTrainer, self).__init__()

    def get(self):
        return handle_error(error_type="INVALID_METHOD")

    def post(self):
            data = {
                "service_id": request.data['service_id'],
                "message": request.data["message"],
                "response": request.data["response"]
            }
            return self.train(data, training_type="chat")

app.add_url_rule(url + "chat-training", view_func=ChatTrainer.as_view('chat-train'))


if __name__ == "__main__":
    app.run(host=config.host, port=5000, debug=True)
