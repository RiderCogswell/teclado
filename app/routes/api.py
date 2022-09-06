from flask import Blueprint, request
from app.models import User
from app.models import User
from app.db import get_db

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/users', methods=['POST'])
def signup():
  data = request.get_json()
  
  newUser = User(
    username = data.username, # dictionaries in python cannot be accessed like objects, must use bracket notation
    email = data.email,
    password = data.password
  )

  return ''