import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import joblib
import pandas

@anvil.server.callable
def predict_faringite(age, temperature, pain, swollenadp, tender, tonsillarswelling, exudate, cough, rino, conjunctivitis, erythema, abdopain, nauseavomit, headache, scarlet, petechiae):
  loaded_model = joblib.load(data_files['random_forest_model.pkl'])

  respostas = {
    'age_y': abs(int(age)),
    'pain': int(pain),
    'swollenadp': int(swollenadp),
    'tender': int(tender),
    'tonsillarswelling': int(tonsillarswelling),
    'exudate': int(exudate),
    'temperature': abs(float(temperature)),
    'cough': int(cough),
    'rhinorrhea': int(rino),
    'conjunctivitis': int(conjunctivitis),
    'headache': int(headache),
    'erythema': int(erythema),
    'petechiae': int(petechiae),
    'abdopain': int(abdopain),
    'nauseavomit': int(nauseavomit),
    'scarlet': int(scarlet)
  }

  dados_perguntas = pd.DataFrame([respostas])
  previsao = loaded_model.predict(dados_perguntas)
  return previsao[0]