# main_csv_data.py
from csv_data import read_csv_file, clean_and_format_csv_data, analyze_csv_data

if __name__ == "__main__":
    csv_file_path = "data_science_project/data_csv/sample.csv"

    # Read CSV file
    csv_data = read_csv_file(csv_file_path)

    # Clean and format CSV data
    cleaned_and_formatted_csv_data = clean_and_format_csv_data(csv_data)

    # Analyze CSV data
    result = analyze_csv_data(cleaned_and_formatted_csv_data)

    print("\nAnalysis Result:")
    print(result)
