# check.py
import requests

def validate_html(file_path):
    with open(file_path, 'r') as file:
        html_content = file.read()

    url = "https://validator.w3.org/nu/?out=json"
    headers = {"Content-Type": "text/html; charset=utf-8"}
    response = requests.post(url, data=html_content.encode('utf-8'), headers=headers)

    if response.status_code == 200:
        errors = response.json().get("messages", [])
        if errors:
            print("HTML validation failed:")
            for error in errors:
                print(f"Line {error['lastLine']}: {error['message']}")
            exit(1)
        else:
            print("HTML validation passed.")
    else:
        print("Failed to connect to the validator.")
        exit(1)

if __name__ == "__main__":
    validate_html("index.html")