import datetime

from bson.json_util import dumps
from bson.objectid import ObjectId
from pymongo import MongoClient

import chatterbot
import config
from models import Services, Users


def handle_error(error_type):
        response = {
            "status": "failure",
            "response": {
                "time": datetime.datetime.now(),
                "message": config.ERROR_MESSAGES[error_type],
            }
        }
        return response


class ServiceHandler:
    def __init__(self, action=None, data=None):
        self.client = MongoClient('mongodb://localhost:27017/')
        db = self.client.terrabot
        self.coll = db.services
        if action == "create-service":
            self.create_service(data)
        elif action == "get-service":
            self.get_service(data)
        else:
            self.export_service(data)

    def create_service(self, data):
        """
        Create the provided service
        :param data:
        :return:
        """

        insert = Services(
            service_name=data["service_name"],
            service_desc=data["service_desc"],
            created_on=datetime.datetime.now(),
            passed_test=0,
            failed_test=0
        ).save()
        if insert:
            return {
                "status": "success",
                "response": {
                    "service_details": dumps(insert.to_son().to_dict()),
                    "message": "Successfully created service"
                }
            }

    def export_service(self, data):
        pass

    def get_service(self, id):
        """
        Gets a service from the database
        :param data:
        :return:
        """
        data = self.coll.find_one({"_id": ObjectId(id)})
        if data:
            return {
                "status": "success",
                "response": {
                    "service_details": dumps(data),
                    "message": "Successfully created service"
                }
            }
        else:
            return handle_error(error_type="INVALID_SERVICE")


class UserHandler:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        db = self.client.terrabot
        self.coll = db.users

    def create_user(self, userdata):
        """
               Create the provided service
               :param userdata:
               :return:
               """

        insert = Users(
            username=userdata["username"],
            service_registered_for=userdata["service_registered_for"],
            created_on=datetime.datetime.now(),
        ).save()
        if insert:
            return {
                "status": "success",
                "response": {
                    "service_details": dumps(insert.to_son().to_dict()),
                    "message": "Successfully created user"
                }
            }
        else:
            return handle_error(error_type="UNABLE_TO_CREATE")

    def get_user(self, id):
        """
                Gets a service from the database
                :param data:
                :return:
                """
        data = self.coll.find_one({"_id": ObjectId(id)})
        if data:
            return {
                "status": "success",
                "response": {
                    "service_details": dumps(data),
                    "message": "Successfully created service"
                }
            }
        else:
            return handle_error(error_type="INVALID_USER")

    def export_user(self, userdata):
        pass
