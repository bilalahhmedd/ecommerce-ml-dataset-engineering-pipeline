Data acquisition layer is crucial to develop datasets for AI training models and applications. This layer is implementation stage of ml-data-engineering pipeline to crawl, acquire and land data into centeral raw data storage.

## Overview
Data acquisition layer comprises two modules.
* ebay-products-scrapper
* historical-data-acquisition

## System Components
 1. scraping layer
    * ebay products scrapper
        * ebay scraping bot 1.3.0
            * ebay spider
            * ebay results count spider
2. historical data acquisition layer
    * filter data
    * get data from web app history files
    * parse big csv and filter historical images data

## Technologies

* python
* scrapy
* salenium
* pandas
* requests
* jsons