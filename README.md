# CarsList

This repository contains:

1. A Python script to scrape car-related listings from OLX India.
2. A Bash script to extract mutual fund Scheme Name and Asset Value data from AMFI's public NAV file.

---

## 1. Python Script - `main.py`

Scrapes car-related ads from [OLX car cover listings](https://www.olx.in/items/q-car-cover), filters relevant entries, and saves them to a text file.

### Features

- Scrapes listings using BeautifulSoup.
- Filters based on keywords like `car`, `seat cover`, `alto`, etc.
  
### Usage

Install dependencies:

```bash

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py

```
## 2. Bash Script - script.sh
Fetches mutual fund data from AMFI and extracts only the Scheme Name and Asset Value columns.

### Features
Downloads data from: https://www.amfiindia.com/spages/NAVAll.txt
Extracts and formats data into TSV.

Saves output to schemas.tsv.

### Usage
Make the script executable and run:

```
chmod +x script.sh
./script.sh
```
