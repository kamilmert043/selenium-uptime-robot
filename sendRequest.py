import requests
import os
from dotenv import load_dotenv
from sendMail import send_email

load_dotenv()
base_url = os.getenv("BASE_URL")

def requestSend():
    try:
        response = requests.get(base_url, timeout=10)
        status = response.status_code
        print(f"Status Code: {status}")

        if status == 200:
            print("Connection established")
        elif status == 204:
            send_email("No item found with the specified key", "204 No Content")
        elif status == 304:
            send_email("Cache is still valid (If-None-Match header)", "304 Not Modified")
        elif status == 400:
            send_email("Malformed syntax in request", "400 Bad Request")
        elif status == 401:
            send_email("User authentication required", "401 Unauthorized")
        elif status == 403:
            send_email("Request understood but refused", "403 Forbidden")
        elif status == 404:
            send_email("Resource not found", "404 Not Found")
        elif status == 405:
            send_email("Method not allowed for resource", "405 Method Not Allowed")
        elif status == 406:
            send_email("Content characteristics not acceptable", "406 Not Acceptable")
        elif status == 429:
            send_email("Exceeded throttling limit", "429 Too Many Requests")
        elif status == 500:
            send_email("Unexpected server error", "500 Internal Server Error")
        else:
            send_email("Unexpected error. Check logs or contact admin.", f"Unknown Error: {status}")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the server.")
        send_email("Server is down or unreachable.", "Connection Error")
    except requests.exceptions.Timeout:
        print("Error: Request timed out.")
        send_email("The request to the server timed out.", "Timeout Error")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        send_email("An unexpected error occurred during the request.", "Request Error")
