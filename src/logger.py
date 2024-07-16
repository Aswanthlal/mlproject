import logging
import os 
from datetime import datetime

LOG_Fille=f'{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log'
logs_path=os.path.join(os.getcwd(),'logs',LOG_Fille)
os.makedirs(logs_path,exist_ok=True)

LOG_Fille_PATH=os.path.join(logs_path,LOG_Fille)

logging.basicConfig(
    filename=LOG_Fille_PATH,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
      
)
