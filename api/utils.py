from passlib.context import CryptContext
import jwt
from db.datbase import setting, redis, session
from datetime import datetime, timedelta, timezone
from uuid import uuid4
from models.log import FailedLogginAttempt
import requests
from models.channels import Channels




password_context = CryptContext(schemes=["bcrypt"])

def get_hass_password(pwd: str):
    hash = password_context.hash(pwd)
    return hash


def verify_password(pwd: str, hashed_pwd: str) -> bool:
    is_valid = password_context.verify(pwd, hashed_pwd)
    return is_valid

def create_token(user_data: dict) -> str:
    payload = {
        "user": user_data,
        "exp": datetime.now(timezone.utc) + timedelta(seconds=setting.TOKEN_EXPIRATION),
        "jti": str(uuid4())
    }
    token = jwt.encode(payload=payload, key=setting.TOKEN_SECRET, algorithm=setting.TOKEN_ALGORITHM)
    return token

def decode_token(token: str) -> dict:
    try:
        decoded = jwt.decode(token, key=setting.TOKEN_SECRET, algorithms=[setting.TOKEN_ALGORITHM])
        return decoded
    except jwt.ExpiredSignatureError:
        return {"error": "Token has expired"}
    except jwt.InvalidTokenError:
        return {"error": "Invalid token"}
    except Exception as e:
        return {"error": str(e)}


def log_failed_attempt(email: str, ip_address: str):

    log = FailedLogginAttempt(email=email, ip_address=ip_address, attempt_time=datetime.now(timezone.utc))
    log.new()

    redis.incr(ip_address)
    redis.expire(ip_address, 300)


def is_brute_force(ip: str, threshold: int = 5) -> bool:
    count = redis.get(ip)
    if count is None:
        return False
    return int(count) > threshold



def send_to_telex(email: str, message: str):

    channels = session.query(Channels).all()

    for channel in channels:
        payload = {
            "event_name": "brute_force attack dectected",
            "message": message,
            "status": "success",
            "username": "AyLon Website",
        }

        response = requests.post(
            channel.channel_url,
            json=payload,
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
        )
    print(response.json())