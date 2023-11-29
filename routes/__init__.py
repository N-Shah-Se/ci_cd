from flask import Blueprint

routes = Blueprint("routes", __name__)

from .UserManagement.user import *
