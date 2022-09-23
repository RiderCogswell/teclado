from flask import session, redirect
from functools import wraps

def login_required(func):
  @wraps(func) # wraps preserves the original name to make debugging easier -- PHEW
  def wrapped_function(*args, **kwargs): # think of this as (...arguments) in JS
    if session.get('loggedIn') == True:
      return func(*args, **kwargs)
    return redirect('/login')

  return wrapped_function