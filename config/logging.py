from loguru import logger
from pathlib import Path

# Create logs folder if it doesn't exist
Path("logs").mkdir(exist_ok=True)

# Remove default logger
logger.remove()

# Save logs to file
logger.add("logs/app.log", level="INFO")

# Also show logs in terminal
logger.add(lambda msg: print(msg, end=""), level="INFO")