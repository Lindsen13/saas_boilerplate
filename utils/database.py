from pymongo import MongoClient
from utils.configs import connection_params

# connect to mongodb
mongoconnection = MongoClient(
    "mongodb+srv://{user}:{password}@{host}/?retryWrites=true&w=majority&appName=Cluster0".format(
        **connection_params
    )
)

db = mongoconnection[connection_params["database"]]
