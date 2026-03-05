# 💳 Credit Risk Prediction System

An end-to-end **Machine Learning application** that predicts the probability of a borrower defaulting on a loan.

This project demonstrates the complete **machine learning workflow**, including:

* Exploratory Data Analysis (EDA)
* Data preprocessing
* Feature engineering
* Model training and comparison
* Model selection
* Deployment of an interactive web application

The final model is deployed as a **Streamlit web app** for real-time credit risk prediction.

---

# 🚀 Live Demo

Try the application here:

👉 https://huggingface.co/spaces/vsharma142004/credit-risk-prediction

---

# 📊 Project Overview

Financial institutions assess various financial indicators before approving loans.
This project simulates a simplified **credit risk assessment system** that predicts the likelihood of loan default based on applicant financial data.

Users can input financial information such as:

* Annual Income
* Loan Amount
* Credit History

The system then:

1️⃣ Calculates engineered financial features
2️⃣ Uses a trained machine learning model to estimate default probability
3️⃣ Displays risk classification and visual insights

The prediction is presented through an **interactive dashboard** that includes risk metrics and feature contribution visualization.

---

# 🧠 Machine Learning Pipeline

This project follows a complete **ML pipeline**:

### 1️⃣ Exploratory Data Analysis (EDA)

Initial analysis was performed to understand:

* Feature distributions
* Relationships between variables
* Outliers and anomalies
* Correlation between financial indicators

---

### 2️⃣ Data Preprocessing

The dataset was cleaned and prepared using:

* Handling missing values
* Feature scaling
* Log transformations for skewed financial data

---

### 3️⃣ Feature Engineering

New features were created to improve predictive performance.

Engineered features include:

```
log_income
log_loan_amount
loan_to_income_ratio
credit_history
```

Feature transformations:

* **Log transformation** of income
* **Log transformation** of loan amount
* **Loan-to-Income Ratio** calculation

These transformations improve model stability and help capture financial risk patterns.

---

### 4️⃣ Model Training & Comparison

Multiple machine learning models were trained and evaluated:

* Logistic Regression
* Random Forest
* XGBoost

Models were evaluated using:

* ROC-AUC Score
* Accuracy
* Classification performance

### 📈 Model Performance

| Model               | ROC-AUC   |
| ------------------- | --------- |
| Logistic Regression | **0.659** |
| Random Forest       | Lower     |
| XGBoost             | Lower     |

**Logistic Regression achieved the best performance and was selected as the final model.**

Advantages of Logistic Regression in this problem:

* Strong baseline performance
* High interpretability
* Stable predictions
* Efficient for structured financial data

---

# 📊 Application Features

### 🔍 Real-Time Risk Prediction

Users can enter applicant financial details and instantly receive a loan risk evaluation.

---

### 📈 Risk Dashboard

The application displays:

* Default probability
* Risk classification
* Risk score gauge
* Visual metrics

---

### 📉 Feature Contribution Visualization

A bar chart shows how each financial feature contributes to the predicted risk.

---

### 💡 Financial Risk Insights

The system analyzes the **loan-to-income ratio** and provides contextual feedback:

* Healthy financial balance
* Moderate exposure
* High financial risk

---

# 🖥️ Application Interface

The Streamlit app includes:

* Financial input panel
* Risk probability display
* Interactive gauge visualization
* Feature contribution charts
* Financial insight messages

---

# 🛠️ Tech Stack

### Programming Language

Python

---

### Machine Learning

* scikit-learn
* XGBoost

---

### Data Processing

* pandas
* numpy

---

### Visualization

* plotly

---

### Web Application

Streamlit

---

### Deployment

Hugging Face Spaces

---

# 📂 Project Structure

```
credit-risk-prediction
│
├── app.py              # Streamlit application
├── model.pkl           # Trained ML model
├── requirements.txt    # Project dependencies
├── Dockerfile          # Deployment configuration
└── README.md           # Project documentation
```

---

# ⚙️ Installation & Running Locally

### 1️⃣ Clone the repository

```
git clone https://github.com/yourusername/credit-risk-prediction.git
cd credit-risk-prediction
```

---

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Run the application

```
streamlit run app.py
```

The app will open in your browser:

```
http://localhost:8501
```

---

# 📊 Example Prediction Flow

1️⃣ Enter applicant financial details
2️⃣ Click **Assess Risk**
3️⃣ Model calculates default probability
4️⃣ Dashboard displays:

* Risk category
* Default probability
* Risk score gauge
* Feature impact chart

---

# ⚠️ Disclaimer

This project is built **for educational and demonstration purposes only**.

It should **not be used for real-world financial decision making.**

---

# 👨‍💻 Author

**Vansh Sharma**

Machine Learning Enthusiast | AI Developer

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
