#!/usr/bin/env python3
'''blueprint implementation
'''
from api.v1.views.session_auth import *
from api.v1.views.users import *
from api.v1.views.index import *
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")


User.load_from_file()