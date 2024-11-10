import pandas as pd


def detect_outliers(sampled_data):
    """
    Detects outliers in the stock price data based on a threshold of 2 standard deviations.

    Parameters:
    - sampled_data (DataFrame): DataFrame containing 30 consecutive stock data points.

    Returns:
    - DataFrame: A DataFrame with outliers containing columns:
      'Stock-ID', 'Timestamp', 'Stock Price', 'Mean Price', 'Deviation', '% Deviation'.
    """
    try:
        # Calculate the mean and standard deviation of the 'Stock Price' column
        mean_price = sampled_data['Stock Price'].mean()
        std_dev = sampled_data['Stock Price'].std()

        # Define the outlier threshold (2 standard deviations from the mean)
        threshold = 2 * std_dev

        # Identify outliers as values outside 2 standard deviations from the mean
        outliers = sampled_data[
            (sampled_data['Stock Price'] > mean_price + threshold) |
            (sampled_data['Stock Price'] < mean_price - threshold)
            ].copy()
        print("outliers")
        if outliers.empty:
            print("No outliers found in the data.")
            return None

        # Calculate deviation and % deviation for each outlier
        outliers['Mean Price'] = mean_price
        outliers['Deviation'] = outliers['Stock Price'] - mean_price
        outliers['% Deviation'] = (outliers['Deviation'].abs() / threshold) * 100

        return outliers[['Stock-ID', 'Timestamp', 'Stock Price', 'Mean Price', 'Deviation', '% Deviation']]

    except Exception as e:
        print(f"Error during outlier detection: {e}")
        return None
