An e-commerce machine learning data engineering pipeline to build reasonably good quality dataset to be served to ai training applications.

This project is implementation of kind of pipeline with steps including data acquisation, data cleaning, proudct annotation workflows and ML-reading dataset generation.

---------------------------------------------------------------------------------------------------------------------

Overview

Building reasonably good quality dataset for computer vision system is comprised of scattered stages.

* Data acquisition
* Data cleaning and standardization
* Feature engineering
* Annotation workflows
* Dataset validation
* ML reading dataset preparation

This project tells us how these different steps can be integrated into unified data engineering pipeline for e-commerce product data.

---------------------------------------------------------------------------------------------------------------------

Problem statement

Computer vision ai applications highly depend on good quality datasets.

While, creation of good quality datasets requires scattered routines.

* Product data resides in multiple sources
* Raw data has to be cleaned and normalized
* Annotation systems must be well integrated with preprocessing pipeline
* Data has to be inspected before serving to ai applications

This repo demonstrates an end to end workflow for solving these challenges.

---------------------------------------------------------------------------------------------------------------------

Pipeline architecture

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

---------------------------------------------------------------------------------------------------------------------

System components

Data Collection Layer

Process of acquiring product listing data from e-commerce store (ebay)

Capabilities:

* Product Scraping workflows
* Product metadata extraction
* Image collection pipelines
* Structured raw dataset generation

TechStack:

* Python
* Scrapy
* bash scripting

---------------------------------------------------------------------------------------------------------------------

Data processing layer

Transforms raw data into standardized data

Capabilities:

* Datasets cleaning
* Normalization pipelines
* Feature engineering
* Data validation workflow

TechStack:

* Python
* Pandas
* Jupyter Notebooks

---------------------------------------------------------------------------------------------------------------------

Annotation layer

Layer of data labeling workflow for machine learning systems

* Dataset annotation workflows
* Annotation automation
* Dataset export pipeline
* Dockerized annotation environment

TechStack:

* Labelstudio
* Docker
* Python
* Bash