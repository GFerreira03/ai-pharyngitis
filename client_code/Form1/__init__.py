from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def send_click(self, **event_args):
    faringite_predict = anvil.server.call('predict_faringite',
                                self.age_text.text,
                                self.temperature_text.text,
                                self.radio_pain_1.get_group_value(),
                                self.radio_swollenadp_1.get_group_value(),
                                self.radio_tender_1.get_group_value(),
                                self.radio_tonsillarswelling_1.get_group_value(),
                                self.radio_exudate_1.get_group_value(),
                                self.radio_cough_1.get_group_value(),
                                self.radio_rino_1.get_group_value(),
                                self.radio_conjunctivitis_1.get_group_value(),
                                self.radio_erythema_1.get_group_value(),
                                self.radio_abdopain_1.get_group_value(),
                                self.radio_nauseavomit_1.get_group_value(),
                                self.radio_headache_1.get_group_value(),
                                self.radio_scarlet_1.get_group_value(),
                                self.radio_petechiae_1.get_group_value())
  
    self.result_label.visible = True
    
    result = "Positive" if faringite_predict == 1 else "Negative"
    self.result_label.text = result

  def send_show(self, **event_args):
    """This method is called when the Button is shown on the screen"""
    
    