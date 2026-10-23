import logging
import time
from pathlib import Path
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s:%(message)s : %(asctime)s : %(process)d",
)

logger = logging.getLogger(__name__)

concours = {
    "id": "C102",
    "location": None,
}

logger.debug("Inspecting concours record")
logger.info("Processing concours %s", concours["id"])

logger.info("Processing finished")

file_path=Path("logr.json").resolve()


try :
    with file_path.open(mode="r",encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    logger.exception(f"file not found in {file_path}")
    sys.exit(2)
else:
    logger.info("found the file")