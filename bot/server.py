import datetime

from flask import request
from flask_api import FlaskAPI

import config
from handlers import ServiceHandler, UserHandler, handle_error
from utils import utils

app = FlaskAPI(__name__)
# terra_bot = learnerbot.TerraBotTrainer()
url = "{0}/{1}".format((config.api_url + config.api_version), "")
service_handler = ServiceHandler()
user_handler = UserHandler()


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
        return  utils.get_response_data(status="failure", error_or_sucess_message=request.data["message"])


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


@app.route(url + "get-user", methods=["GET"])
def get_user():
    response = user_handler.get_user(id=request.args.get("user_id"))
    return response


if __name__ == "__main__":
    app.run(host=config.host, port=5000, debug=True)
