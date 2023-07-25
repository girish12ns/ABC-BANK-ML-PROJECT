import logging
import os
from datetime import datetime

LOGS_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_path=os.path.join(os.getcwd(),"logs",LOGS_FILE)
os.makedirs(log_path,exist_ok=True)

LOGS_FILE_PATH=os.path.join(log_path,LOGS_FILE)

logging.basicConfig(
    filename=LOGS_FILE_PATH,
    format="[%(asctime)s - %(lineno)d %(name)s - %(levelname)s - %(message)s ]",
    level=logging.INFO

)