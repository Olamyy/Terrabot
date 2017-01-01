log_file = '../log.log'
db_name = 'terrabot'
server_port = 8000
default_message = "Hi, I'm TerraBot"
bot_name = "TerraBot"
api_url = "/api/"
api_version = "v1.0"
host = "localhost"
api_body = ["message", "service_id", "user_id"]
ERROR_MESSAGES = {
    "NO_DATA_ERROR": "No data passed through. Pass some data",
    "INVALID_SERVICE": "Invalid service ID. Could not get service",
    "INVALID_USER": "Invalid user ID. Could not get user",
    'UNABLE_TO_CREATE': "Unable to create the required service or user"
}
