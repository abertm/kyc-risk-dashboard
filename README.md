# KYC Risk Dashboard – Mock Customer Analysis

## Overview
This project demonstrates a **mock KYC (Know Your Customer) dashboard** built with Python, Streamlit, and Plotly.  
It showcases the creation of a synthetic customer dataset, risk flagging, verification status, and an interactive dashboard suitable for fintech or compliance environments.

## Features
- Filter customers by **country, verification status, and risk flag**  
- Search customers by **name or ID**  
- Key metrics displayed: **Total Customers, High/Low Risk, Verification Status Counts**  
- Interactive charts:  
  - Risk Flag Distribution (Pie Chart)  
  - Verification Status Distribution (Pie Chart)  
  - Customers by Country (Bar Chart)  
  - High/Low Risk Customers by Verification Status (Stacked Bar Chart)  

## Dataset
- Generated with [Faker](https://faker.readthedocs.io/)  
- Contains **1000 mock customers**  
- 9 columns: `first_name`, `last_name`, `dob`, `country_code`, `id_number`, `email`, `phone`, `risk_flag`, `status`  
- Binary `risk_flag`: `High` / `Low`  

## Tech Stack
- Python 3.x  
- [Streamlit](https://streamlit.io/) – interactive dashboard  
- [Pandas](https://pandas.pydata.org/) – data manipulation  
- [Plotly Express](https://plotly.com/python/plotly-express/) – visualizations  
- [Faker](https://faker.readthedocs.io/) – mock data generation  

## How to Run
1. Clone the repository:  
```bash
git clone https://github.com/YOUR_USERNAME/kyc-risk-dashboard.git
cd kyc-risk-dashboard
