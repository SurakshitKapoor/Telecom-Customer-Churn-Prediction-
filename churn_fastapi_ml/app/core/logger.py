
import logging
import os
from datetime import datetime

os.makedirs("logs", exist_ok=True)

# file name as per current date and time -> to know when the model is created and all!
log_file = f"logs/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    print("We are in logger.py")
    logger.info("Logger is working!")
    print(f"Logging to: {log_file}")
    print(os.getcwd())