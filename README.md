# 📊 Indeed Job Data Analysis

## 🔍 Overview

After searching for a Data Analyst role in Canada for over a year, I decided to take a data-driven approach to analyze job market trends. This project uses data from **Indeed job postings** to extract insights into hiring trends, top locations, in-demand skills, and work mode distributions.

The goal of this project is to leverage data analytics to understand the job market better and enhance my skills in **Python, SQL, and Power BI**.

## 🚀 Key Insights

- **Top Hiring Cities**: Toronto, Vancouver, and Mississauga have the highest job postings.
- **Most In-Demand Roles**: "Business Analyst" and "Data Analyst" dominate job postings.
- **Work Mode Distribution**:
  - **On-site**: Majority of job postings (~63%)
  - **Hybrid**: Growing trend (~27%)
  - **Remote**: Only ~9.8% of job listings are remote
- **Top Hiring Companies**: ATB Financial, Loblaw, and McAfee, among others.

## 🔧 Tools & Technologies Used

- **Python** (Selenium, Pandas, NumPy) – Web scraping, data cleaning, and preprocessing
- **SQL** – Data structuring and querying
- **Power BI** – Data visualization and interactive dashboard creation
- **Excel** – Data verification and quick calculations

## 📂 Project Structure

```
Indeed-Job-Analysis/
│── data/                   # Raw and cleaned job data
│   ├── indeed_jobs.csv      # Raw scraped data
│   ├── final_cleaned_jobs.csv # Cleaned job postings
│   ├── location_summary.csv  # Summary of job locations
│   ├── company_summary.csv   # Summary of hiring companies
│
│── scripts/                # Python scripts for scraping & cleaning
│   ├── web_scraper.py       # Scrapes job postings from Indeed
│   ├── data_cleaning.py     # Cleans and processes the raw data
│   ├── sql_queries.sql      # SQL queries for data analysis
│
│── visualizations/         # Power BI and report files
│   ├── indeed_dashboard.pbix # Power BI dashboard
│
│── README.md               # Project documentation
│── Requirements.txt        # Required Python libraries
```

## 📈 Power BI Dashboard

The interactive Power BI dashboard provides insights into job postings, work mode distribution, and hiring trends.

🔗 **View Dashboard (If Published)**: [Power BI Report Link]

## 🛠 How to Run the Project

1. **Clone this repository:**
   ```sh
   git clone https://github.com/yourusername/Indeed-Job-Analysis.git
   cd Indeed-Job-Analysis
   ```

2. **Install dependencies:**
   ```sh
   pip install -r Requirements.txt
   ```

3. **Run the web scraper:**
   ```sh
   python scripts/web_scraper.py
   ```
   *(Make sure to configure Selenium properly if scraping new data.)*

4. **Clean and preprocess the data:**
   ```sh
   python scripts/data_cleaning.py
   ```

5. **Analyze the data using SQL:**
   ```sh
   sqlite3 database.db < scripts/sql_queries.sql
   ```

6. **Visualize the data:**
   - Open `indeed_dashboard.pbix` in Power BI
   - Refresh the data connections

## 💡 Future Improvements

- Automate data updates with scheduled scraping
- Include job descriptions for deeper text analysis
- Integrate salary trends into analysis

## 🤝 Connect with Me

If you're a **recruiter, hiring manager, or fellow job seeker**, let’s connect! I'm actively looking for a **Data Analyst** role and open to discussing insights from this project.

📧 **Email**: abhisheksrivastava613@gmail.com  
🔗 **LinkedIn**: [linkedin.com/in/abhishek-srivastava1999](https://www.linkedin.com/in/abhishek-srivastava1999/)  
💻 **GitHub**: [github.com/AbhishekSrivastava1999](https://github.com/AbhishekSrivastava1999/)

---

### ⭐ If you found this project useful, consider giving it a **star** on GitHub!

#DataAnalytics #PowerBI #Python #JobMarket #CareerGrowth #DataVisualization
