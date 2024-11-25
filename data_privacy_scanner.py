import requests
from bs4 import BeautifulSoup

def fetch_website_content(url):
    try:
        # Make a HTTP request to the web site
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Check HTTP errors
    except requests.exceptions.RequestException as e:
        print(f"Error during the connection: {e}")
        return None

def analyze_privacy_terms(content):
    # Keywords to find in the text
    privacy_terms = ["privacy", "GDPR", "data protection", "cookies", "user data"]
    results = {term: content.lower().count(term) for term in privacy_terms}
    return results

def fetch_website_content(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Check HTTP errors
        #print(response.text)  # Stampa il contenuto della pagina
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error during the connection: {e}")
        return None


def main():
    print("Welcome into the Data Privacy Scanner!")
    url = input("Enter the URL to be analyzed (ex. https://example.com): ").strip()
    
    print("\n[INFO] Connection to the website..")
    content = fetch_website_content(url)
    
    if content:
        print("\n[INFO] Analyzing the content...")
        results = analyze_privacy_terms(content)
        
        print("\n--- Results of the analysis ---")
        for term, count in results.items():
            print(f"The term '{term}' appears {count} times.")
    else:
        print("Unable to analyze the content of the website.")

if __name__ == "__main__":
    main()
