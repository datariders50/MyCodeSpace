import requests

def check_email_zero_bounce(email):
    api_key = 'your-api-key'  # Get from ZeroBounce account
    url = f"https://api.zerobounce.net/v2/validate?api_key={api_key}&email={email}"
    
    response = requests.get(url)
    result = response.json()
    
    if result['status'] == "valid":
        return True  # Email is valid and active
    elif result['status'] in ["invalid", "do_not_mail"]:
        return False  # Email is inactive or invalid
    else:
        return None  # Catch-all for unknown responses

# Example usage
email = "example@example.com"
is_active = check_email_zero_bounce(email)
print(f"Is the email active? {is_active}")