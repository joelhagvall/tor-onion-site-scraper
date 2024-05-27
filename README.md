# Tor Onion Site Scraper 

This repository contains a Python-based scraper designed to collect HTML files from URLs accessible through the Tor network. The scraper was developed by Joel Hägvall and Giancarlo Valverde, with assistance from ChatGPT.

## 📝 Features

- Collects HTML data from URLs using Tor as a proxy.
- Retrieves titles and descriptions from the HTML files located in a specified directory.
- Gathers titles and stats to provide additional details about the listings.
- Stores the extracted data in CSV files.
- Plots the frequency of keywords.

## 📦 Prerequisites

Before utilizing this scraper, ensure the following dependencies are installed on your system:
- Python 3.6 or higher
- Tor Browser or Tor service running in the background
- Required Python libraries: `requests`, `pysocks`, `beautifulsoup4`, `pandas`, `matplotlib`

## 🛠️ Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/**yourusername**/tor-onion-scraper.git
    cd tor-onion-scraper
    ```

2. **Install Dependencies**

    - Install the required libraries using `pip`:

    ```bash
    pip install requests pysocks beautifulsoup4 pandas matplotlib
    ```

3. **Ensure Tor is Running**

    - Ensure Tor is active in the background. If you are using the Tor Browser, keep it open while the scraper runs.
## 🚀 Usage

Steps for Data Scraping and Content Analysis

1. **Prepare Category Scraping**
- Navigate to the scraping folder.
- Edit the _scrapeCategorySiteHTML.py_ script, updating the category array to match the first category to be scraped.
- Execute the script.
- A new directory "named new_onion_sites_html" is created, along with a subdirectory named after the category, containing its HTML files.
- Repeat this process for all 24 selected categories.

2. **Scrape Index Page**
- In the scraping folder, execute the _scrapeIndexSiteHTML.py script_.
- A new directory named faq is created within the new_onion_sites_html directory, containing all HTML files found on the "Help & Infos" page.

3. **Extract Category Elements**
- Open the _extractElementsHTMLCategory.py_ script in the scraping directory.
- Ensure all 24 categories are present in the categories array.
- Execute the script to generate CSV files in the "categoryPageTitleStats" directory. These files will contain the columns Title and Stats for each product in all categories.

4. **Extract Product Elements**
- Open the _extractElementsHTMLProduct.py_ script in the scraping folder.
- Update the categories array to include all 24 categories.
- Execute the script to create CSV files for all categories in the newly created "productPageResultsHTML" directory.

5. **Compile Product Data**
- Navigate to the "productPageResultsHTML" folder. 
- Ensure all CSV files are created for each category, containing elements such as Title, Description, Refund Policy, and Comments.

6. **Merge CSV Files**
- In the main directory, edit the _mergeCsv.py_ script.
- Update the "results_directory" array to "categoryPageTitleStats" and set the CSV filename to _categoryTitleStats.csv_.
- Execute the script to merge all CSV files in the directory.
- Repeat the process by updating the array to "productPageResultsHTML" and the CSV filename to _merged_data.csv_.

7. **Create Coding Scheme**
- Develop a table with categories representing the coding scheme for content analysis.
- Create subcategories and develop keywords for each subcategory.
- Add a Frequency column to track keyword frequencies and a Total column for the total count.

8. **Keyword Frequency Analysis**
- Extract keywords from the first subcategory of the first crime category and paste them into the _visualBarKeywordFreq.py_ script located in the visual folder, within the keywords array.
- Use the generated plot to record total frequencies in the table.
- Repeat this process for every subcategory of each category.

9. **Visualize Subcategory Frequencies**
- Open the _visualBarSubcategories.py_ script.
- Update the categories array to match all subcategories of the first crime category.
- Edit the frequencies array to match their respective frequencies.

10. **In-Depth Analysis**
- For each crime category, perform an in-depth analysis of listings related to the research question.
- Choose examples based on observations and the highest frequency subcategory.
- Use the site’s search function to find examples and extract statistics from the _categoryTitleStats.csv file_.


## Authors

- **Giancarlo Valverde** - _Developer_
- **Joel Hägvall** - _Developer_
- **ChatGPT** (OpenAI) - _Large Language Model_


## Disclaimer

Please note that this program is primarily developed for research purposes, particularly for our thesis. We do not support or endorse any illegal or unethical activities.


