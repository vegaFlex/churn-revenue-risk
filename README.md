## CHURN REVENUE RISK ANALYSIS

### Objective
This project assesses customer churn risk and expected revenue loss using a real telecom dataset.  
The model predicts churn probability and estimates potential revenue loss per customer.

### Data
- Telco Customer Churn dataset  
- 7043 customers  
- 22 feature columns  
- Target variable: `churn_flag` (binary)

### Methods
- Python Pandas for data preparation  
- EDA analysis and feature engineering  
- Logistic Regression model  
- Random Forest benchmark model  
- Power BI dashboard for business visualization  

### Key Results
- AUC Logistic Regression: **0.842**  
- AUC Random Forest: **0.822**  
- Base churn rate: **26.5%**  
- Expected revenue loss: **~497K**  
- Very high risk customers: **1761**

### Business Insights
- Month-to-month contracts show highest churn risk  
- Fiber optic customers churn more frequently  
- Higher monthly charges correlate with higher churn risk  
- Targeting high-risk customers can reduce revenue loss  

### Dashboard
Power BI dashboard includes:

- Churn probability by segment  
- Revenue at risk breakdown  
- Contract and internet service analysis  
- Top risk customers  

Dashboard file: `powerbi/churn_revenue_risk.pbix`  
Preview image: `reports/dashboard.png`

### Tech Stack
- Python  
- Pandas  
- Scikit-learn  
- SQL  
- Power BI  
- VS Code
