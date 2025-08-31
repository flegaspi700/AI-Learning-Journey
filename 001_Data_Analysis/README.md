# Data Analysis and EDA

This folder contains files and resources for data analysis and exploratory data analysis (EDA).

Use this space to store scripts, notebooks, and datasets related to analyzing and understanding your data.

## File Descriptions

- `EDA_Roller_Coaster.ipynb`: A Jupyter Notebook that contains an exploratory data analysis of the roller coaster dataset.
- `EDA_Netflix_Movies.ipynb`: A Jupyter Notebook that contains an exploratory data analysis of the Netflix dataset.
- `EDA_FRED_Economic_Data.ipynb`: A Jupyter Notebook that contains an exploratory data analysis of FRED economic data.
- `Data/coaster_db.csv`: The dataset used for the roller coaster analysis.
- `Data/netflix_data.csv`: The dataset used for the Netflix analysis.

## Exploratory Data Analysis Table

| Title                                     | Dataset Name               | Notes                                                                  |
|-------------------------------------------|----------------------------|------------------------------------------------------------------------|
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

You can install these dependencies using pip:

```bash
pip install pandas matplotlib seaborn fredapi plotly
```

## Key Findings

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

