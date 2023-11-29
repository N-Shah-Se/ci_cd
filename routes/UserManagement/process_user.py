import json
import traceback
from routes.dec_func.success_messages import success_signup
from routes.dec_func.errors_messages import server_error


def process_signup_user(body, ip):
    try:
        print(ip)
        return success_signup()
    except Exception as ex:
        traceback.print_exc()
        stack = traceback.extract_stack()
        (filename,line,process,text) = stack[-1]
        return server_error(filename,line,text)