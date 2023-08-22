import requests
import re
from bs4 import BeautifulSoup

def get_social_links(soup):
    social_links = []
    social_patterns = [r'facebook\.com', r'twitter\.com', r'instagram\.com']

    for link in soup.find_all('a', href=True):
        for pattern in social_patterns:
            if re.search(pattern, link['href'], re.IGNORECASE):
                social_links.append(link['href'])
                break

    return social_links

def get_emails(text):
    email_pattern = r'\S+@\S+'
    emails = re.findall(email_pattern, text)
    return emails

def get_contact_numbers(text):
    contact_numbers = []
    contact_patterns = [
        r'\b\d{10}\b',             # 10-digit phone number
        r'\b\d{3}-\d{3}-\d{4}\b',  # XXX-XXX-XXXX format
        r'\b\(\d{3}\)\s*\d{3}-\d{4}\b',  # (XXX) XXX-XXXX format
        r'^\+?\d.\s?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}?'
    ]

    for pattern in contact_patterns:
        matches = re.findall(pattern, text)
        contact_numbers.extend(matches)

    return contact_numbers

def main():
    url = input("Enter the URL of the website: ")

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text()
        
        social_links = get_social_links(soup)
        emails = get_emails(text)
        contact_numbers = get_contact_numbers(text)

        print("Social Links:", social_links)
        print("Emails:", emails)
        print("Contact Numbers:", contact_numbers)
    else:
        print("Failed to retrieve the webpage.")

if __name__ == "__main__":
    main()

# Contact detail function is not working because syntax of contact is different for a various sites. I run the code for the site https://practice.geeksforgeeks.org/problem-of-the-day