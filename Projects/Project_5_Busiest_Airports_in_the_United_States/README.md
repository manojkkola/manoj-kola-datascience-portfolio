# Busiest Airports in the United States: A Multi-Source Data Preparation Project

## Overview
This project (DSC 540 – Data Preparation) explores how population growth in major U.S. cities relates to airport traffic and weather conditions. It is built as a multi-stage data preparation pipeline: three datasets from three different source types — a flat file, a web page, and an API — are cleaned, standardized, joined, and stored in a relational database before being analyzed and visualized.

## Data Sources
| Source Type | Dataset | Description |
|---|---|---|
| Flat file (CSV, Kaggle) | City population data | Population counts and growth metrics for major U.S. cities |
| Website (Wikipedia) | List of the busiest U.S. airports | Airport names, IATA codes, cities, and passenger traffic (2018–2024), extracted via web scraping |
| API (OpenWeatherMap) | City weather data | Temperature and other current conditions for each airport's city |

The three sources are joined on **City** and **State** as the common key and merged using SQL joins after standardizing city naming conventions across datasets.

## Approach
1. **Data Selection** — scoped the three data sources and mapped how they relate to one another through the city field.
2. **Extraction & Cleaning** — scraped the Wikipedia airport table, pulled weather data via the OpenWeatherMap API, and loaded the Kaggle population CSV; standardized column names, city labels, and data types across all three.
3. **Transformation** — engineered an `Airport_Type` category based on passenger volume and handled missing/zero values.
4. **Storage** — loaded all three cleaned datasets into a SQLite database (`manoj_project.db`) as individual tables, then created a consolidated `final_airport_data` table using a `LEFT JOIN` so all airport records are retained even where weather or population data is incomplete.
5. **Analysis & Visualization** — queried the merged dataset back into pandas and produced nine visualizations covering passenger traffic, airport type distribution, population vs. traffic, temperature vs. traffic, and growth trends from 2018–2024.

## Key Findings
- The busiest U.S. airports by 2024 passenger traffic are concentrated in the largest metro areas, consistent with population-driven travel demand.
- There is a visible, though not perfectly linear, relationship between a city's total population and its airport's passenger volume.
- Passenger traffic shows a clear multi-year recovery trend from 2018 through 2024, reflecting the post-pandemic rebound in air travel.
- Airport type (categorized by traffic volume) is a useful lens for comparing average passenger load and growth patterns across the dataset.

## Ethical Considerations
- Cleaning decisions — such as categorizing airports with missing/zero passenger data — can introduce bias if not clearly documented, since assumptions about missing values may not reflect real-world conditions.
- Data accuracy and credibility depend on the reliability of public sources (Kaggle, Wikipedia, OpenWeatherMap); provenance and licensing terms were respected throughout.
- Transparency about transformations and assumptions is essential so conclusions drawn from the merged dataset can be fairly evaluated.

## Contents
| File | Description |
|---|---|
| `DSC540_Manoj_Kola_Project_Milestone_1.docx` | Data source selection, relationships, project plan, and ethical considerations |
| `DSC540_Manoj_Kola_Project_Milestone_2.ipynb` / `.pdf` | Extraction and cleaning of the first data source |
| `DSC540_Manoj_Kola_Project_Milestone_3.ipynb` / `.pdf` | Extraction and cleaning of the second data source |
| `DSC540_Manoj_Kola_Project_Milestone_4.ipynb` / `.pdf` | Extraction and cleaning of the third data source |
| `DSC540_Manoj_Kola_Project_Milestone_5.ipynb` / `.pdf` | Final database merge, SQL joins, and visualization notebook |

## Tools & Methods
Python, pandas, SQLite, SQL joins, web scraping, REST API integration (OpenWeatherMap), matplotlib, data blending across CSV/API/HTML sources

## Author
Manoj Kumar Kola
