import pandas as pd

# Load your dataset
data = pd.read_csv('../data/filtered_jobs.csv')

# Function to clean the location column
def clean_location(row):
    if pd.isna(row) or row.strip() == '':
        return 'Unknown', 'Unknown'
    if 'Hybrid work in' in row:
        return 'Hybrid', row.replace('Hybrid work in ', '').strip()
    elif 'Remote' in row:
        return 'Remote', 'Remote'
    else:
        return 'On-site', row.strip()

# Function to clean the company column
def clean_company(row, location):
    if pd.isna(row) or row.strip() == '':
        return 'Unknown'
    
    row = row.strip()
    
    # If the company starts with "New,", use the location column for the correct company name
    if row == "New" and location.strip() != '':
        return location.strip()
    
    # Extract company name after "New," and clean it
    if row.startswith("New,"):
        parts = row.split(",", 1)  # Split at the first comma
        if len(parts) > 1:
            return parts[1].strip()  # Return the part after "New,"
        else:
            return "Unknown"
    
    # Return the cleaned company name
    return row

# Apply cleaning functions
data[['Mode', 'Cleaned_Location']] = data['location'].apply(
    lambda x: pd.Series(clean_location(x))
)
data['Cleaned_Company'] = data.apply(
    lambda x: clean_company(x['company'], x['location']), axis=1
)

# Ensure all job titles are valid
data['job_title'] = data['job_title'].apply(lambda x: x.strip() if pd.notna(x) else 'Unknown')

# Handle missing locations
data['location'] = data['location'].fillna('Unknown')

# Final check for missing values
if data.isnull().sum().sum() > 0:
    print("Warning: There are still missing values in the dataset.")
else:
    print("All missing values handled successfully.")

# Save the cleaned dataset
cleaned_file_path = '../data/final_cleaned_jobs.csv'
data.to_csv(cleaned_file_path, index=False)

# Output confirmation
print(f"Cleaned data saved to '{cleaned_file_path}'")
