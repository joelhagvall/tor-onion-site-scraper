# Tor Onion Site Scraper

This repository contains a Python-based scraper tool for fetching and saving content from .onion sites accessible via the Tor network. Developed by Joel Hägvall and Giancarlo Valverde, this scraper is designed to navigate through multiple pages of each .onion site and store the HTML content in an organized manner, respecting the structure and navigation of the sites.

## Features

- Fetch HTML content of .onion websites using Tor as a proxy.
- Navigate and download multiple pages from each site.
- Save each page in a separate directory corresponding to its .onion site.
- Handle pagination and internal site links automatically.
- Maintain privacy and anonymity features provided by the Tor network.

## Prerequisites

Before you start using this scraper, you need to have the following installed on your system:
- Python 3.6 or higher
- Tor Browser or Tor service running in the background
- Required Python libraries: `requests`, `pysocks`, `beautifulsoup4`

## Installation

1. **Clone the Repository**

git clone https://github.com/yourusername/tor-onion-scraper.git
cd tor-onion-scraper


2. **Install Dependencies**
pip install -r requirements.txt


3. **Ensure Tor is Running**
- Make sure Tor is active in the background. If using Tor Browser, keep it open while the scraper runs.

## Usage

To start scraping .onion sites:

1. **Edit the `urls` list in `scraper.py`**
- Add the .onion URLs you intend to scrape to the list.

2. **Run the Scraper**
python scraper.py


3. **Check Output**
- Navigate to the `onion_sites_html` directory to see the downloaded HTML files organized by site.

## Contributing

Contributions are welcome! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

- **Joel Hägvall** - _Initial Work_
- **Giancarlo Valverde** - _Further Development_

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Thanks to the Tor Project for providing the tools that make this type of anonymous communication possible.
