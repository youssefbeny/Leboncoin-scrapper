# Leboncoin-scrapper
Leboncoin Scraper
This project is a Python script that scrapes listings from Leboncoin.fr based on specified criteria (keywords, maximum price, category) and sends email alerts for new listings. The results are also saved to an Excel file.
Features
Searches listings on Leboncoin.fr with pagination (up to 5 pages by default).
Filters by keywords, maximum price, and category.
Saves listings to an Excel file (annonces_leboncoin.xlsx).
Tracks viewed listings to avoid duplicates (stored in seen_links.txt).
Sends email alerts for new listings via a Gmail account.
Continuous monitoring with a configurable interval (10 minutes by default).
Prerequisites
To run this script, you need:
Python 3.7+
The following Python libraries:
requests
beautifulsoup4
pandas
openpyxl (for Excel export)
A Gmail account with an app password for sending emails (see Configure Gmail).
Installation
Clone the repository to your local machine:
git clone https://github.com/your-username/leboncoin-scraper.git
cd leboncoin-scraper
Create a virtual environment (recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install the dependencies:
pip install -r requirements.txt
Create a requirements.txt file with the following content to list dependencies:
requests==2.32.3
beautifulsoup4==4.12.3
pandas==2.2.3
openpyxl==3.1.5
Configure Gmail
To send emails, you need to set up a Gmail app password:
Enable two-factor authentication on your Gmail account.
Go to Manage your Google Account.
Under "Signing in to Google," select App passwords.
Generate an app password for "Mail" and note it down (this will be used as EMAIL_PASSWORD).
Usage
Run the script:
python leboncoin_scraper.py
Answer the interactive prompts to configure:
Your email for receiving alerts (EMAIL_RECEIVER).
Search keywords (e.g., used car).
Maximum price (e.g., 5000).
Category (e.g., voitures for cars).
Your Gmail address for sending emails (EMAIL_SENDER).
Your Gmail app password (EMAIL_PASSWORD).
The script scrapes listings every 10 minutes (configurable via INTERVAL) and:
Saves results to annonces_leboncoin.xlsx.
Stores viewed listing links in seen_links.txt.
Sends an email for each new listing detected.
Example Output
Configuration of the Leboncoin bot...
What is your email for receiving alerts? user@example.com
What is the title or keywords for the listing? used car
What is the maximum price? 5000
What is the category? voitures
What is your sender email? your-email@gmail.com
What is your Gmail app password? xxxxxxxxxxxxxxxx
Scan in progress...
Scraping page 1: https://www.leboncoin.fr/recherche?category=voitures&text=used%20car&price=0-5000
Table updated: annonces_leboncoin.xlsx
New listings found!
- Renault Clio 2010 | 4500 € | https://www.leboncoin.fr/ad/voitures/123456789
Email alert sent!
Generated Files
annonces_leboncoin.xlsx: Contains all scraped listings (title, price, link).
seen_links.txt: Stores links of viewed listings to avoid duplicates.
Customization
You can modify the following parameters in the script:
MAX_PAGES: Maximum number of pages to scrape (default: 5).
INTERVAL: Interval between scans in seconds (default: 600, or 10 minutes).
Warnings
Terms of Service: Ensure you comply with Leboncoin.fr's terms of use. Excessive scraping may lead to IP blocking.
Request Delay: A 2-second delay is added between page requests to avoid blocks.
Network Errors: The script handles HTTP and JSON errors, but check your criteria if no listings are found.
Security: Do not share your Gmail app password in a public repository.
Common Issues
Error 403/429: Leboncoin may block frequent requests. Increase the delay (time.sleep) or use a proxy.
JSON Script Not Found: The website structure may have changed. Check Leboncoin.fr's page source.
Email Error: Verify your Gmail app password and two-factor authentication settings.
Contributing
Contributions are welcome! To add features (e.g., advanced filters, other websites), follow these steps:
Fork the repository.
Create a branch (git checkout -b feature/new-feature).
Commit your changes (git commit -m "Add new feature").
Push your branch (git push origin feature/new-feature).
Open a Pull Request.
License
This project is licensed under the MIT License. See the LICENSE file for details.
Contact
For questions, open an issue on GitHub or contact me at y.benyedder06@gmail.com.
