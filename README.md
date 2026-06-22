An e-commerce machine learning data engineering pipeline to build reasonably good quality dataset to feed ai training applications.

This project demonstrates pipeline containing multiple stages (data acquisation, data processing, proudct annotation workflows and ML-ready dataset generation).

---------------------------------------------------------------------------------------------------------------------

## Overview

Building good quality dataset for computer vision system requires following multiple steps.

* Data acquisition
* Data cleaning and standardization
* Feature engineering
* Annotation workflows
* Dataset validation
* ML ready dataset preparation

This project tells us how these different steps can be integrated into unified data engineering pipeline for e-commerce product data.

---------------------------------------------------------------------------------------------------------------------

## Problem statement

Computer vision ai applications are dependent on good quality datasets. Prdoucing such datasets process has following challenges.

* Product data resides in multiple sources
* Raw data has to be cleaned and normalized
* Annotation systems must be well integrated with preprocessing pipeline
* Data has to be inspected before serving to ai applications

This repo demonstrates an end to end workflow for solving these challenges.

---------------------------------------------------------------------------------------------------------------------

## Pipeline architecture
<pre>
E-commerce product listings
            ↓
Scrapy-based data extraction
            ↓
Raw Dataset Collection
            ↓
Data Cleaning and Standardization
            ↓
Feature Engineering and Validation
            ↓
Label studio Annotation Pipeline
            ↓
Annotated Dataset Validation
            ↓
ML-Ready Dataset Output
</pre>
---------------------------------------------------------------------------------------------------------------------

## System components

### Data Acquisition Layer

Process of acquiring product listing data from e-commerce store (ebay)

#### Capabilities:

* Product listing Scraping workflow
     * Product metadata extraction
     * Image collection pipelines
* Structured raw dataset generation
     * Data extraction from web app listing raw data

#### TechStack:

* Python
* Scrapy
* bash scripting

---------------------------------------------------------------------------------------------------------------------

### Data processing layer

Transforms raw data into standardized data

#### Capabilities:

* Datasets cleaning
     * Images deduplication
     * Filtering unique set of ebay listing
* Normalization pipelines
     * good quality images filtering
* Data validation workflow
     * Images visual sampling and inspection

#### TechStack:

* Python
* Pandas
* Jupyter Notebooks

---------------------------------------------------------------------------------------------------------------------

### Annotation layer

Layer of data labeling workflow for machine learning systems

* Dataset annotation workflows
* Annotation automation
* Dataset export pipeline
* Dockerized annotation environment

#### TechStack:

* Labelstudio
* Docker
* Python
* Bash

---------------------------------------------------------------------------------------------------------------------

### Post annotation and data validation layer

Layer of scripts and notebooks to inspect, validate and curate annotated dataset.

* Annotation data parsers
* Annotators performance analysis
* Annotations visual sample inspection

#### TechStack:

* Python
* Plotly-dash
* Bash
* Pandas
* Json

---------------------------------------------------------------------------------------------------------------------

## Repository Structure
<pre>
ecommerce-ml-dataset-engineering-pipeline/
├── 00_pre_data_aquisition_stage
├── 01_scraping_layer
├── 02_data_processing_layer
├── 03_annotation_layer
├── 04_post_annotation_data_validation
├── 05_data_serving_layer
├── architecture
├── docs
├── README.md
├── sample_data
└── utils
</pre>
---------------------------------------------------------------------------------------------------------------------

### Technology Stack

Python<br>
Scrapy<br>
Pandas<br>
SQL<br>
Docker<br>
Label Studio<br>
Bash<br>
Linux<br>
Jupyter Notebook<br>

---------------------------------------------------------------------------------------------------------------------

### Example Workflow
<pre>
Run scraper
        ↓
Gather raw dataset
        ↓
Clean & normalize data
        ↓
Setup and deploy annotation app
        ↓
Perform annotation workflow
        ↓
validate annotated datasets
        ↓
Produce ML-ready dataset
</pre>
---------------------------------------------------------------------------------------------------------------------

### Use Cases

* Computer vision dataset preparation
* E-commerce product classification datasets
* Data annotation workflows
* Dataset engineering pipelines
* ML dataset preparation systems
* Future Improvements
* Automated scheduling
* Dataset versioning
* Monitoring pipelines
* Cloud deployment support
