import traceback
from functools import wraps
from flask import request
from .key_email_validator import *


def validate_signup_user(f):
    try:
        @wraps(f)
        def decorated(*args, **kwrgs):
            try:
                if "email" in request.json:
                    request.json["email"] = request.json["email"].lower()
                    validate_email = check_valid_email(request.json["email"])
                    if not validate_email:
                        return validate_email
                    print(request.json)
                    if "username" in request.json:
                        request.json["username"] = request.json['username'].lower()
                    return f(*args, **kwrgs)
            except Exception as e:
                traceback.print_exc()
                stack = traceback.extract_stack()
                (filename, line, process, text) = stack[-1]
                print("Filename: {}, Line: {}, Process: {}, Text: {}".format(filename,line,process,str(e)))
                return server_error(filename,line,str(e))
        return decorated
    except Exception as e:
        traceback.print_exc()
        stack = traceback.extract_stack()
        (filename,line,process,text) = stack[-1]
        print("Filename: {}, Line: {}, Process: {}, Text: {}".format(filename,line,process,text))
        return server_error(filename,line,text)
