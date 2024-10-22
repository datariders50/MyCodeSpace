Yes, there are Python libraries and approaches you can use to get company information based on an email domain. Below are some methods that can be useful:

1. Using whois Python Library

You can use the whois Python library to retrieve basic information about a domain. This is not as comprehensive as APIs like Clearbit, but it can provide useful details like the domain registrar and registration information.

pip install python-whois

import whois

def get_domain_info(domain):
    domain_info = whois.whois(domain)
    return domain_info

# Example usage
domain = 'example.com'
info = get_domain_info(domain)
print(info)

This gives you basic domain info, but it won’t return company-specific information like name or industry.

2. Using email-verifier Python Library

The email-verifier library allows you to verify email domains and get company information. This library interacts with third-party APIs (like Hunter.io), so it may still have limits, but you can handle it programmatically.

pip install email-verifier

from emailverifier import Client

# Get your API key from Hunter.io or any other service
api_key = 'your_api_key_here'

client = Client(api_key)
response = client.get('contact@example.com')

# Extract the company data from the response
if response['data']['domain']:
    company_info = response['data']['domain']['organization']
    print(company_info)

3. Using Scraping Techniques (BeautifulSoup & Requests)

If the domain has an accessible “About Us” page or similar, you could scrape the website for company information.

pip install beautifulsoup4 requests

import requests
from bs4 import BeautifulSoup

def get_company_info(domain):
    try:
        response = requests.get(f"http://{domain}")
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Example: Scrape title or meta description as company info
        title = soup.find('title').text
        description = soup.find('meta', attrs={'name': 'description'})
        
        return {
            "title": title,
            "description": description['content'] if description else "No description available"
        }
    except Exception as e:
        return {"error": str(e)}

# Example usage
domain = 'example.com'
info = get_company_info(domain)
print(info)

This method might not give you structured data but can pull information directly from the company’s website.

4. Using DNS Lookup

If you want to avoid paid services, you can use DNS records and whois data to infer information about the domain. Although this won’t always give you a company name, it can give you domain registrant information.

pip install dnspython

import dns.resolver

def get_mx_records(domain):
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        return [str(record.exchange) for record in mx_records]
    except Exception as e:
        return str(e)

# Example usage
domain = 'example.com'
mx_records = get_mx_records(domain)
print(mx_records)

5. Custom API Integration with Python Requests

If you need to integrate an external API like Hunter.io, FullContact, or Clearbit, you can use the requests library in Python. Here’s an example for Hunter.io.

pip install requests

import requests

def get_company_info_hunter(domain):
    api_key = 'your_hunter_io_api_key'
    url = f"https://api.hunter.io/v2/domain-search?domain={domain}&api_key={api_key}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Unable to fetch data"}

# Example usage
domain = 'example.com'
info = get_company_info_hunter(domain)
print(info)

Conclusion

	•	For a completely free solution, the whois and web scraping approaches are viable but limited.
	•	For more structured company information, you can use API services (e.g., Hunter.io, Clearbit) with their free tiers, but you’ll be limited by their usage caps.