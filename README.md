# Vendor Intelligence & Freight Cost Prediction System

## 📑 Table of Contents

- <a href="#project-overview">Project Overview</a>
- <a href="#business-problem">Business Problem</a>
- <a href="#objectives">Objectives</a>
- <a href="#dataset-information">Dataset Information</a>
- <a href="#technologies-used">Technologies Used</a>
- <a href="#project-structure">Project Structure</a>
- <a href="#data-ingestion-pipeline">Data Ingestion Pipeline</a>
- <a href="#sql-based-analysis">SQL-Based Analysis</a>
- <a href="#data-preprocessing">Data Preprocessing</a>
- <a href="#machine-learning-models">Machine Learning Models</a>
- <a href="#model-evaluation">Model Evaluation</a>
- <a href="#business-insights-generated">Business Insights Generated</a>
- <a href="#logging-and-monitoring">Logging and Monitoring</a>
- <a href="#key-features">Key Features</a>
- <a href="#future-improvements">Future Improvements</a>
- <a href="#conclusion">Conclusion</a>
- <a href="#author">Author</a>

---

<h2 id="project-overview">📌 Project Overview</h2>

This project is an end-to-end Data Analytics and Machine Learning system developed to analyze vendor performance, predict freight costs, and generate business insights using SQL, Python, and Machine Learning techniques.

The system automates vendor analysis, sales aggregation, invoice intelligence, and freight prediction workflows.

---

<h2 id="business-problem">📊 Business Problem</h2>

Organizations often face challenges such as:

- High freight costs
- Manual vendor analysis
- Inefficient inventory tracking
- Invoice processing complexity
- Lack of automated business insights

This project helps solve these problems using data-driven analytics and machine learning.

---

<h2 id="objectives">🎯 Objectives</h2>

- Build automated data ingestion pipelines
- Generate vendor performance summaries
- Predict freight costs using ML models
- Perform sales and purchase analysis
- Detect invoice-related anomalies
- Improve operational visibility through analytics

---

<h2 id="dataset-information">🗂 Dataset Information</h2>

The project uses multiple business datasets including:

- purchases.csv
- purchase_prices.csv
- sales.csv
- vendor_invoice.csv
- inventory datasets

These datasets contain:

- Vendor details
- Product pricing
- Freight costs
- Sales transactions
- Inventory records
- Excise tax information

---

<h2 id="technologies-used">🛠 Technologies Used</h2>

### Programming Language
- Python

### Libraries
- Pandas
- NumPy
- Scikit-learn
- SQLite3
- Matplotlib
- Logging

### Tools
- Jupyter Notebook
- VS Code
- Git & GitHub

---

<h2 id="project-structure">📁 Project Structure</h2>

```bash
Data_Analysis_Large_Project/
│
├── Models/
│   ├── predict_freight_model.pkl
│   └── scaler.pkl
│
├── freight_cost_prediction/
│   ├── train.py
│   ├── data_preprocessing.py
│   └── model_evaluation.py
│
├── invoice_flagging/
│   ├── train.py
│   ├── data_preprocessing.py
│   └── model_evaluation.py
│
├── inference/
│   ├── predict_freight.py
│   └── predict_invoice_flag.py
│
├── jupyter_notebook/
│   └── Invoice_Intelligence_ML_Project.ipynb
│
├── get_vendor_summary.py
├── app.py
├── requirements.txt
└── README.md
```

---

<h2 id="data-ingestion-pipeline">⚙️ Data Ingestion Pipeline</h2>

The ingestion pipeline performs:

- CSV file ingestion
- Data cleaning
- Missing value handling
- Data type conversion
- SQLite database loading
- Logging and monitoring

---

<h2 id="sql-based-analysis">🧮 SQL-Based Analysis</h2>

SQL queries were used to:

- Aggregate vendor purchases
- Calculate sales summaries
- Generate freight summaries
- Compute excise taxes
- Merge sales and purchase intelligence

Example SQL operations include:

- GROUP BY
- JOIN
- Common Table Expressions (CTEs)
- Aggregations
- Sorting and filtering

---

<h2 id="data-preprocessing">🧹 Data Preprocessing</h2>

The preprocessing pipeline includes:

- Null value treatment
- Feature engineering
- Numeric conversions
- Outlier handling
- Data normalization
- Data type casting

---

<h2 id="machine-learning-models">🤖 Machine Learning Models</h2>

Models used in the project:

- Linear Regression
- Random Forest Regressor
- XGBoost (if applicable)

The models were trained to predict:

- Freight costs
- Invoice intelligence patterns

---

<h2 id="model-evaluation">📈 Model Evaluation</h2>

Evaluation metrics used:

- R² Score
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

The models were evaluated on test datasets to ensure prediction reliability.

---

<h2 id="business-insights-generated">💡 Business Insights Generated</h2>

The project provides insights such as:

- Top-performing vendors
- Vendors with high freight costs
- Sales performance analysis
- Purchase trend analysis
- Invoice intelligence patterns
- Vendor contribution analysis

---

<h2 id="logging-and-monitoring">📝 Logging and Monitoring</h2>

The system includes logging functionality for:

- Data ingestion tracking
- SQL execution monitoring
- Error handling
- Pipeline execution status

---

<h2 id="key-features">🚀 Key Features</h2>

- Automated data pipeline
- SQL analytics engine
- Freight cost prediction
- Vendor intelligence reporting
- Invoice flagging system
- Model evaluation workflow
- Scalable project structure

---

<h2 id="future-improvements">🔮 Future Improvements</h2>

Possible future enhancements:

- Streamlit dashboard integration
- Real-time prediction APIs
- Cloud deployment
- Advanced anomaly detection
- Power BI dashboard integration
- Automated reporting system

---

<h2 id="conclusion">✅ Conclusion</h2>

This project demonstrates a complete end-to-end Data Analytics and Machine Learning workflow involving:

- Data ingestion
- SQL analysis
- Data preprocessing
- Feature engineering
- Model development
- Business intelligence generation
- Model deployment with Streamlit

The system helps automate vendor analytics and freight prediction processes using modern data analytics techniques.

---

## ▶️ How to Run This Project

<h2 id="how-to-run-this-project">🚀 How to Run This Project</h2>

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/vendor-performance-analysis.git
```

### 2️⃣ Navigate to project directory

```bash
cd vendor-performance-analysis
```

### 3️⃣ Install required libraries

```bash
pip install -r requirements.txt
```

### 4️⃣ Load the CSVs and ingest into database

```bash
python scripts/ingestion_db.py
```

### 5️⃣ Run the freight prediction pipeline

```bash
python freight_cost_prediction/train.py
```

### 6️⃣ Run inference

```bash
python inference/predict_freight.py
```

### 7️⃣ Launch Streamlit app (Optional)

```bash
streamlit run app.py
```

<h2 id="author">👨‍💻 Author</h2>

## Vivek Raj Verma

Data Scientist