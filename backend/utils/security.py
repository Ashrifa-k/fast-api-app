from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password[:100])

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password[:100], hashed_password[:100])

def get_password_hash(password: str):
    return pwd_context.hash(password[:100])