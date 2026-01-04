import os
from dotenv import load_dotenv

# Load variables from .env into environment
load_dotenv()

BASE_URL = os.getenv("BASE_URL", "").strip()
PUBLIC_API_KEY = os.getenv("PUBLIC_API_KEY", "").strip()
PRIVATE_SECRET_KEY = os.getenv("PRIVATE_SECRET_KEY", "").strip()
ACCOUNT_ID = os.getenv("ACCOUNT_ID", "").strip()

def validate_config() -> None:
    """Fail fast if required config is missing."""
    missing = []
    if not BASE_URL:
        missing.append("BASE_URL")
    if not PUBLIC_API_KEY:
        missing.append("PUBLIC_API_KEY")
    if not PRIVATE_SECRET_KEY:
        missing.append("PRIVATE_SECRET_KEY")
    if not ACCOUNT_ID:
        missing.append("ACCOUNT_ID")

    if missing:
        raise ValueError(
            "Missing required environment variables: "
            + ", ".join(missing)
            + ". Add them to a .env file in the project root."
        )
