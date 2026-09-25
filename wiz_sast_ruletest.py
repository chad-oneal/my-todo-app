import logging
logger = logging.getLogger(__name__)

def startup_event():
    # exact incident pattern
    logger.info(f"Database URL: {settings.DATABASE_URL[:40]}...")
