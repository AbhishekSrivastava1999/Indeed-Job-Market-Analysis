import pandas as pd

def analyze_data():
    # Load the cleaned dataset
    data = pd.read_csv('../data/final_cleaned_jobs.csv')

    # Job title summary
    job_title_summary = data['job_title'].value_counts().reset_index()
    job_title_summary.columns = ['Job Title', 'Count']

    # Location summary
    location_summary = data['Cleaned_Location'].value_counts().reset_index()
    location_summary.columns = ['Location', 'Count']

    # Company summary
    company_summary = data['Cleaned_Company'].value_counts().reset_index()
    company_summary.columns = ['Company', 'Count']

    # Output summaries
    print("Job Title Summary:")
    print(job_title_summary.head(10))

    print("\nLocation Summary:")
    print(location_summary.head(10))

    print("\nCompany Summary:")
    print(company_summary.head(10))

    # Save summaries as separate files for visualization
    job_title_summary.to_csv('../data/job_title_summary.csv', index=False)
    location_summary.to_csv('../data/location_summary.csv', index=False)
    company_summary.to_csv('../data/company_summary.csv', index=False)
    print("\nSummaries saved as CSV files.")

# Run the analysis
if __name__ == "__main__":
    analyze_data()
