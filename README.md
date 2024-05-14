# Tor Onion Site Scraper 

This repository hosts a Python-based scraper tailored to fetch titles and descriptions from .onion sites accessible via the Tor network. The scraper is developed by Joel Hägvall and Giancarlo Valverde.

## 📝 Features

- Retrieves titles and descriptions from .onion websites using Tor as a proxy.
- Saves the extracted data in a CSV file.
- Maintains privacy and anonymity features provided by the Tor network.

## 📦 Prerequisites

Before utilizing this scraper, ensure the following dependencies are installed on your system:
- Python 3.6 or higher
- Tor Browser or Tor service running in the background
- Required Python libraries: `requests`, `pysocks`, `beautifulsoup4`

## 🛠️ Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/tor-onion-scraper.git
    cd tor-onion-scraper
    ```

2. **Install Dependencies**


3. **Ensure Tor is Running**

    - Keep Tor active in the background. If using Tor Browser, keep it open while the scraper runs.

## 🚀 Usage

To start scraping .onion sites:

1. **Edit the `category` variable in `scrapeCategorySiteHTML.py`**
    - Set the `category` variable to the category you intend to scrape, our categories are provided in the `categoriesAndLinks.txt`.

2. **Run the Scraper**

    ```bash
    python scrapeCategorySiteHTML.py
    ```

3. **Check Output**

    - Upon completion, the scraper will generate a CSV file containing titles and descriptions from the specified category, along with a directory name based on the category.

## Contributing



## Authors

- **Joel Hägvall** - _Developer_
- **Giancarlo Valverde** - _Developer_

## License



## Acknowledgments


