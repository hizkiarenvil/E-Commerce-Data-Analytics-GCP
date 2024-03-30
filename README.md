# E-Commerce-Data-Analytics-GCP || Data Engineer End-to-End Project

![Project Architecture](https://github.com/hizkiarenvil/E-Commerce-Data-Analytics-GCP/raw/main/e-commerce-gcp-data-analytics/assets/Project%20Architecture.jpeg)


This repository contains the code for a data engineering project that involves uploading a CSV file to Google Cloud Storage (GCS) and then loading it into a BigQuery table. The project also includes creating a dataset in BigQuery, processing the data within BigQuery, and delivering the data to be analyzed in Looker Studio.

## Project Details

The goal of this project is to demonstrate a data engineering pipeline for processing and analyzing e-commerce data. The pipeline consists of the following steps:

1. **Data Cleaning**: The CSV file containing e-commerce data is cleaned to handle missing values and remove duplicates.

2. **Cloud Storage Upload**: The cleaned CSV file is uploaded to Google Cloud Storage for storage and easy access.

3. **BigQuery Table Creation**: A dataset is created in Google BigQuery, and a table is defined to store the e-commerce data.

4. **Data Loading**: The cleaned data from Cloud Storage is loaded into the BigQuery table for analysis.

5. **Dashboard Creation**: Optionally, a dashboard can be created using visualization tools like Tableau to analyze sales and revenue trends.

## Requirements

- Python 3.x
- Google Cloud SDK
- Google Cloud Storage
- Google BigQuery

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/data-engineering-project.git
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up Google Cloud credentials by creating a service account key file and setting the environment variable `GOOGLE_APPLICATION_CREDENTIALS` to point to this file.

## Usage

1. Place your CSV file to be uploaded to Cloud Storage in the specified directory.

2. Run the `load.py` script to upload the CSV file to Cloud Storage and load it into BigQuery:

    ```bash
    python load.py
    ```

3. Check the BigQuery table to verify that the data has been loaded successfully.

4. Optionally, create a dashboard using visualization tools like Tableau to analyze sales and revenue trends.

## Configuration

- Modify the `load.py` script to customize the dataset and table names, as well as other configurations if needed.

## Credits

This project was created by [Your Name].

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
