# E-Commerce Sales Data Engineering Pipeline Using Databricks

## Project Overview

This project focuses on building an E-Commerce Sales Data Engineering Pipeline using Databricks and PySpark.

The pipeline processes daily order-export CSV files and transforms raw data into clean, structured, and business-ready datasets using Medallion Architecture.

## Technologies Used

- Databricks
- Python
- PySpark
- Lakeflow Spark Declarative Pipelines (SDP)
- Auto Loader
- Delta Tables
- Medallion Architecture

## Architecture

The project follows the Medallion Architecture with three layers:

### 1. Bronze Layer
- Ingests daily E-Commerce order CSV files using Auto Loader.
- Stores raw source records.
- Adds ingestion metadata columns.
- Implements initial acceptance checks.

**Output:** `bronze_orders_sdp`

### 2. Silver Layer
- Cleans and standardizes source data.
- Handles blank values and converts them into NULL.
- Performs data type conversions.
- Calculates order amounts.
- Applies business validation rules.
- Separates rejected records.

**Output:**
- `silver_orders`
- `silver_orders_rejected`

### 3. Gold Layer
Prepares business-level aggregations from validated order data.

Implemented aggregations include:
- City-wise sales – `gold_city_sales`
- Category-wise sales – `gold_category_sales`
- Product-wise sales – `gold_product_sales`
- Payment analysis – `gold_payment_analysis`

Order summary and overall sales summary are planned extensions.

## Pipeline Workflow

1. Ingest daily CSV files into the Bronze layer.
2. Clean and validate data in the Silver layer.
3. Separate valid and rejected records.
4. Prepare Gold-layer business aggregations.
5. Generate datasets for sales analysis.

## Repository Structure

```text
ecommerce-sales-data-engineering/
│
├── README.md
├── notebooks/
│   ├── 01_bronze_layer.py
│   ├── 02_silver_layer.py
│   └── 03_gold_layer.py
├── docs/
└── screenshots/
```

## Key Learnings

- Working with Databricks and PySpark.
- Implementing Auto Loader for data ingestion.
- Understanding Medallion Architecture.
- Building data transformation pipelines.
- Performing data cleaning and validation.
- Creating business-level aggregations.

## Project Status

Bronze and Silver layer implementations are completed. Gold city, category, product, and payment aggregations have been developed. Additional Gold summary tables remain planned.



