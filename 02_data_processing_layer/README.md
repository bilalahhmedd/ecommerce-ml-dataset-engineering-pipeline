Data processing is crucial stage of pipeline to produce quality data. This data processing layer is responsible to ensure good quality data being moved from scraping layer into annotation layer.

## Overview

Image data processing layer requires both automated scripts and mannual approach to visually inspect images data.
It is segmented into two stages (deduplication data, inspection and validation). where each stage contains multiple disconnected utily scripts. 

1. deduplicate data
    * run dedup process on scrapped images data set to list set of duplicated images
    * list unique ids from crawler output
    * list duplicated folders
    * move out duplicated images and folder to trash section
2. inspection and validation
    * generate random samples from scraped data for inspecation
    * evaluate output of dedup process
    * generate random samples from deduped data
    * copy random samples to inspection stage

### techonologies:

* python
* knjcode/imgdupes
* jupyter-notebooks
* shutil
* pandas
