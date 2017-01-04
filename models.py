from pymodm import connect, MongoModel, fields

import config

client = connect('{0}{1}'.format(config.db_uri, config.db_name))


class Services(MongoModel):
    service_id = fields.ObjectIdField(verbose_name="Service ID", primary_key=True)
    service_name = fields.CharField(verbose_name="Service Name", mongo_name="service_name")
    service_desc = fields.CharField(verbose_name="Service Description", max_length=300)
    # tested_users = fields.ListField(verbose_name="Tested User Count", field=fields.LineStringField, blank=True)
    failed_test = fields.IntegerField(verbose_name="Failed Test Count")
    passed_test = fields.IntegerField(verbose_name="Passed Test Count")
    created_on = fields.DateTimeField(verbose_name="Date of service creation")


class Users(MongoModel):
    user_id = fields.ObjectIdField(primary_key=True)
    username = fields.CharField(verbose_name="User Name", max_length=50)
    service_registered_for = fields.ObjectIdField(verbose_name="Service ID")
    created_on = fields.DateTimeField(verbose_name="Date of user creation")


class Train(MongoModel):
    training_id = fields.ObjectIdField(primary_key=True)
    service_id = fields.ObjectIdField()
    user_id = fields.ObjectIdField()
    training_data = fields.DictField()
#
# test = Users.objects.all()
# print(list(test))


# #
# insert = Users(
#     username="Olamilekan",
#     service_registered_for= ObjectId("5868a60cbba4a24b01f7a5a2"),
#     created_on=datetime.datetime.now()
# ).save()
