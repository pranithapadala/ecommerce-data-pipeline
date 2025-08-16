# E-Commerce Analytics Batch Processing Pipeline

This project implements a complete, end-to-end batch processing pipeline for e-commerce analytics. It processes raw clickstream data into clean, aggregated datasets ready for reporting and decision-making. The entire workflow, from raw data ingestion to a final interactive web dashboard, is built using Python, SQL, dbt, Git, and AWS S3.

## 📊 Interactive Dashboard Preview

The final output of this pipeline is a live analytics dashboard built with Flask and Chart.js, which visualizes key business metrics directly from the transformed data.

*(**Action Required:** Take a high-quality screenshot of your final, polished dashboard and replace the placeholder below. This is the most important visual in your portfolio!)*

<p align="center">
  <img src="YOUR_SCREENSHOT_URL_HERE" alt="Dashboard Preview" width="800"/>
</p>

---

## 🚀 How to Run This Project

### Prerequisites
*   Python 3.8+
*   An AWS account with configured credentials (`aws configure`)
*   An AWS S3 bucket
*   dbt (Data Build Tool)

---

## 📌 Key Features & What I Did
* Data Ingestion and Cloud Storage:
Developed a Python script (upload_to_s3.py) to simulate the daily ingestion of raw clickstream data (events.csv) into a structured data lake on AWS S3.
*Data Transformation and Modeling with dbt:
Built a robust staging model in Python (stg_events.py) to reliably extract data from S3, cleaning and normalizing the raw events.
Developed SQL-based data marts for transactions, users, and products, transforming the staged data into analysis-ready dimensional models.
Applied transformations to standardize data types, handle duplicates, and aggregate data to derive meaningful metrics like daily transaction counts and user activity.
*Data Quality Assurance:
Implemented data quality checks using dbt's schema.yml to enforce not null and unique constraints, ensuring the integrity and reliability of the final datasets.
Used a failed test to diagnose an issue with duplicate transaction IDs and refined the transformation logic to fix it, demonstrating a full data debugging cycle.
*Data Export for Downstream Use:
Developed a Python script (export_to_s3.py) to export the clean, transformed tables from the DuckDB data warehouse back to AWS S3, making them available for other teams or services.
*Interactive Analytics Dashboard:
Built a lightweight web application using Flask to serve the transformed data through a REST API.
Developed a dynamic frontend with HTML, CSS, and Chart.js to create interactive visualizations.

---
## 🛠️ Technology Stack
Scripting & Backend: Python
Cloud Storage: AWS S3
Data Transformation: dbt, SQL
Data Warehouse: DuckDB
Web Framework: Flask
Frontend Visualization: Chart.js, HTML, CSS
Version Control: Git / GitHub

---

flowchart TD
    A["<b>events.csv</b><br/>(Local Raw Data)"] --> B["<b>upload_to_s3.py</b><br/>(Ingest to AWS S3)"]
    B --> C["<b>stg_events.py</b><br/>(dbt Staging Model in Python)"]
    C --> D["<b>SQL Marts</b><br/>(dbt Transformation)"]
    D --> E["<b>ecommerce.duckdb</b><br/>(Local Data Warehouse)"]
    E --> F["<b>export_to_s3.py</b><br/>(Export Clean Data to S3)"]
    E --> G["<b>Flask Web App</b><br/>(Serve Data via API)"]
    G --> H["<b>Interactive Dashboard</b><br/>(Browser Visualization)"]

---
## 🚀 Outcome & Impact
* Successfully built a full, end-to-end batch processing pipeline, demonstrating a comprehensive understanding of the modern data engineering lifecycle.
* Created a robust, scalable, and maintainable workflow from raw data ingestion to an interactive dashboard.
* Showcased the ability to integrate a wide range of tools, including cloud storage (AWS S3), a modern data warehouse (DuckDB), industry-standard transformation tooling (dbt), and web development frameworks (Flask).







