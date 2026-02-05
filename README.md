📊 E-commerce Sales Data Analysis (Week 4 Project)

This project is a complete data analysis + visualization project using Python, Pandas, and Matplotlib.

It follows the Week 4 requirements:
✅ Load data
✅ Clean & validate
✅ Analyze
✅ Visualize (at least 2 chart types)
✅ Write insights
✅ Save charts + report
✅ GitHub-ready folder structure

🚀 Project Objective

The goal of this project is to analyze an E-commerce sales dataset and generate meaningful insights using:

Summary statistics

Product-wise revenue analysis

Monthly sales trends

Region-based distribution (optional)

📂 Dataset Used

The dataset is stored inside:

data/sales_data.csv

Columns in Dataset

Date → Sales date

Product → Product category

Quantity → Units sold

Price → Price per unit

Customer_ID → Unique customer ID

Region → Sales region

Total_Sales → Final sales amount

🛠️ Technologies Used

Python 3

Pandas

Matplotlib

📊 Visualizations Included

This project generates and saves charts inside:

visualizations/

Charts Created:

Bar Chart → Sales by Product Category

Line Chart → Monthly Sales Trend

(Optional) Pie Chart → Sales Distribution by Region

📁 GitHub Repository Structure

Ecommerce-Sales-Analysis/
│
├── README.md
├── main.py
├── requirements.txt
│
├── data/
│ └── sales_data.csv
│
├── visualizations/
│ ├── sales_by_product.png
│ ├── monthly_sales_trend.png
│ └── sales_by_region_pie.png
│
└── report/
└── final_report.md

⚙️ How to Run This Project (VS Code)
1️⃣ Clone the Repository
git clone <your-github-repo-link>
2️⃣ Open in VS Code

Open the folder in VS Code.

3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run the Project
python main.py
✅ Analysis Workflow Followed
Step 1: Data Loading

Loaded the dataset using Pandas

Step 2: Data Cleaning & Validation

Converted Date column into datetime format

Verified Total_Sales = Quantity × Price

Checked for missing values and invalid records

Step 3: Data Analysis

Total revenue calculation

Best product category by revenue

Monthly trend analysis

Region-wise sales distribution

Step 4: Visualization

Created professional charts using Matplotlib

Added labels, titles, and formatting

Saved charts as .png files

Step 5: Reporting

Generated a final report with insights inside:
report/final_report.md

📌 Project Insights (Example)

The product category with the highest revenue contributes the most to overall sales.

Monthly sales show a trend pattern that helps understand demand changes.

Regional distribution highlights which region performs best.

📤 Submission Checklist

✅ README.md
✅ main.py
✅ requirements.txt
✅ data/ folder
✅ visualizations/ folder
✅ report/ folder

👨‍💻 Author

Name: Krishnanshu Singh
Course/Internship: Python Data Analysis Internship
Week: Week 4
