# main_json_data.py
from json_data import read_json_file, clean_and_format_json_data, analyze_json_data

if __name__ == "__main__":
    json_file_path = "data_science_project/data_json/sample.json"

    # Read JSON file
    json_data = read_json_file(json_file_path)

    # Clean and format JSON data
    cleaned_and_formatted_json_data = clean_and_format_json_data(json_data)

    # Analyze JSON data
    result = analyze_json_data(cleaned_and_formatted_json_data)

    print("\nAnalysis Result:")
    print(result)
