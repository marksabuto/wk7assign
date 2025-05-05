import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import os

# Set style for better looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

def load_and_explore_data():
    """Task 1: Load and explore the dataset"""
    print("\n=== TASK 1: LOADING AND EXPLORING DATA ===\n")
    
    try:
        # Try to load from CSV first
        if os.path.exists('iris.csv'):
            df = pd.read_csv('iris.csv')
            print("Loaded data from iris.csv")
        else:
            # Fall back to sklearn dataset
            iris = load_iris()
            df = pd.DataFrame(iris.data, columns=iris.feature_names)
            df['variety'] = pd.Categorical.from_codes(iris.target, iris.target_names)
            print("Loaded Iris dataset from sklearn")
        
        # Display first few rows
        print("\nFirst 5 rows of the dataset:")
        print(df.head())
        
        # Explore structure
        print("\nDataset info:")
        print(df.info())
        
        # Check for missing values
        print("\nMissing values per column:")
        print(df.isnull().sum())
        
        # Clean data (though iris dataset typically has no missing values)
        df_clean = df.dropna()  # In case we had missing values
        
        return df_clean
    
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def basic_data_analysis(df):
    """Task 2: Perform basic data analysis"""
    print("\n=== TASK 2: BASIC DATA ANALYSIS ===\n")
    
    if df is None:
        print("No data to analyze")
        return
    
    # Basic statistics
    print("Descriptive statistics for numerical columns:")
    print(df.describe())
    
    # Group by categorical column and compute mean
    if 'variety' in df.columns:
        print("\nMean values by variety:")
        print(df.groupby('variety').mean())
    else:
        print("\nNo categorical column found for grouping")
    
    # Additional analysis
    print("\nAdditional findings:")
    # Example: Find which variety has the longest petals
    if 'petal.length' in df.columns and 'variety' in df.columns:
        max_petal = df.groupby('variety')['petal.length'].mean().idxmax()
        print(f"- {max_petal} has the longest petals on average")

def create_visualizations(df):
    """Task 3: Create data visualizations"""
    print("\n=== TASK 3: DATA VISUALIZATION ===\n")
    
    if df is None:
        print("No data to visualize")
        return
    
    # Create plots directory if it doesn't exist
    os.makedirs('plots', exist_ok=True)
    
    try:
        # Visualization 1: Line chart (simulated time series)
        plt.figure()
        if 'sepal.length' in df.columns:
            df['sepal.length'].plot(kind='line', title='Sepal Length Values (Simulated Time Series)')
            plt.ylabel('Sepal Length')
            plt.xlabel('Index (simulated time)')
            plt.savefig('plots/line_chart.png', bbox_inches='tight')
            plt.close()
            print("- Saved line chart as plots/line_chart.png")
        
        # Visualization 2: Bar chart (mean by category)
        plt.figure()
        if 'variety' in df.columns and 'petal.width' in df.columns:
            df.groupby('variety')['petal.width'].mean().plot(kind='bar')
            plt.title('Average Petal Width by Variety')
            plt.ylabel('Petal Width')
            plt.savefig('plots/bar_chart.png', bbox_inches='tight')
            plt.close()
            print("- Saved bar chart as plots/bar_chart.png")
        
        # Visualization 3: Histogram
        plt.figure()
        if 'sepal.width' in df.columns:
            df['sepal.width'].plot(kind='hist', bins=15)
            plt.title('Distribution of Sepal Width')
            plt.xlabel('Sepal Width')
            plt.savefig('plots/histogram.png', bbox_inches='tight')
            plt.close()
            print("- Saved histogram as plots/histogram.png")
        
        # Visualization 4: Scatter plot
        plt.figure()
        if 'sepal.length' in df.columns and 'petal.length' in df.columns:
            sns.scatterplot(data=df, x='sepal.length', y='petal.length', 
                          hue='variety' if 'variety' in df.columns else None)
            plt.title('Sepal Length vs Petal Length')
            plt.savefig('plots/scatter_plot.png', bbox_inches='tight')
            plt.close()
            print("- Saved scatter plot as plots/scatter_plot.png")
            
    except Exception as e:
        print(f"Error generating plots: {e}")

def main():
    """Main function to execute all tasks"""
    print("=== DATA ANALYSIS SCRIPT ===")
    
    # Task 1: Load and explore data
    df = load_and_explore_data()
    
    # Task 2: Basic data analysis
    basic_data_analysis(df)
    
    # Task 3: Data visualization
    create_visualizations(df)
    
    print("\nAnalysis complete! Check the generated plot files in the 'plots' directory.")

if __name__ == "__main__":
    main()