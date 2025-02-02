import logging
from core.config import settings


def configure_logging():
    """Configure application-wide logging settings."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    logger = logging.getLogger(settings.PROJECT_NAME)
    return logger


logger = configure_logging()
