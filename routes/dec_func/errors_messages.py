import json
from .constant_status import *


def username_email_org_exist(msg):
    message = globals()[msg]
    return json.dumps({"message":message}), 401, HEADERS

def server_error(*msg):
    (filename, line, text) =msg[0], msg[1], msg[2]
    error = ERROR_MSG.format(filename,line,text)
    return json.dumps({"message":error}), 503, HEADERS 


