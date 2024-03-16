from ._anvil_designer import LoginNovaTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class LoginNova(LoginNovaTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    anvil.users.login_with_form()
    print(f"Um usuario logou: {anvil.users.get_user()['email']}")
    self.button_1.icon = "fa:user"
    self.button_1.align = "right"
    self.button_1.spacing_below = None
    for row in app_tables.feedbacks.search(Usuario=anvil.users.get_user()['email']):
      self.querry_feedbacks.text ='Dia: ' + row ['Data'] + ' ' + row ['Usuario'] +': '+ row['Feedback']
    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.logout()
    open_form('LandingPageNova')

  def PUBLICAR_click(self, **event_args):
    """This method is called when the button is clicked"""
    app_tables.feedbacks.add_row(Usuario = anvil.users.get_user()['email'],
                          Feedback = self.FEEDBACK.text,
                          Data = date.today().__str__())
    open_form('Login')