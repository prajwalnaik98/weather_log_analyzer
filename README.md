# Weather Log Analyzer

A beginner-friendly Python project that reads weather records from a CSV file, performs basic analysis, generates formatted reports, and exports monthly weather statistics to a JSON file.

---

## Project Description

This project processes weather data for two Indian cities — **Mumbai** and **Delhi** — covering all twelve months of 2024. It demonstrates how to use Python's built-in libraries to read CSV files, analyze data, calculate statistics, identify weather extremes, and save the results in JSON format.

---

## Concepts Used

| Concept | Implementation |
|---|---|
| Functions with docstrings | Used throughout `weather_analyzer.py` |
| CSV file handling | `load_weather_data()` using `csv.DictReader` |
| JSON writing | `save_summary()` using `json.dump()` |
| List comprehensions | Extracting months and temperatures |
| Dictionary comprehensions | Building monthly summaries |
| `filter()` with lambda | Filtering weather records by city |
| `map()` with lambda | Extracting temperature values |
| `datetime.strptime()` | Parsing `DD-MM-YYYY` date strings |
| `pathlib` | Creating the `outputs/` directory |
| Exception handling | Reading and writing files safely using `try/except` |
| Loops | Iterating through weather records |
| Conditionals | Handling empty datasets and program flow |
| f-strings | Formatting reports for the console |

---

## How to Run

1. Install Python 3.8 or later.
2. Place `weather_data.csv` and `weather_analyzer.py` in the same directory.
3. Open a terminal inside the project folder.
4. Run the following command:

```bash
python weather_analyzer.py
```

The script will automatically:

- Create an `outputs/` folder
- Display weather reports for Mumbai and Delhi
- Generate `outputs/monthly_summary.json`

No external libraries are required.

---

## Project Folder Structure

```text
weather_log_analyser/
│
├── weather_data.csv
├── weather_analyzer.py
├── README.md
│
└── outputs/
    └── monthly_summary.json
```

---

## Functions Overview

| Function | Purpose |
|---|---|
| `setup_folders()` | Creates the output directory using `pathlib` |
| `load_weather_data(filename)` | Reads weather data from the CSV file |
| `filter_by_city(data, city)` | Returns records for a selected city |
| `get_temperatures(data)` | Extracts temperature values using `map()` |
| `monthly_summary(data)` | Generates monthly weather statistics |
| `find_extremes(data)` | Finds the hottest, coldest, and rainiest days |
| `save_summary(summary, filename)` | Saves the summary to a JSON file |
| `print_report(data)` | Prints a formatted weather report |
| `main()` | Executes the complete workflow |

---

## Sample Output

```text
Folder ready: C:\...\weather_log_analyser\outputs

============================================================
  Weather Report: Mumbai
============================================================
Date           Temp (°C)   Humidity   Rainfall  Condition
------------------------------------------------------------
01 Jan 2024        31.2°      72.0%      2.1mm  Partly Cloudy
01 Feb 2024        32.5°      68.0%      0.5mm  Sunny
...

============================================================
  Monthly Summary: Mumbai
============================================================
Month          Avg Temp   Avg Humidity   Total Rain
------------------------------------------------------------
January           31.2°         72.0%        2.1mm
February          32.5°         68.0%        0.5mm
...

============================================================
  Extreme Days: Mumbai
============================================================
Hottest day : 01 Apr 2024 — 36.1°C (Hot and Humid)

Coldest day : 01 Aug 2024 — 28.5°C (Heavy Rain)

Rainiest day: 01 Jul 2024 — 621.3mm (Very Heavy Rain)

============================================================

Year average temperature for Mumbai: 31.7°C
```

---

## Output JSON

The program also generates:

```json
{
    "Mumbai": {
        "January": {
            "avg_temperature_c": 31.2,
            "avg_humidity_pct": 72.0,
            "total_rainfall_mm": 2.1
        }
    },
    "Delhi": {
        "January": {
            "avg_temperature_c": 14.3,
            "avg_humidity_pct": 78.0,
            "total_rainfall_mm": 5.2
        }
    }
}
```

---

## Author

**Developed by:** **Prajwal Naik**

This project was built to strengthen practical Python programming skills, including file handling, data processing, JSON operations, exception handling, and working with Python's standard library.
