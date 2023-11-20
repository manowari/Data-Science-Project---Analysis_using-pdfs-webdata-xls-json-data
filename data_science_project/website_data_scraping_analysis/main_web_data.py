# main_web_data.py
from web_data import fetch_web_data, clean_and_format_web_data, analyze_web_data

if __name__ == "__main__":
    web_url = "https://example.com/api/data"
    
    # Fetch web data
    web_data = fetch_web_data(web_url)

    # Clean and format web data
    cleaned_and_formatted_web_data = clean_and_format_web_data(web_data)

    # Analyze web data
    result = analyze_web_data(cleaned_and_formatted_web_data)

    print("\nAnalysis Result:")
    print(result)
