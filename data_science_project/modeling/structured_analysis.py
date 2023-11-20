# structured_analysis.py
from modeling.statistics import calculate_mean, calculate_median, calculate_standard_deviation, calculate_variance, calculate_mode
import pandas as pd
from sklearn.linear_model import LinearRegression

def analyze_structured_data(data):
    # Replace this with your actual analysis for structured data

    # Placeholder: Extracted structured data (replace with your actual data extraction logic)
    df = pd.DataFrame(data)

    # Continuous Variables Analysis
    continuous_analysis_result = analyze_continuous_variables(df[['Age', 'Income']])

    # Categorical Variables Analysis
    categorical_analysis_result = analyze_categorical_variables(df['Category'])

    # Linear Regression
    regression_result = perform_linear_regression(df[['Age']], df['Income'])

    # Additional Statistical Analysis (if needed, otherwise, remove this line)
    additional_statistical_result = perform_additional_statistical_analysis(df['Income'])

    result = {
        'continuous_analysis': continuous_analysis_result,
        'categorical_analysis': categorical_analysis_result,
        'linear_regression': regression_result,
        'additional_statistical_analysis': additional_statistical_result
    }

    return result

def analyze_continuous_variables(continuous_data):
    # Calculate averages, deviations, variances, etc. for continuous variables
    mean = calculate_mean(continuous_data)
    median = calculate_median(continuous_data)
    std_deviation = calculate_standard_deviation(continuous_data)
    variance = calculate_variance(continuous_data)
    mode, mode_frequency = calculate_mode(continuous_data)

    result = {
        'mean': mean,
        'median': median,
        'standard_deviation': std_deviation,
        'variance': variance,
        'mode': mode,
        'mode_frequency': mode_frequency
    }

    return result

def analyze_categorical_variables(categorical_data):
    # Calculate counts for each category in categorical variables
    category_counts = categorical_data.value_counts().to_dict()

    result = {
        'category_counts': category_counts
    }

    return result

def perform_linear_regression(x, y):
    # Perform linear regression on continuous variables
    model = LinearRegression()
    model.fit(x, y)
    regression_coefficient = model.coef_[0]
    regression_intercept = model.intercept_

    result = {
        'coefficient': regression_coefficient.tolist(),
        'intercept': regression_intercept.tolist()
    }

    return result

def perform_additional_statistical_analysis(data):
    # Additional statistical analysis using functions from the modeling.statistics module
    additional_result = {
        'mean': calculate_mean(data),
        'median': calculate_median(data),
        'standard_deviation': calculate_standard_deviation(data),
        'variance': calculate_variance(data),
        'mode': calculate_mode(data)
    }

    return additional_result
