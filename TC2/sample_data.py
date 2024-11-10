import pandas as pd
import random


def sample_data(file_path):
    """
    Reads a CSV file and selects 30 consecutive data points starting from a random timestamp.

    Parameters:
    - file_path (str): The path to the CSV file containing stock data.

    Returns:
    - DataFrame: A DataFrame containing 30 consecutive rows of data.
    - None: If the file is empty or has less than 30 data points.
    """
    try:
        # Read CSV file with date parsing for Timestamp column
        df = pd.read_csv(file_path, parse_dates=['Timestamp'], dayfirst=True)

        # Check if the file has at least 30 data points
        if df.empty or len(df) < 30:
            print(f"Error: {file_path} does not have enough data points (at least 30 required).")
            return None

        # Select a random starting point for a sequence of 30 consecutive rows
        start_idx = random.randint(0, len(df) - 30)
        sampled_data = df.iloc[start_idx:start_idx + 30].copy()

        return sampled_data

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None
