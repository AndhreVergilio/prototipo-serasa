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
    alert('Logou como: '+anvil.users.get_user()['email'])
    # Any code you write here will run before the form opens.

  def label_1_show(self, **event_args):
    """This method is called when the Label is shown on the screen"""
    self.label_1.text = ('logado como: ' + anvil.users.get_user()['email'])

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.logout()
    alert('Deslogou')
    anvil.users.login_with_form()

  def PUBLICAR_click(self, **event_args):
    """This method is called when the button is clicked"""
    app_tables.feedbacks.add_row(Usuario = anvil.users.get_user()['email'],
                          Feedback = self.FEEDBACK.text)
    
    
    
    

