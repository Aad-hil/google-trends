from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from datetime import datetime
import os

# Set up Selenium options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# Open Google Trends "Trending Now" page
driver.get("https://trends.google.com/trends/trendingsearches/daily")


# Define a function to scrape "Trending Now" titles
def scrape_trending_now():
    try:
        # Wait for the trending now section to load and select the trend titles
        trending_section = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'mZ3RIc'))
        )

        # Scrape trending titles
        trending_titles = [trend.text for trend in trending_section]

        # Add a timestamp for when the data is collected
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        trending_data = {'Timestamp': timestamp, 'Trending Titles': trending_titles}

        return trending_data

    except Exception as e:
        print(f"Error scraping trending now titles: {str(e)}")
        return None


# Scrape the trending titles
trending_data = scrape_trending_now()

# Define the Excel file path
file_path = "trending_now_titles.xlsx"

# If we successfully scraped data, update the Excel file
if trending_data:
    # Convert the new data into a DataFrame
    df_new = pd.DataFrame(trending_data['Trending Titles'], columns=['Trending Now Titles'])
    df_new['Timestamp'] = trending_data['Timestamp']

    # Check if the Excel file already exists
    if os.path.exists(file_path):
        # Load the existing Excel file
        df_existing = pd.read_excel(file_path)

        # Append new data to the existing DataFrame
        df_updated = pd.concat([ df_new,df_existing], ignore_index=True)
    else:
        # If the file doesn't exist, just use the new data
        df_updated = df_new

    # Save the updated DataFrame back to the same Excel file
    df_updated.to_excel(file_path, index=False)
    print("Trending Now titles report updated successfully!")

# Close the browser
driver.quit()
