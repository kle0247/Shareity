from dotenv import load_dotenv
import os 

load_dotenv()

class Configuration(object):
    SECRET_KEY = os.environ.get("SECRET_KEY")
# where database uri would go