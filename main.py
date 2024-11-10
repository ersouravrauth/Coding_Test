import os
from TC2.sample_data import sample_data
from TC2.detect_outliers import detect_outliers


def process_files(num_files):
    # List all CSV files in the input folder
    input_folder = 'input'
    output_folder = 'output'
    all_files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]

    # If fewer files are available, process the available files
    files_to_process = all_files[:num_files] if len(all_files) >= num_files else all_files

    if not files_to_process:
        print("No files found in the input folder.")
        return

    # Process each file
    for file_name in files_to_process:
        file_path = os.path.join(input_folder, file_name)

        # Sample 30 data points
        sampled_data = sample_data(file_path)
        print(sampled_data)
        if sampled_data is not None:
            # Detect outliers
            outliers = detect_outliers(sampled_data)

            if outliers is not None:
                # Save the outliers to a CSV file in the output folder
                output_file_path = os.path.join(output_folder, f"outliers_{file_name}")
                outliers.to_csv(output_file_path, index=False)
                print(f"Outliers detected and saved for {file_name}.")


if __name__ == "__main__":
    # Example: process 2 files (can be changed based on input)
    process_files(2)
