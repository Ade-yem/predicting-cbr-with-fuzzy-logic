import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from fuzzy_logic import predict, view_charts

def get_file_content(file: str):
    df = pd.read_excel(file, "Sheet1")
    return df

def compute(df: pd.DataFrame):
    for index, row in df.iterrows():
        # add a new column "predicted cbr" to the dataframe and input the answers of each row
        df.at[index, "Predicted CBR"] = predict(row["Percentages of addition of fiber (%)"], row["Liquid Limit (%)"], row["Optimum Moisture Content"])
    return df

def plot_regression(df: pd.DataFrame):
    fig, ax = plt.subplots()
    actual = df["CBR"]
    predicted = df["Predicted CBR"]
    
    # Scatter plot
    ax.scatter(predicted, actual, label="Data points")
    
    # Adding regression line
    coeff = np.polyfit(predicted, actual, 1)
    poly1d_fn = np.poly1d(coeff)
    ax.plot(predicted, poly1d_fn(predicted), color='red', label="Best fit line")
    ax.set_title("Fitness Plot")
    ax.set_xlabel("Predicted values")
    ax.set_ylabel("Actual values")
    ax.legend()
    
    plt.savefig('./reports/Best_fit.png')
    plt.close()

def calc_r_squared(df: pd.DataFrame):
    actual = df["CBR"]
    predicted = df["Predicted CBR"]
    mean = np.mean(actual)
    ss_res = np.sum((actual - predicted) ** 2)
    ss_tot = np.sum((actual - mean) ** 2)
    r_squared = 1 - (ss_res / ss_tot)
    return r_squared

def calc_mape(df: pd.DataFrame):
    actual = df["CBR"]
    predicted = df["Predicted CBR"]
    mape = np.mean(np.abs((actual - predicted) / actual)) * 100
    return mape

def calc_rmse(df: pd.DataFrame):
    actual = df["CBR"]
    predicted = df["Predicted CBR"]
    rmse = np.sqrt(np.mean((actual - predicted) ** 2))
    return rmse


def generate_report(df: pd.DataFrame):
    """
    Plots the relationship between predicted and Actual CBR and also calculates the
    R-squared, Mean Absolute Percentage Error and the Root Mean Squared Error
    """
    os.makedirs('reports', exist_ok=True)
    df.to_excel(excel_writer="predictions.xlsx", sheet_name="Result")
    view_charts()
    plot_regression(df)
    rmse = calc_rmse(df)
    r_squared = calc_r_squared(df)
    mape = calc_mape(df)
    with open("./reports/report.txt", "w") as f:
        f.write(f"R-squared: {r_squared}\n")
        f.write(f"Mean Absolute Percentage Error: {mape}\n")
        f.write(f"Root Mean Squared Error: {rmse}\n")


def main(file: str):
    df = get_file_content(file)
    df = compute(df)
    generate_report(df)

if __name__ == "__main__":
    main("data.xlsx")
