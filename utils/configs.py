import os


connection_params = {
    "user": os.environ.get("MONGO_USERNAME","Not set"),
    "password": os.environ.get("MONGO_PASSWORD","Not set"),
    "host": os.environ.get("MONGO_HOST","cluster0.y9ldphq.mongodb.net"),
    "port": "",
    "namespace": "",
    "database": os.environ.get("MONGO_DATABASE","saas_db")
}
