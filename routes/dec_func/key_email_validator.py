from email_validator import validate_email, EmailNotValidError
import traceback
from .errors_messages import *


def check_valid_email(email):
    try:
        valid = validate_email(email)
        email = valid.email
        return True
    except EmailNotValidError:
        traceback.print_exc()
        return username_email_org_exist("PROVIDE VALID EMAIL")
