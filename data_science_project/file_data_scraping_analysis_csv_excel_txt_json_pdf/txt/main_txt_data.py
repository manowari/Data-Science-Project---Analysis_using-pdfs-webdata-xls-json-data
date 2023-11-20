# main_txt_data.py
from txt_data import read_txt_file, clean_and_format_txt_data, analyze_txt_data

if __name__ == "__main__":
    txt_file_path = "data_science_project/data_txt/sample.txt"

    # Read TXT file
    txt_data = read_txt_file(txt_file_path)

    # Clean and format TXT data
    cleaned_and_formatted_txt_data = clean_and_format_txt_data(txt_data)

    # Analyze TXT data
    result = analyze_txt_data(cleaned_and_formatted_txt_data)

    print("\nAnalysis Result:")
    print(result)
