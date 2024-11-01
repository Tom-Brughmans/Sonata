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
|'New_type_name'               |   string /                                                                                     |
|'Amphora_type_merged'         |   string / Typologies for Amphora type that take into account grouped types |
|'Provenance'               	 |   string / A region where an amphora was produced                                              |
|'content'	                   |   string / A product carried in an amphora:                                                    |
|'Site'	                       |   string / A modern name of an archaeological site from which an amphorae assemblage came      |
|'Site_type'	                 |   string / A site category                                                                     |
|'Grouped_sites'	             |   string /                                                                                     |
|'Amphora_type_lower_date' 	   |   float / A production start date of an amphora                                                |
|'Amphora_type_upper_date'     |   float / A production end date of an amphora                                                  |
|'Lower_context_date'          |   float / A consumption start date of an amphora                                               |
|'Upper_context_date'          |   float / A consumption end date of an amphora                                                 |
|'Frequency'	                 |   float / An amphora frequency                                                                 |
|'Pleiades URI'                |   string / Site geographical coordinates according to the Pleiades Atlas                       |
|'Latitude'                    |   float / Site geographical coordinates in latitude                                            |
|'Longitude'                   |   float / Site geographical coordinates in longitude                                           |
|'Tyrrhenian_vs_Adriatic'      |   string /                                                                                     |
|'Publication'	               |   string / Bibliographic reference for assemblage publication                                  |
|'Period'	                     |   string /                                          |
|'Notes'	                     |   string /                                                 |
|'Site_notes'                  |   string /                                                                  |
|'Amphora_type_notes'          |   string /       |
|'problems'	                   |   string /                   |

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
