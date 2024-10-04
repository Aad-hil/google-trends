from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

# Set up Selenium options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in the background

# Set up ChromeDriver path
chrome_service = Service('path/to/chromedriver')

# Keywords to monitor
keywords = ["AI", "Python programming", "Climate change"]

# Start ChromeDriver session
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Open Google Trends
driver.get("https://trends.google.com/trends/")

def monitor_trends(keyword):
    # Locate the search box and search the keyword
    search_box = driver.find_element(By.CLASS_NAME, 'input')
    search_box.clear()
    search_box.send_keys(keyword)
    search_box.send_keys(Keys.ENTER)
    time.sleep(2)  # Wait for page load

    # Scrape trending data
    trend_elements = driver.find_elements(By.CLASS_NAME, 'list-item-title')
    trends = [trend.text for trend in trend_elements]
    return trends

# Loop through keywords and scrape data
trend_data = {}
for keyword in keywords:
    print(f"Monitoring trends for: {keyword}")
    trends = monitor_trends(keyword)
    trend_data[keyword] = trends

# Convert the data into a DataFrame
trend_df = pd.DataFrame.from_dict(trend_data, orient='index').transpose()

# Save the results to an Excel file
trend_df.to_excel("trends_report.xlsx", index=False)
print("Trends report generated successfully!")

# Close the browser
driver.quit()
