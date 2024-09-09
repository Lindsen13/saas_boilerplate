import os


connection_params = {
    "user": os.environ["MONGO_USERNAME"],
    "password": os.environ["MONGO_PASSWORD"],
    "host": os.environ["MONGO_HOST"],
    "port": "",
    "namespace": "",
    "database": os.environ["MONGO_DATABASE"],
}
