from fastapi import FastAPI, status
from .auth_services import auth_service, UserModel, ChannelModel
from fastapi.requests import Request
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




@app.post("/register", status_code=status.HTTP_202_ACCEPTED)
async def register_user(user_data: UserModel):
    """
    Register a new user
    """
    return auth_service.signup_user(user_data)

@app.post("/login", status_code=status.HTTP_200_OK)
async def login_user(request: Request, user_data: UserModel):
    """
    Login a user"""
    return auth_service.login_user(request, user_data)

@app.get("/users/{email}")
async def get_user(email: str):
    """
    Get a user by email
    """
    user = auth_service.get_user_by_email(email)
    return user


@app.post("/set-channels", status_code=status.HTTP_202_ACCEPTED)
async def set_channels(request: Request, channel_data: ChannelModel):
        
        return auth_service.set_channels(channel_data=channel_data)


@app.get("/")
async def home():
    return {"message": "Welcome to the home page"}

@app.get("/logo")
async def logo():
    return FileResponse("Black Clean Modern Letter A Logo.png")


@app.get("/integration.json")
def get_integration_json(request: Request):
    base_url = str(request.base_url).rstrip("/")

    integration_json = {

        "data": {
            "date": {
                "created_at": "2025-02-19",
                "updated_at": "2025-02-20"
                },

            "descriptions": {
                "app_description": "Sends an alert to telex webhook when user tries to brute force attack the web application",
                "app_logo": f"{base_url}/logo",
                "app_name": "Brute Force attack alert",
                "app_url": base_url,
                "background_color": "##E74C3C"
                },
            "integration_category": "Security & Compliance",
            "integration_type": "modifier",
            "is_active": False,
            "output": [
                {
                    "label": "output_channel_1",
                    "value": True
                },
                {
                    "label": "output_channel_2",
                    "value": False
                }
            ],
                        "key_features": [
                "Sends alert when login attempt fails 5 times in 5 minutes",
                "Sends alert when user atempt to login failed 5 times using multiple ip address",
            ],
            "permissions": {
                "monitoring_user": {
                    "always_online": True,
                    "display_name": "Security Monitoring"
                }
            },
            "settings": [
                {
                    "label": "Gender",
                    "type": "radio",
                    "required": True,
                    "default": "Male",
                    "options": ["Male", "Female"]
                    },
                {
                    "label": "Key",
                    "type": "text",
                    "required": True,
                    "default": "customize the message recieved"
                    },
                {
                    "label": "Do you want to continue",
                    "type": "checkbox",
                    "required": True,
                    "default": "Yes"
                },
                {
                    "label": "Provide Speed",
                    "type": "number",
                    "required": True,
                    "default": "1000"
                    },
                {
                    "label":"Sensitivity Level",
                    "type": "dropdown",
                    "required": True,
                    "default": "Low",
                    "options": ["High", "Low"]
                    },
                {
                    "label": "Alert Admin",
                    "type": "multi-checkbox",
                    "required": True,
                    "default": "Super-Admin",
                    "options": ["Super-Admin", "Admin", "Manager", "Developer"]
                    }
                ],
            "target_url": base_url
         }
    }

    return integration_json