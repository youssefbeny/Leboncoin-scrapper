# Leboncoin Scraper

A Python script to scrape listings from **Leboncoin.fr** based on keywords, max price, and category, saving results to Excel and sending email alerts for new listings.

## Features
- Scrapes listings with pagination (default: 5 pages).
- Filters by keywords, max price, and category.
- Saves listings to `annonces_leboncoin.xlsx`.
- Tracks viewed listings in `seen_links.txt`.
- Sends email alerts via Gmail for new listings.
- Runs every 10 minutes (configurable).

## Prerequisites
- **Python 3.7+**
- Libraries: `requests`, `beautifulsoup4`, `pandas`, `openpyxl`
- Gmail account with an **app password** (see [Configure Gmail](#configure-gmail)).

## Installation
1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/leboncoin-scraper.git
   cd leboncoin-scraper
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create `requirements.txt`:
   ```
   requests==2.32.3
   beautifulsoup4==4.12.3
   pandas==2.2.3
   openpyxl==3.1.5
   ```

## Configure Gmail
1. Enable **two-factor authentication** on your Gmail account.
2. Go to [Google Account Security](https://myaccount.google.com/security).
3. Select **App passwords**, generate one for "Mail," and note it down (`EMAIL_PASSWORD`).

## Usage
1. Run the script:
   ```bash
   python leboncoin_scraper.py
   ```

2. Enter:
   - Receiver email (`EMAIL_RECEIVER`).
   - Search keywords (e.g., `used car`).
   - Max price (e.g., `5000`).
   - Category (e.g., `voitures`).
   - Sender Gmail (`EMAIL_SENDER`).
   - Gmail app password (`EMAIL_PASSWORD`).

3. The script scrapes every 10 minutes, saves to `annonces_leboncoin.xlsx`, and emails new listings.

## Generated Files
- `annonces_leboncoin.xlsx`: All scraped listings (title, price, link).
- `seen_links.txt`: Tracks viewed listing links.

## Customization
- `MAX_PAGES`: Pages to scrape (default: 5).
- `INTERVAL`: Scan interval in seconds (default: 600).

## Warnings
- Respect Leboncoin.fr's terms to avoid IP bans.
- 2-second delay between requests to prevent blocks.
- Do not share your Gmail app password publicly.

## Troubleshooting
- **403/429 Errors**: Increase delay (`time.sleep`) or use a proxy.
- **JSON Error**: Check if Leboncoin's structure changed.
- **Email Issues**: Verify Gmail app password and two-factor authentication.

## Contributing
1. Fork the repo.
2. Create a branch (`git checkout -b feature/new-feature`).
3. Commit changes (`git commit -m "Add feature"`).
4. Push branch (`git push origin feature/new-feature`).
5. Open a Pull Request.

## License
MIT License. See [LICENSE](LICENSE).

## Contact
For issues, contact [y.benyedder06@gmail.com](mailto:y.benyedder06@gmail.com).

---

### Notes
- Replace `https://github.com/your-username/leboncoin-scraper.git` with your actual repo URL.
- Include `requirements.txt` in your repository.
- Test locally before publishing.
- Let me know if you need further tweaks!