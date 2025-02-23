# User Authentication System with Brute Force Protection

This project implements a simple **user authentication system** that includes **brute force attack protection**. Users can register and log in, and the system blocks excessive failed login attempts, notifying a configured Telegram channel.

## Features

- **User Registration**
- **User Login**
- **Brute Force Protection**
  - Blocks accounts after **5 failed login attempts in 5 minutes**.
  - Sends an alert to a **configured Telegram channel** when an account is blocked.
- **Webhook Configuration** for alert notifications

---

## API Endpoints
**Base Url:** `https://aylon.duckdns.org`
### 1. Register a User

**Endpoint:** `POST /register`

**Request Body:**

```json
{
  "email": "user@example.com",
  "password": "your_secure_password"
}
```

**Response:**

```json
{
  "message": "User registered successfully"
}
```

### 2. Login a User

**Endpoint:** `POST /login`

**Request Body:**

```json
{
  "email": "user@example.com",
  "password": "your_secure_password"
}
```

**Responses:**

- ✅ **Success:**
  ```json
  {
    "message": "Login successful",
    "token": "your_access_token"
  }
  ```
- ❌ **Failed Login Attempt:**
  ```json
  {
    "error": "Invalid credentials"
  }
  ```
- ⛔ **Blocked Account (After 5 failed attempts):**
  ```json
  {
    "error": "Account is temporarily blocked due to multiple failed login attempts. An alert has been sent."
  }
  ```

---

### 3. Set Notification Channels

**Endpoint:** `POST https://aylon.duckdns.org/set-channels`

**Request Body:**

```json
{
  "email": "user@example.com",
  "password": "your_secure_password",
  "channel_webhook_url": ["https://your.telex.channel/webhook"]
}
```

**Response:**

```json
{
  "message": "Notification channels updated successfully"
}
```

---

## Testing Brute Force Protection

To test the **brute force attack functionality**, run the provided test script:

```sh
python test_brute_force.py
```

This script will attempt multiple failed logins and verify if the system blocks the account and sends an alert.

OR
Try Login in with invalid password 6 times. Then go check your channel to confirm that the alert has been sent

AND

Try login in with different Ip address with invalid password 6 times. Then go check your channel to confirm that the alert has been sent


---

## Screenshots

Include relevant screenshots of API requests and responses here.

---

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/PcNerd9/HNG-stage3-telex-integration.git
   ```
2. Create a virtual environment
   ```sh
   python3 -m venv .venv
   ```
3. Switch to the virtual environment
   ```sh
   source .venv.bin/activate
   ```
4. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
5. Run the server:
   ```sh
   uvicorn main:app --reload
   ```
