import json
import traceback
from .constant_status import *

def success_signup():
    return json.dumps({"message":SIGN_UP}), 201, HEADERS