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

import smtplib
import dns.resolver
import socket

def get_mx_record(domain):
    """Get the mail exchange (MX) record for the email domain."""
    try:
        # Query the MX records for the domain
        mx_records = dns.resolver.resolve(domain, 'MX')
        mx_record = str(mx_records[0].exchange)
        return mx_record
    except dns.resolver.NoAnswer:
        return None
    except Exception as e:
        print(f"Error getting MX record: {e}")
        return None

def check_email_active(email):
    """Check if the given email address is active using SMTP without sending an email."""
    try:
        # Split the email to get the domain part
        domain = email.split('@')[1]

        # Get the MX record for the domain
        mx_record = get_mx_record(domain)
        if not mx_record:
            return False, f"MX record not found for domain: {domain}"

        # Establish an SMTP connection to the mail server
        server = smtplib.SMTP(timeout=10)
        
        # Try different SMTP ports (25, 587, 465)
        try:
            server.connect(mx_record, 25)  # Standard SMTP port
        except (socket.error, smtplib.SMTPConnectError):
            print("Port 25 blocked or failed, trying port 587.")
            try:
                server.connect(mx_record, 587)  # Alternative SMTP port
            except (socket.error, smtplib.SMTPConnectError):
                print("Port 587 failed, trying port 465 (SSL).")
                try:
                    server = smtplib.SMTP_SSL(mx_record, 465)  # SSL SMTP port
                except Exception as e:
                    return False, f"All SMTP connection attempts failed: {e}"

        server.set_debuglevel(1)  # Set to 1 to see detailed SMTP communication

        # Greet the mail server
        server.ehlo()
        
        # Set the email address we're "sending" from (can be a fake address)
        sender_email = 'your-email@example.com'
        server.mail(sender_email)

        # Check if the recipient email is valid
        code, message = server.rcpt(email)

        # Close the connection
        server.quit()

        # Check the SMTP response code (250 means accepted, others are rejected)
        if code == 250:
            return True, "Email is valid and active."
        else:
            return False, f"Email is inactive or rejected (Code: {code}, Message: {message})"

    except Exception as e:
        return False, f"An error occurred: {e}"

# Example usage
email = "example@example.com"
is_active, result_message = check_email_active(email)
print(f"Is the email active? {is_active} - {result_message}")



