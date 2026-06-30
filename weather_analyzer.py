import csv
import json
from datetime import datetime
from pathlib import Path

def setup_folders():
    outputs_folder = Path("outputs")
    outputs_folder.mkdir(exist_ok=True)
    print(f"Folder ready: {outputs_folder.resolve()}")

def load_weather_data(filename):
    records = []
    try:
        with open(filename, newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                row["date"] = datetime.strptime(row["date"], "%d-%m-%Y")
                row["temperature_c"] = float(row["temperature_c"])
                row["humidity_pct"] = float(row["humidity_pct"])
                row["rainfall_mm"] = float(row["rainfall_mm"])
                records.append(row)
    except FileNotFoundError:
        print(f"Error: File '{filename}' was not found.")
    return records

def filter_by_city(data, city):
    return list(filter(lambda record: record["city"] == city, data))

def get_temperatures(data):
    return list(map(lambda record: record["temperature_c"], data))

def monthly_summary(data):
    month_names = [record["date"].strftime("%B") for record in data]
    unique_months = [
        month for index, month in enumerate(month_names)
        if month not in month_names[:index]
    ]
    summary = {
        month: {
            "avg_temperature_c": round(
                sum(r["temperature_c"] for r in data if r["date"].strftime("%B") == month)
                / len([r for r in data if r["date"].strftime("%B") == month]), 1),
            "avg_humidity_pct": round(
                sum(r["humidity_pct"] for r in data if r["date"].strftime("%B") == month)
                / len([r for r in data if r["date"].strftime("%B") == month]), 1),
            "total_rainfall_mm": round(
                sum(r["rainfall_mm"] for r in data if r["date"].strftime("%B") == month), 1)
        }
        for month in unique_months
    }
    return summary

def find_extremes(data):
    return {
        "hottest": max(data, key=lambda r: r["temperature_c"]),
        "coldest": min(data, key=lambda r: r["temperature_c"]),
        "rainiest": max(data, key=lambda r: r["rainfall_mm"])
    }

def save_summary(summary, filename):
    try:
        with open(filename, "w", encoding="utf-8") as json_file:
            json.dump(summary, json_file, indent=4)
        print(f"\nMonthly summary saved to: {filename}")
    except Exception as error:
        print(f"Error saving summary: {error}")

def print_report(data):
    if not data:
        print("No data to display.")
        return
    city_name = data[0]["city"]
    print(f"\n{'=' * 60}")
    print(f"  Weather Report: {city_name}")
    print(f"{'=' * 60}")
    print(f"{'Date':<14} {'Temp (°C)':>10} {'Humidity':>10} {'Rainfall':>10}  Condition")
    print(f"{'-' * 60}")
    for record in data:
        date_str = record["date"].strftime("%d %b %Y")
        print(f"{date_str:<14}{record['temperature_c']:>9.1f}°{record['humidity_pct']:>9.1f}%{record['rainfall_mm']:>9.1f}mm  {record['condition']}")

    summary = monthly_summary(data)
    print(f"\n{'=' * 60}")
    print(f"  Monthly Summary: {city_name}")
    print(f"{'=' * 60}")
    print(f"{'Month':<12} {'Avg Temp':>10} {'Avg Humidity':>14} {'Total Rain':>12}")
    print(f"{'-' * 60}")
    for month, stats in summary.items():
        print(f"{month:<12}{stats['avg_temperature_c']:>9.1f}°{stats['avg_humidity_pct']:>13.1f}%{stats['total_rainfall_mm']:>11.1f}mm")

    extremes = find_extremes(data)
    print(f"\n{'=' * 60}")
    print(f"  Extreme Days: {city_name}")
    print(f"{'=' * 60}")
    print(f"  Hottest day : {extremes['hottest']['date'].strftime('%d %b %Y')} — {extremes['hottest']['temperature_c']}°C ({extremes['hottest']['condition']})")
    print(f"  Coldest day : {extremes['coldest']['date'].strftime('%d %b %Y')} — {extremes['coldest']['temperature_c']}°C ({extremes['coldest']['condition']})")
    print(f"  Rainiest day: {extremes['rainiest']['date'].strftime('%d %b %Y')} — {extremes['rainiest']['rainfall_mm']}mm ({extremes['rainiest']['condition']})")
    print(f"{'=' * 60}")

    temperatures = get_temperatures(data)
    avg_temp = round(sum(temperatures) / len(temperatures), 1)
    print(f"\n  Year average temperature for {city_name}: {avg_temp}°C")

def main():
    setup_folders()
    all_data = load_weather_data("weather_data.csv")
    if not all_data:
        print("No data loaded. Exiting.")
        return
    mumbai_data = filter_by_city(all_data, "Mumbai")
    print_report(mumbai_data)
    delhi_data = filter_by_city(all_data, "Delhi")
    print_report(delhi_data)
    combined_summary = {
        city: monthly_summary(filter_by_city(all_data, city))
        for city in ["Mumbai", "Delhi"]
    }
    save_summary(combined_summary, "outputs/monthly_summary.json")

if __name__ == "__main__":
    main()