import datetime
import pprint

import pymongo
from bson import ObjectId
from pymodm import connect, MongoModel, fields

client = connect('mongodb://localhost:27017/terrabot')
from pymongo import MongoClient


class Services(MongoModel):
    service_id = fields.ObjectIdField(verbose_name="Service ID", primary_key=True)
    service_name = fields.CharField(verbose_name="Service Name", mongo_name="service_name")
    service_desc = fields.CharField(verbose_name="Service Description", max_length=300)
    # tested_users = fields.ListField(verbose_name="Tested User Count", field=fields.LineStringField, blank=True)
    failed_test = fields.IntegerField(verbose_name="Failed Test Count")
    passed_test = fields.IntegerField(verbose_name="Passed Test Count")
    created_on = fields.DateTimeField(verbose_name="Date of service creation")


class User(MongoModel):
    username = fields.CharField(verbose_name="User Name", max_length=50)
    service_registered_for = fields.ObjectIdField(verbose_name="Service ID")
    created_on = fields.DateTimeField(verbose_name="Date of user creation")
