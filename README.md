# Weather Data Lake to Data Warehouse Pipeline

## Project Overview

This project is an **end-to-end weather data pipeline** that collects real-time weather data from the **OpenWeather API**, stores it in JSON format, processes it using **Apache Spark**, and loads the cleaned data into a **PostgreSQL data warehouse** for analysis and visualization. All tools used are **open-source** and the solution is built **without Docker**.

---

## Architecture

```
[OpenWeather API]
        ↓
[fetch_weather.py - Python script]
        ↓
[Raw JSON file]
        ↓
[transform_weather.py - PySpark job]
        ↓
[Cleaned CSV output]
        ↓
[load_to_warehouse.py - Pandas + SQLAlchemy]
        ↓
[PostgreSQL Database]
```

---

## 🛠️ Tools & Technologies

| Task            | Tool Used                   |
| --------------- | --------------------------- |
| Data Ingestion  | Python, `requests`, `json`  |
| Storage (raw)   | Local file system (JSON)    |
| Data Processing | Apache Spark, PySpark       |
| Data Warehouse  | PostgreSQL (cloud or local) |
| Data Loading    | Pandas, SQLAlchemy          |

---

## Project Structure

```
weather-pipeline/
├── fetch_weather.py           # Ingests weather data from OpenWeather API
├── transform_weather.py       # PySpark job to clean and convert JSON to CSV
├── load_to_warehouse.py       # Loads cleaned CSV into PostgreSQL table
├── weather.csv/               # Output folder with cleaned CSV files
├── *.json                     # Raw JSON files with weather data
└── README.md                  # Project documentation
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone (https://github.com/bellonbits/Weather-Data-Lake-to-Data-Warehouse-Pipeline).git
cd Weather-Data-Lake-to-Data-Warehouse-Pipeline
```

### 2. Create Python Virtual Environment

```bash
python3 -m venv spark-env
source spark-env/bin/activate
pip install -r requirements.txt  # includes pandas, requests, sqlalchemy, findspark, psycopg2
```

### 3. Install Apache Spark & Java

* Install [Apache Spark](https://spark.apache.org/downloads.html) and [Java JDK 11+](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html).
* Set environment variables:

  ```bash
  export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
  export SPARK_HOME=/path/to/spark
  export PATH=$SPARK_HOME/bin:$JAVA_HOME/bin:$PATH
  ```

---

## Running the Pipeline

### 1. Ingest Weather Data

```bash
python fetch_weather.py
```

> Saves raw weather JSON (e.g., `weather_2025-06-03_23-20-00.json`)

### 2. Transform Data with Spark

```bash
python transform_weather.py
```

> Reads all `.json` files in the directory and writes a cleaned CSV to `weather.csv/`

### 3. Load Data to PostgreSQL

Edit `load_to_warehouse.py` with your actual database credentials, then:

```bash
python load_to_warehouse.py
```

---

## Sample Output

| timestamp           | city    | temperature | humidity | description      |
| ------------------- | ------- | ----------- | -------- | ---------------- |
| 2025-06-04 00:06:00 | Nairobi | 18.3°C      | 85%      | scattered clouds |

---

## Configuration Notes

* Make sure PostgreSQL is running and accessible on the given host/port.
* To secure credentials, consider using environment variables or a `config.json` file.

---

## Next Steps

* Connect PostgreSQL to **Apache Superset** or **Power BI Desktop**.
* Schedule scripts using **The Apache Airflow**.
* Add **historical weather** collection or **forecast analysis**.

---

## Author

**Peter Gatitu Mwangi**
Email: [petergatitu61@gmail.com](mailto:petergatitu61@gmail.com)
Project Repo: [GitHub](https://github.com/bellonbits/Weather-Data-Lake-to-Data-Warehouse-Pipeline) 

