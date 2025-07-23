# Worldometer Logo

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import datetime

# Setup WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Load the site

driver.get("https://www.worldometers.info/world-population/population-by-country/")

# Wait for the table to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "table.datatable-table"))
)

# Wait a bit more to ensure AJAX content is fully loaded
time.sleep(2)

table = driver.find_element(By.CSS_SELECTOR, "table.datatable-table")
rows = table.find_elements(By.TAG_NAME, "tr")

# Store data
data = []
for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    data.append([col.text for col in cols])

# Create DataFrame
df = pd.DataFrame(data, columns=["No", "Country (or Dependency)", "Population(2025)", "Yearly Change", "Net Change", "Density (P/Km²)", "Land Area (Km²)", "Migrants(net)", "Fert. Rate", "Median Age", "Urban Pop %", "World Share"])

# Save to Excel
filename = f"worldmeters_{datetime.date.today()}.xlsx"
df.to_excel(fr"D:\Python\New_folder\{filename}", index=False)
#df.to_excel(r"D:\Python\New_folder\worltmeters.xlsx", index=False) #without datetime

driver.quit()
print("✅ Data table scraped and saved!")