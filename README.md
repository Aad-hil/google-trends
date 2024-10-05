---
# Google Trends "Trending Now" Data Scraper

This project automates the process of scraping trending topics from [Google Trends](https://trends.google.com/trends/trendingsearches/daily) and stores the data in an Excel file. It is built using **Python** and **Selenium WebDriver**, allowing users to track popular search trends over time with ease.

## Features

- **Automated Scraping**: The script automatically opens Google Trends, scrapes the current "Trending Now" topics, and stores them in a local Excel file.
  
- **Timestamped Entries**: Each scraped trend is recorded with a timestamp, indicating when the data was collected, helping you analyze trends over time.

- **Excel File Management**: Instead of overwriting the file, the new data is appended to the **top** of the existing data. This ensures that the latest trends are always shown first in the file (`trending_now_titles.xlsx`).

- **Efficient Workflow**: With Selenium WebDriver, the process of visiting the website, extracting information, and updating the Excel file is fully automated.

## Requirements

- Python 3.x
- Selenium WebDriver
- Pandas
- OpenPyXL (for working with Excel files)

You can install the required Python libraries using:

```bash
pip install selenium pandas openpyxl
```

## Setup & Usage

1. **Clone the repository**:

```bash
git clone https://github.com/your-username/google-trends-scraper.git
```

2. **Install the dependencies**:
```bash
pip install -r requirements.txt
```

3. **Download ChromeDriver**: Make sure to have [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) installed, and ensure the version matches your installed version of Chrome.

4. **Run the script**:
```bash
python trends_scraper.py
```

The script will:
- Open a Chrome browser window and navigate to Google Trends.
- Scrape the current "Trending Now" titles.
- Append the data to an Excel file (`trending_now_titles.xlsx`), adding a timestamp to each trend entry.

## Example Output

The output Excel file (`trending_now_titles.xlsx`) will look something like this:

| Trending Now Titles                | Timestamp           |
|------------------------------------|---------------------|
| Example Trend Title 1              | 2024-10-04 12:00:00 |
| Example Trend Title 2              | 2024-10-04 12:00:00 |
| ...                                | ...                 |

## Contributing

Feel free to contribute! Fork the repo, make your changes, and submit a pull request.
---
