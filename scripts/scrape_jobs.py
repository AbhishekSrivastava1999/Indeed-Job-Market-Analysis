import undetected_chromedriver as uc
import pandas as pd
import time
import random
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException

# User agents for rotation
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Linux x86_64)"
]

def scrape_with_selenium(job_title="data analyst", location="Canada", max_pages=30):
    options = uc.ChromeOptions()
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--start-maximized")
    user_agent = random.choice(user_agents)
    options.add_argument(f"user-agent={user_agent}")

    try:
        driver = uc.Chrome(options=options)
    except WebDriverException as e:
        print(f"Error initializing the browser: {e}")
        return pd.DataFrame()

    base_url = f"https://ca.indeed.com/jobs?q={job_title}&l={location}&radius=100"
    all_jobs = []

    try:
        for page in range(max_pages):
            start = page * 10  # Calculate the start parameter for pagination
            url = f"{base_url}&start={start}"
            print(f"Fetching URL: {url}")

            driver.get(url)
            time.sleep(random.randint(5, 15))  # Add a random delay to avoid detection

            # Check for CAPTCHA
            try:
                captcha_present = driver.find_element(By.XPATH, "//div[contains(@class, 'captcha')]") or \
                                  driver.find_element(By.XPATH, "//iframe[contains(@src, 'captcha')]")

                if captcha_present:
                    print("CAPTCHA detected. Please solve it manually.")
                    input("Solve the CAPTCHA in the browser and press Enter to continue...")
                    continue
            except NoSuchElementException:
                # No CAPTCHA detected, proceed normally
                pass

            # Extract job cards
            try:
                job_cards = driver.find_elements(By.CSS_SELECTOR, "div.job_seen_beacon")
                print(f"Jobs found on current page: {len(job_cards)}")
            except NoSuchElementException:
                print("No job cards found. Exiting...")
                break

            for job_card in job_cards:
                try:
                    # Adjusted selectors based on site inspection
                    table = job_card.find_element(By.CSS_SELECTOR, "table.mainContentTable")
                    title = table.find_element(By.CSS_SELECTOR, "a.jcs-JobTitle").text.strip()

                    text_nodes = table.text.split("\n")
                    if len(text_nodes) >= 3:
                        company = text_nodes[1].strip()
                        location = text_nodes[2].strip()

                        # Ensure the location is valid (not a rating or random number)
                        if location and location[0].isdigit():  # Simple check for numeric location entries like '3.3'
                            location = "N/A"
                    else:
                        company = "N/A"
                        location = "N/A"

                    all_jobs.append({
                        "Job Title": title,
                        "Company": company,
                        "Location": location
                    })
                except Exception as e:
                    print(f"Error parsing job card: {e}")

            # Save data incrementally
            if all_jobs:
                pd.DataFrame(all_jobs).drop_duplicates().to_csv('./data/indeed_jobs_temp.csv', index=False)
                print("Data saved incrementally to indeed_jobs_temp.csv")

            # Long pause after every 10 pages
            if page % 10 == 0 and page > 0:
                print("Taking a longer break...")
                time.sleep(random.randint(60, 120))  # Pause for 1-2 minutes every 10 pages

    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        try:
            driver.quit()
        except OSError as e:
            if "WinError 6" in str(e):
                print("Browser session already closed.")

    if not all_jobs:
        print("No jobs were scraped. Check the website structure and CAPTCHA handling.")
    return pd.DataFrame(all_jobs)

if __name__ == "__main__":
    max_pages_to_scrape = int(input("Enter the maximum number of pages to scrape (e.g., 10, 20, 30): "))
    jobs_df = scrape_with_selenium(job_title="Data Analyst", location="Canada", max_pages=max_pages_to_scrape)
    if not jobs_df.empty:
        jobs_df = jobs_df.drop_duplicates()  # Remove duplicate entries
        print(jobs_df.head())
        jobs_df.to_csv('./data/indeed_jobs.csv', index=False)
        print("Scraped data saved to ./data/indeed_jobs.csv")
    else:
        print("No data to save.")
