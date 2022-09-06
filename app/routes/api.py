from flask import Blueprint, request, jsonify, session
from app.models import User
from app.models import User
from app.db import get_db
import sys

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/users', methods=['POST'])
def signup():
  data = request.get_json()
  db = get_db() # connect to database
  
  try:
    newUser = User(
      username = data['username'], # dictionaries in python cannot be accessed like objects, must use bracket notation
      email = data['email'],
      password = data['password']
    )

    db.add(newUser)
    db.commit() # add and then commit newUser
  except:
    # insert failed, send error to front end
    print(sys.exc_info()[0])

    db.rollback() # if insert failed, rollback commit (to avoid a crashed app)

    return jsonify(message = 'Signup failed'), 500 # and send error to front end

  session.clear() # clear previous session data
  session['user_id'] = newUser.id # save user data in session
  session['loggedIn'] = True # set logged in to true, for conditional rendering
  return jsonify(id = newUser.id)