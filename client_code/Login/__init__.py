from ._anvil_designer import LoginTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Login(LoginTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    anvil.users.login_with_form()
    print(f"This user has logged in: {anvil.users.get_user()['email']}")
    # Any code you write here will run before the form opens.
