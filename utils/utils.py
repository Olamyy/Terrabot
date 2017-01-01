import logging
import uuid

import config


def logger(level,message):
    logging.basicConfig(filename=config.log_file, level=logging.DEBUG)
    logging.log(logging.getLevelName(level), message)


def generate_service_id(id_for):
    uid = uuid.uuid4().hex[:10]
    service_id = "{0}_{1}".format(id_for, uid)
    return service_id