from src.infrastructure.config.secrets import get_secret

DATABASE_URL = get_secret("DATABASE_URL")
JWT_SECRET = get_secret("JWT_SECRET")

