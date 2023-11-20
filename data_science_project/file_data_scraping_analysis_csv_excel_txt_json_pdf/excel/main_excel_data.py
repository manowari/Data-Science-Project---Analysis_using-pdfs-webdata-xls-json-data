# main_excel_data.py
from excel_data import read_excel_file, clean_and_format_excel_data, analyze_excel_data

if __name__ == "__main__":
    excel_file_path = "data_science_project/data_excel/sample.xlsx"

    # Read Excel file
    excel_data = read_excel_file(excel_file_path)

    # Clean and format Excel data
    cleaned_and_formatted_excel_data = clean_and_format_excel_data(excel_data)

    # Analyze Excel data
    result = analyze_excel_data(cleaned_and_formatted_excel_data)

    print("\nAnalysis Result:")
    print(result)
