from models.user import User
from models.log import FailedLogginAttempt
from db.datbase import session
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.functions import func
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from .utils import get_hass_password, verify_password, create_token, log_failed_attempt, is_brute_force,  send_to_telex
from fastapi import Depends, status
from datetime import datetime, timezone, timedelta
from typing import List
from models.channels import Channels


class UserModel(BaseModel):
    email: str
    password: str

class ChannelModel(UserModel):
    channels: List[str]


class AuthService:

    def get_user_by_email(self, email: str, session: Session = session) -> UserModel:
        user = session.query(User).filter(User.email == email).first()
        return user


    def signup_user(self, user_data: UserModel, session: Session = session):
        user_data.email = user_data.email.lower()
        email = user_data.email
        hashed_password = get_hass_password(user_data.password)

        user = self.get_user_by_email(email)
        if user:
            return JSONResponse(status_code=400, content={"message": "User already exists"})
        
        new_user = User(email=email, password=hashed_password)
        new_user.new()

        return JSONResponse(status_code=201, content={"message": "User created successfully"})
    
    def login_user(self, request, user_data: UserModel, session: Session = session):
        user_data.email = user_data.email.lower()
        user = self.get_user_by_email(user_data.email)
        ip_address = request.client.host
        if is_brute_force(ip_address):
                result = session.query(
                    FailedLogginAttempt.ip_address,
                    func.count(FailedLogginAttempt.id).label("count")).filter(
                        FailedLogginAttempt.ip_address == ip_address,
                        FailedLogginAttempt.attempt_time == datetime.now(timezone.utc) + timedelta(minutes=5)).group_by(FailedLogginAttempt.ip_address).all()

                
                if len(result) > 1:
                    message =  f"email: {user_data.email} tried to sign in from multiple ip address from different location with incorrect credentials"
                    send_to_telex(user_data.email, message=message)
                    return JSONResponse(status_code=status.HTTP_429_TOO_MANY_REQUESTS, content={"message": "Your account has been suspended"})
                message = f"email: {user_data.email} tried to sign in with incorrect credentials more than 5 times in 5 minutes"
                send_to_telex(user_data.email, message=message)
                return JSONResponse(status_code=status.HTTP_429_TOO_MANY_REQUESTS, content={"message": "Too many login attempts"})
        if not user:
            log_failed_attempt(email = user_data.email, ip_address = ip_address)
            return JSONResponse(status_code=400, content={"message": "User does not exist"})
        
        if not verify_password(user_data.password, user.password):
            log_failed_attempt(email= user_data.email, ip_address = ip_address)
            return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={"message": "Invalid password"})
    
        token = create_token({"email": user.email})        
        return JSONResponse(status_code=200, content={"message": "Login successful", "access_token": token})

    def verify_user(self, email: str, password: str, session = session) -> bool:

        user = self.get_user_by_email(email)

        if user is None:
            return False
        return verify_password(password, user.password)


    def set_channels(self, channel_data: ChannelModel):

        if self.verify_user(channel_data.email, channel_data.password):
            for channel_url in channel_data.channels:
                channel = Channels(channel_url=channel_url)
                channel.save()
            return JSONResponse(status_code=status.HTTP_202_ACCEPTED, content={"message": "Channels succesfully add"})
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": "Channels cannot be added"})

auth_service = AuthService()