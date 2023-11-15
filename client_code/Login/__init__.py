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
    print(f"Um usuario logou: {anvil.users.get_user()['email']}")
    for row in app_tables.feedbacks.search(Usuario=anvil.users.get_user()['email']):
        self.querry_feedbacks.text = row ['Usuario'] +': '+ row['Feedback']
    # Any code you write here will run before the form opens.

  
  def label_1_show(self, **event_args):
    """This method is called when the Label is shown on the screen"""
    self.label_1.text = ('logado como: ' + anvil.users.get_user()['email'])

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.logout()
    alert('Deslogou')
    open_form('Login')

  def PUBLICAR_click(self, **event_args):
    """This method is called when the button is clicked"""
    app_tables.feedbacks.add_row(Usuario = anvil.users.get_user()['email'],
                          Feedback = self.FEEDBACK.text)
    open_form('Login')

  def querry_feedbacks_show(self, **event_args):
    """This method is called when the Label is shown on the screen"""
    pass