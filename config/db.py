from pymongo import MongoClient
import urllib.parse

username = urllib.parse.quote_plus('Saurabh-0903')
password = urllib.parse.quote_plus('S@urabh0903')
conn = MongoClient("mongodb+srv://%s:%s@cluster0.a4g9tgw.mongodb.net/" % (username, password))