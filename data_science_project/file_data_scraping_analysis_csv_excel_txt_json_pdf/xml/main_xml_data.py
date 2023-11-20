# main_xml_data.py
from xml_data import read_xml_file, clean_and_format_xml_data, analyze_xml_data

if __name__ == "__main__":
    xml_file_path = "data_science_project/data_xml/sample.xml"

    # Read XML file
    xml_data = read_xml_file(xml_file_path)

    # Clean and format XML data
    cleaned_and_formatted_xml_data = clean_and_format_xml_data(xml_data)

    # Analyze XML data
    result = analyze_xml_data(cleaned_and_formatted_xml_data)

    print("\nAnalysis Result:")
    print(result)
