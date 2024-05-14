# Tor Onion Site Scraper 

This repository hosts a Python-based scraper developed to retrieve HTML files based on URLs accessible via the Tor network. The scraper is developed by Joel Hägvall and Giancarlo Valverde.

## 📝 Features

- Saves HTML data based on URL, using Tor as a proxy.
- Retrieves titles and descriptions from the HTML files located in a specified directory.
- Saves the extracted data in a CSV file.
- Plot occurrences of keywords.

## 📦 Prerequisites

Before utilizing this scraper, ensure the following dependencies are installed on your system:
- Python 3.6 or higher
- Tor Browser or Tor service running in the background
- Required Python libraries: `requests`, `pysocks`, `beautifulsoup4`, `pandas`, `matplotlib`

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

    - Upon completion, the scraper will generate a CSV file containing titles and descriptions from the specified category, along with a directory name based on the category. Repeat this step for all categories that you want to scrape.

4. **Merge CSVs**
    - Given all CSV-files created, execute the `mergeCsv.py` file and a `merged_data.csv` will be created that is now the final dataset.
  
5. **Plotting**
   - Located in the `visual` folder, edit the `visualBarKeywordFreq.py` script and paste relevant keywords. Execute the script and the bar plot will show. The `visualPieKeywordFreq.py` works similar but returns a pie chart instead.

## Contributing



## Authors

- **Joel Hägvall** - _Developer_
- **Giancarlo Valverde** - _Developer_

## License



## Acknowledgments


