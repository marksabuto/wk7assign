# Iris Dataset Analysis Project

This project performs exploratory data analysis and visualization on the famous Iris dataset. The script generates various plots and statistical analyses to help understand the characteristics of different iris flower varieties.

## Features

1. **Data Loading and Exploration**
   - Loads data from 'iris.csv' if available
   - Falls back to sklearn's built-in iris dataset if CSV is not found
   - Displays basic dataset information and checks for missing values

2. **Basic Data Analysis**
   - Generates descriptive statistics for numerical columns
   - Calculates mean values grouped by iris variety
   - Identifies varieties with notable characteristics

3. **Data Visualization**
   - Creates four different types of plots:
     - Line chart: Sepal length trends
     - Bar chart: Average petal width by variety
     - Histogram: Distribution of sepal width
     - Scatter plot: Relationship between sepal length and petal length

## Project Structure

```
.
├── data_analysis.py    # Main analysis script
├── plots/             # Directory containing generated plots
│   ├── line_chart.png
│   ├── bar_chart.png
│   ├── histogram.png
│   └── scatter_plot.png
└── README.md          # This file
```

## Requirements

- Python 3.x
- pandas
- matplotlib
- seaborn
- scikit-learn

## Usage

1. Make sure you have all required packages installed:
   ```bash
   pip install pandas matplotlib seaborn scikit-learn
   ```

2. Run the analysis script:
   ```bash
   python data_analysis.py
   ```

3. Check the generated plots in the `plots` directory.

## Output

The script will:
1. Display dataset information and basic statistics in the console
2. Generate four visualization plots in the `plots` directory
3. Provide insights about the iris varieties

## Plot Descriptions

1. **Line Chart** (`line_chart.png`)
   - Shows the trend of sepal length values
   - Useful for observing patterns in the data sequence

2. **Bar Chart** (`bar_chart.png`)
   - Displays average petal width for each iris variety
   - Helps compare petal width differences between varieties

3. **Histogram** (`histogram.png`)
   - Shows the distribution of sepal width measurements
   - Useful for understanding the range and frequency of sepal widths

4. **Scatter Plot** (`scatter_plot.png`)
   - Plots sepal length against petal length
   - Color-coded by variety
   - Helps visualize relationships between these measurements and variety clustering

## Data Columns

The dataset contains the following columns:
- `sepal.length`: Length of the sepal (in cm)
- `sepal.width`: Width of the sepal (in cm)
- `petal.length`: Length of the petal (in cm)
- `petal.width`: Width of the petal (in cm)
- `variety`: Type of iris (Setosa, Versicolor, or Virginica) 