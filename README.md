## World Population Scraper (Worldometers.info)

A Python-based scraper to collect global population statistics from [Worldometers.info](https://www.worldometers.info/world-population/population-by-country/). This project automates the process of gathering up-to-date demographic and geographic data and exports it to Excel.

## Features

- Scrapes the latest world population data
- Extracts key fields like:
  - Country
  - Population (2025)
  - Yearly Change
  - Net Change
  - Density (P/Km²)
  - Land Area
  - Migrants (net)
  - Fertility Rate
  - Median Age
  - Urban Population %
  - World Share
- Saves the data into an Excel file (with the current date in the filename)


## Tools Used

- Python
- Selenium
- WebDriver Manager
- pandas
- Excel (via openpyxl)


## Installation

Install the required packages:

```bash
pip install selenium webdriver-manager pandas openpyxl
```

## Usage

python world_population_scraper.py

## Screenshot

![Population Metrics from Worldometers]
(Population%20Metrics%20from%20Worldometers.info.png)


## Output

This will open the website, scrape the data, and save an Excel file named like:
worldmeters_2025-07-23.xlsx


