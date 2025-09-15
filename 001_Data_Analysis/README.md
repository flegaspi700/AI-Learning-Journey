# Data Analysis and EDA

This folder contains files and resources for data analysis and exploratory data analysis (EDA).

Use this space to store scripts, notebooks, and datasets related to analyzing and understanding your data.

## File Descriptions

- `EDA_sql_Student_Mental_Health.ipynb`: A Jupyter Notebook that contains an SQL-based exploratory data analysis of student mental health data using PostgreSQL. Based on DataCamp dataset examining international students' mental health indicators.
- `EDA_Roller_Coaster.ipynb`: A Jupyter Notebook that contains an exploratory data analysis of the roller coaster dataset.
- `EDA_Netflix_Movies.ipynb`: A Jupyter Notebook that contains an exploratory data analysis of the Netflix dataset.
- `EDA_FRED_Economic_Data.ipynb`: A Jupyter Notebook that contains an exploratory data analysis of FRED economic data.
- `fred_data_suggestions.txt`: A text file containing ideas for additional economic indicators to analyze from the FRED database.
- `Data/students.csv`: The dataset used for the student mental health analysis (DataCamp source).
- `Data/coaster_db.csv`: The dataset used for the roller coaster analysis.
- `Data/netflix_data.csv`: The dataset used for the Netflix analysis.

## Exploratory Data Analysis Table

| Title                                     | Dataset Name               | Notes                                                                  |
|-------------------------------------------|----------------------------|------------------------------------------------------------------------|
| [Student Mental Health (SQL)](./EDA_sql_Student_Mental_Health.ipynb) | [students.csv](./Data/students.csv) | An SQL-based exploratory data analysis of student mental health data using PostgreSQL. Examines international students' depression, social connectedness, and acculturative stress by demographics and language proficiency. Based on DataCamp dataset. |
| [Roller Coaster](./EDA_Roller_Coaster.ipynb) | [coaster_db](./Data/coaster_db.csv) | An exploratory data analysis of a roller coaster dataset. |
| [Netflix Movies](./EDA_Netflix_Movies.ipynb) | [netflix_data](./Data/netflix_data.csv) | An exploratory data analysis of Netflix movies, focusing on the 1990s and overall library characteristics. |
| [FRED Economic Data](./EDA_FRED_Economic_Data.ipynb) | FRED API | An exploratory data analysis of economic data from the Federal Reserve. |

## Dependencies

The analysis in this folder requires the following Python libraries:

- pandas
- matplotlib
- seaborn
- fredapi
- plotly
- sqlalchemy
- psycopg2-binary
- python-dotenv

You can install these dependencies using pip:

```bash
pip install pandas matplotlib seaborn fredapi plotly sqlalchemy psycopg2-binary python-dotenv
```

**Note:** The Student Mental Health analysis requires PostgreSQL database setup with appropriate environment variables configured in a `.env` file.

## Key Findings

### Student Mental Health Analysis (SQL)
- **Language Proficiency Impact:** Students with better English and Japanese proficiency show lower depression scores and better social connectedness.
- **Length of Stay Patterns:** International students' mental health indicators vary significantly by duration of stay, with complex relationships between time and adaptation.
- **Academic Level Differences:** Graduate and undergraduate international students display distinct mental health patterns, with varying stress levels and social connection.
- **Age Group Analysis:** Younger international students (under 20) and older students (over 30) show different mental health profiles.
- **High-Risk Groups:** Identified specific cohorts with elevated depression (>15 PHQ-9), low social connectedness (<30 SCS), and high acculturative stress (>60 ASISS).
- **International vs Domestic:** Clear disparities in mental health outcomes between international and domestic students, highlighting unique challenges faced by international students.

### Roller Coaster Analysis
- The number of new roller coasters introduced peaked in the late 1990s and early 2000s.
- There is a strong positive correlation between a roller coaster's height and its speed.
- Vekoma and Bolliger & Mabillard are among the most prolific roller coaster manufacturers.
- Cedar Point and Six Flags parks are home to some of the fastest roller coasters.

### Netflix Movie Analysis
- From the Netflix movie analysis, we found that a large number of movies from the 1990s have a duration of about 100 minutes. 
- The analysis also identified the top directors, genres, and countries with the most content on the platform.

### FRED Economic Data Analysis
- The S&P 500 index shows significant growth over time, with notable fluctuations during economic events.
- The national unemployment rate exhibits cyclical patterns, with sharp increases during recessions.
- State-level unemployment data reveals regional disparities in economic performance, particularly during the COVID-19 pandemic.