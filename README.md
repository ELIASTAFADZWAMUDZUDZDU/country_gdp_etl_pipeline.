# Country GDP ETL Pipeline

A production-inspired **Extract, Transform, Load (ETL)** pipeline built with Python that automatically collects GDP data from Wikipedia, transforms it into multiple currencies, and stores the processed dataset in both CSV and SQLite formats.

This project demonstrates practical data engineering concepts, including modular software architecture, data validation, logging, configuration management, and database integration.

---

## Project Overview

The pipeline performs the complete ETL workflow:

1. **Extract**
   - Retrieves GDP data from an archived Wikipedia dataset.
   - Validates the source table before processing.

2. **Transform**
   - Cleans and standardizes GDP values.
   - Converts GDP (USD) into:
     - GBP
     - EUR
     - INR
   - Uses live exchange rates when available and automatically falls back to predefined rates if the API is unavailable.

3. **Load**
   - Saves the transformed dataset as a CSV file.
   - Loads the dataset into a SQLite database.
   - Executes SQL queries for analysis.
   - Records execution logs for monitoring and debugging.

---

## Project Architecture

```
                Wikipedia GDP Data
                        │
                        ▼
                  Data Extraction
                        │
                        ▼
                Data Transformation
                        │
        ┌───────────────┴───────────────┐
        ▼                               ▼
   CSV Output                    SQLite Database
                                        │
                                        ▼
                                SQL Analysis Query
```

---

## Technologies Used

- Python
- Pandas
- BeautifulSoup
- Requests
- SQLite
- SQL
- Logging
- Modular Python Packages

---

## Skills Demonstrated

This project demonstrates:

- ETL pipeline development
- Data extraction from web sources
- Data cleaning and transformation
- Exchange-rate API integration
- SQLite database management
- SQL querying
- Modular Python architecture
- Configuration management
- Error handling
- Logging and monitoring
- Professional project organization

---

## Project Structure

```
Country-GDP-ETL-Pipeline/
│
├── main.py
│
├── src/
│   ├── config.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── database.py
│   └── logger.py
│
├── data/
├── logs/
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/ELIASTAFADZWAMUDZUDZDU/country_gdp_etl_pipeline.git
```

Navigate into the project:

```bash
cd country_gdp_etl_pipeline
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Pipeline

Execute the pipeline using:

```bash
python main.py
```

---

## Outputs

After execution, the project generates:

| Output                    | Description                                   |
|---------------------------|-----------------------------------------------|
| `data/FINAL_LIST.csv`     | Processed GDP dataset                         |
| `FINAL.db`                | SQLite database containing the processed data |
| `logs/investment_log.txt` | Pipeline execution log                        |

---

## Reliability Features

- Automatic creation of output directories
- Configuration centralized in a dedicated module
- Safe database transactions using context managers
- Parameterized SQL queries
- Input validation during extraction
- Automatic fallback exchange rates if the external API is unavailable
- Execution logging with timestamps

---

## Future Improvements

- PostgreSQL support
- Docker containerization
- Apache Airflow orchestration
- Automated unit testing
- CI/CD pipeline using GitHub Actions
- Cloud deployment

---

## Author

**Elias Tafadzwa Mudzudzu**

Computer Engineering Student | Data Engineering & Artificial Intelligence Enthusiast

---

## License

This project is licensed under the MIT License.
