# Sonata


# Repository structure


    ├── data                   # csv and xlsx files with data
    ├── figs                   # all figures from the paper
    ├── src                    
    │   ├── application        # Jupyter notebooks per calculation and figure
    │   ├── sonata             # functions used for data preprocessing and calculations 
    └── tests                  # unit tests


# Data

<br /> 

<details>
  <summary>  The data table </summary>

|**Field Name**                |      **Type / Description**                                                                      |
| ---------------------------- | ---------------------------------------------------------------------------------------------- |
|'Amphora_type'	               |   string / Commonly used typologies for Amphora type                                           |
|'New_type_name'               |   string / Indicates values in the field ‘Amphora_type’ that are treated as the same type in the analyses|
|'Amphora_type_merged'         |   string / Typologies for Amphora type that take into account grouped types                    |
|'Provenance'                  |   string / A region where an amphora was produced                                            |
|'content'	                   |   string / A product carried in an amphora                                                     |
|'Site'	                       |   string / A modern name of an archaeological site from which an amphorae assemblage came      |
|'Site_type'	               |   string / A site category                                                                   |
|'Grouped_sites'	           |   string /   A grouping of the field ‘Site’ per region or ancient settlement                 |
|'Amphora_type_lower_date' 	   |   float / A production start date of an amphora                                                |
|'Amphora_type_upper_date'     |   float / A production end date of an amphora                                                  |
|'Lower_context_date'          |   float / A consumption start date of an amphora                                               |
|'Upper_context_date'          |   float / A consumption end date of an amphora                                                 |
|'Frequency'	               |   float / An amphora frequency                                                                 |
|'Pleiades URI'                |   string / Site geographical coordinates according to the Pleiades Atlas                       |
|'Latitude'                    |   float / Site geographical coordinates in latitude                                            |
|'Longitude'                   |   float / Site geographical coordinates in longitude                                           |
|'Tyrrhenian_vs_Adriatic'      |   string / Indication of whether the site is on the Tyrrhenian, Adriatic or Central regions of Italy |
|'Publication'	               |   string / Bibliographic reference for assemblage publication                                  |
|'Period'	                     |   string /     Categorical indication of site chronology in Roman historical period          |
|'Notes'	                     |   string /  General notes on the sites and types          |
|'Site_notes'                  |   string /  Notes and considerations on the site and its location                              |
|'Amphora_type_notes'          |   string / Notes and considerations on the amphora type or typical prime use contents designation |
|'problems'	                   |   string / Considerations of problems related to the type identification and whether they could be merged with other types|

</details>

<br /> 

## Setup

### Prerequisites
- **Python version**: Make sure you have Python 3.9 installed. 

### Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Tom-Brughmans/Sonata.git
   cd Sonata
2. **Set up a virtual environment**:
    ```bash
    python3 -m venv myvenv
    source myvenv/bin/activate
3. **Install dependencies**: 
    ```bash
    pip install -r requirements.txt

# Contributors

* [Tom Brughmans](https://pure.au.dk/portal/en/persons/tom-brughmans(78c7314a-9485-4e14-b207-0e836aea5e01).html)
* [Ekaterina Borisova](https://github.com/esborisova)
* [Laura B. Paulsen](https://github.com/laurabpaulsen)
* Paulina Komar

# Funding and acknowledgements

# Cite

```commandline
@article{komar2025,
    title = "Consumption Trends, Trading Patterns and Economic Development in Italy Across Centuries: Data Analysis of Roman Amphorae in a Long-Term Perspective",
    author = "Komar, P., Brughmans, T. & Borisova, E.",
    year = "2025",
    publisher = "J Archaeol Method Theory",
    volume = "32",
    number = "21",
    url = "https://doi.org/10.1007/s10816-024-09686-1",
}
```

