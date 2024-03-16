from ._anvil_designer import LandingPageLegadoTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil.js.window import Quill
import anvil.js

class LandingPageLegado(LandingPageLegadoTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

def click_login_button(self):
  teste = self.