from routes import routes
from flask_cors import cross_origin
from flask import request
from flask_expects_json import expects_json
import traceback
from routes.dec_func.secret_info import *
from .process_user import *
from routes.dec_func.shah_wrapper import validate_signup_user
from routes.dec_func.errors_messages import server_error
from .userapischema import signup_keys

@routes.route("/signup", methods=["POST"])
@expects_json(signup_keys)
@validate_signup_user
def signup_user():
    try:
        print(request.json)
        print(request.remote_addr)
        return process_signup_user(request.json,request.remote_addr)
    except Exception as e:
        traceback.print_exc()
        stack = traceback.extract_stack()
        (filename,line,process,text) = stack[-1]
        return server_error(filename,line,text)