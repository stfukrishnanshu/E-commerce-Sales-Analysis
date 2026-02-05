import pandas as pd
import matplotlib.pyplot as plt
import os

def load_data(file_path):
    """Load CSV file with error handling"""
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        raise FileNotFoundError(" sales_data.csv not found in data folder")

def validate_columns(df):
    """Validate CSV column names"""
    required_columns = {
        "Date",
        "Product",
        "Quantity",
        "Price",
        "Customer_ID",
        "Region",
        "Total_Sales"
    }

    if not required_columns.issubset(df.columns):
        raise ValueError(
            f" CSV must contain columns: {required_columns}"
        )

def clean_data(df):
    """Clean and prepare data"""
    df.dropna(inplace=True)

    df["Date"] = pd.to_datetime(df["Date"])
    df["Quantity"] = df["Quantity"].astype(int)
    df["Price"] = df["Price"].astype(float)
    df["Total_Sales"] = df["Total_Sales"].astype(float)

    # Create Month column for trend analysis
    df["Month"] = df["Date"].dt.to_period("M")

    return df

def analyze_data(df):
    """Perform analysis"""
    monthly_sales = df.groupby("Month")["Total_Sales"].sum()
    product_sales = df.groupby("Product")["Total_Sales"].sum()
    region_sales = df.groupby("Region")["Total_Sales"].sum()

    return monthly_sales, product_sales, region_sales

def create_visualizations(monthly_sales, product_sales, region_sales):
    """Generate charts"""
    os.makedirs("visualizations", exist_ok=True)

    # 1️ Monthly Sales Trend (Line Chart)
    plt.figure(figsize=(10, 5))
    monthly_sales.plot(kind="line", marker="o")
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Total_Sales")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("visualizations/monthly_sales_trend.png")
    plt.show()
    plt.close()



    # 2️ Sales by Product (Bar Chart)
    plt.figure(figsize=(8, 5))
    product_sales.plot(kind="bar", color="steelblue")
    plt.title("Total Sales by Product")
    plt.xlabel("Product")
    plt.ylabel("Total_Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("sales_by_product.png")
    plt.show()
    plt.close()


    # 3️ Sales by Region (Bar Chart)
    plt.figure(figsize=(8, 5))
    region_sales.plot(kind="bar", color="seagreen")
    plt.title("Total Sales by Region")
    plt.xlabel("Region")
    plt.ylabel("Total_Sales")
    plt.tight_layout()
    plt.savefig("sales_by_region.png")
    plt.show()
    plt.close()


def main():
    print(" E-commerce Sales Analysis Started")

    df = load_data("sales_data.csv")
    validate_columns(df)
    df = clean_data(df)

    monthly_sales, product_sales, region_sales = analyze_data(df)
    create_visualizations(monthly_sales, product_sales, region_sales)

    print("✅ Analysis completed successfully!")
    print(f"💰 Total Revenue: {df['Total_Sales'].sum():.2f}")
    print(f"🛒 Total Units Sold: {df['Quantity'].sum()}")
    print(f"👥 Unique Customers: {df['Customer_ID'].nunique()}")

if __name__ == "__main__":
    main()

