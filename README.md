📊 Indeed Job Market Analysis: A Data-Driven Approach
🔍 Analyzing job postings to uncover trends in the Canadian job market

📌 Project Overview
Over the past year, I have been actively searching for a Data Analyst role in Canada. To gain better insights into the job market, I decided to analyze job postings from Indeed and identify key trends such as:

✅ Top hiring cities & companies
✅ Most in-demand job titles
✅ Work mode distribution (On-site, Remote, Hybrid)
✅ Job market trends & skill demand

This project helped me develop my data storytelling and visualization skills while providing a real-world perspective on job market trends.

📊 Key Insights
📍 Top Hiring Locations: Toronto, Vancouver, and Mississauga have the highest job postings.
📌 Most Common Roles: "Business Analyst" and "Data Analyst" are the most in-demand job titles.
🏠 Remote Jobs: Only ~9.8% of postings are remote, indicating a shift toward on-site/hybrid roles.

🛠 Tools & Technologies Used
🔹 Python (Selenium, Pandas, Regex) – Web scraping & data cleaning
🔹 SQL (PostgreSQL/MySQL) – Data structuring & querying
🔹 Power BI – Interactive dashboard & visual storytelling

📂 Project Structure
pgsql
Copy
Edit
📂 Indeed-Job-Market-Analysis  
 ├── 📜 README.md  → Overview of the project  
 ├── 📂 data  → Sample cleaned CSV files  
 ├── 📂 scripts  
 │   ├── scrape_jobs.py  → Web scraping with Selenium  
 │   ├── clean_jobs.py  → Data cleaning with Pandas & Regex  
 │   ├── analysis.sql  → SQL queries for structuring data  
 ├── 📂 dashboard  
 │   ├── PowerBI.pbix  → Power BI file  
📊 How to Run This Project
1️⃣ Clone this repository:
bash
Copy
Edit
git clone [GitHub Repo Link]
cd Indeed-Job-Market-Analysis
2️⃣ Install dependencies:
bash
Copy
Edit
pip install selenium pandas sqlalchemy
3️⃣ Run the web scraper to collect job postings:
bash
Copy
Edit
python scripts/scrape_jobs.py
4️⃣ Clean the data using:
bash
Copy
Edit
python scripts/clean_jobs.py
5️⃣ Use SQL queries to analyze the dataset:
sql
Copy
Edit
-- Example Query: Top 10 Hiring Companies
SELECT company, COUNT(*) AS job_count
FROM job_postings
GROUP BY company
ORDER BY job_count DESC
LIMIT 10;
6️⃣ Open the Power BI dashboard to explore insights!
Load the cleaned dataset into Power BI
Open PowerBI.pbix to view the interactive dashboard
📊 Power BI Dashboard Preview
🔗 [Power BI Interactive Dashboard](Power BI Link if published)

📂 Sample Data (CSV Files)
You can find sample datasets in the data/ folder to test and explore the project without running the scraper.

📢 Future Improvements
🚀 Expanding job analysis to multiple sources (LinkedIn, Glassdoor, etc.)
📊 Incorporating NLP to analyze job descriptions for required skills
🔍 Automating the entire workflow for real-time updates
