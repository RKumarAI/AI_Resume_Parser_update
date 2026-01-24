import logging
import re
import sys

# 1. Setup Professional Logging
def get_logger(name):
    """Returns a pre-configured logger for consistent console output."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler(sys.stdout)
        # 2026 Standard: timestamp - module name - level - message
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger

# 2. Text Preprocessing/Cleaning
def clean_text(text):
    """
    Standardizes text for AI processing by removing invisible characters,
    excessive whitespace, and normalizing encoding.
    """
    if not text:
        return ""
    
    # Remove non-printable characters (common in PDF extractions)
    text = "".join(char for char in text if char.isprintable() or char in "\n\r\t")
    
    # Replace multiple newlines or spaces with single ones to save AI tokens
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r' +', ' ', text)
    
    return text.strip()

# 3. Data Validation Helpers
def validate_email(email):
    """Simple regex check to flag potentially malformed data from AI."""
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(regex, email)) if email else False