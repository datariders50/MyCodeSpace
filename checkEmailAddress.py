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


import smtplib
import dns.resolver  # For MX record lookup

def check_email_active(email):
    domain = email.split('@')[1]
    
    try:
        # Find the mail server for the domain
        mx_records = dns.resolver.resolve(domain, 'MX')
        mail_server = str(mx_records[0].exchange)

        # SMTP connection (do not send email)
        server = smtplib.SMTP()
        server.set_debuglevel(0)  # 1 to print debug messages
        server.connect(mail_server)
        server.helo(server.local_hostname)  # local server name
        server.mail('your-email@example.com')  # Can be any valid email
        code, message = server.rcpt(email)  # Check if recipient is valid

        server.quit()

        if code == 250:
            return True  # Email exists and is active
        else:
            return False  # Email is inactive or doesn't exist

    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Example usage
email = "example@example.com"
is_active = check_email_active(email)
print(f"Is the email active? {is_active}")

