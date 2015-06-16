import os
from pymongo import MongoClient


try:
    mongo = MongoClient(host=os.getenv('MONGO_PORT_27017_TCP_ADDR', 'localhost'))
    db = mongo.helsinki
    subscriptions = db.subscriptions
except Exception as e:
    logging.error('Could not connect to mongoDB: ', e)
    raise e


def save_subscription(email, topic):
    sub = {'email': email, 'topic': topic, '_id': email.lower()}
    subscriptions.insert_one(sub)


def get_subscriptions():
    return subscriptions.find()