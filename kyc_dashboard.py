import streamlit as st
import pandas as pd
import plotly.express as px

# Load CSV from the kyc_csv folder
df = pd.read_csv(
    r"C:/Users/afber/Documents/Data Analysis/Proyectos Code/Fintech_project/kyc_db/kyc_csv/mock_customers_large.csv",
    encoding='utf-8'
)


# Dashboard Title
st.title("KYC Dashboard")

# Sidebar Filters
st.sidebar.header("Filter Customers")

# Country filter
countries = df['country_code'].unique()
selected_country = st.sidebar.selectbox("Select Country", ["All"] + list(countries))

# Verification Status filter (replace 'status' with the exact column name in your CSV)
statuses = df['status'].unique()
selected_status = st.sidebar.selectbox("Select Verification Status", ["All"] + list(statuses))

# Risk Flag filter
risk_flags = df['risk_flag'].unique()
selected_risk = st.sidebar.selectbox("Select Risk Flag", ["All"] + list(risk_flags))

# Search box
search_name = st.sidebar.text_input("Search by Customer Name or ID")

# Apply Filters 
filtered_df = df.copy()

if selected_country != "All":
    filtered_df = filtered_df[filtered_df['country_code'] == selected_country]

if selected_status != "All":
    filtered_df = filtered_df[filtered_df['status'] == selected_status]

if selected_risk != "All":
    filtered_df = filtered_df[filtered_df['risk_flag'] == selected_risk]

if search_name:
    filtered_df = filtered_df[
        (filtered_df['first_name'] + " " + filtered_df['last_name']).str.contains(search_name, case=False) |
        filtered_df['id_number'].astype(str).str.contains(search_name)
    ]


# Key KPIs
total_customers = len(filtered_df)
high_risk = len(filtered_df[filtered_df['risk_flag'] == 'High'])
low_risk = len(filtered_df[filtered_df['risk_flag'] == 'Low'])
verified = len(filtered_df[filtered_df['status'] == 'Verified'])
pending = len(filtered_df[filtered_df['status'] == 'Pending'])
flagged = len(filtered_df[filtered_df['status'] == 'Flagged'])

st.subheader("KYC Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Customers", total_customers)
col2.metric("High Risk Customers", high_risk)
col3.metric("Low Risk Customers", low_risk)

col4, col5, col6 = st.columns(3)
col4.metric("Verified", verified)
col5.metric("Pending", pending)
col6.metric("Flagged", flagged)

# Display filtered data
st.subheader("Filtered Customers")
st.dataframe(filtered_df, height = 250)

# Charts

# Risk Flag Distribution (Pie Chart) 
risk_counts = filtered_df['risk_flag'].value_counts().reset_index()
risk_counts.columns = ['risk_flag', 'count']

fig_risk = px.pie(
    risk_counts,
    names='risk_flag',
    values='count',
    title='Risk Flag Distribution',
    color='risk_flag',
    color_discrete_map={'High':'red', 'Low':'green'}
)
st.plotly_chart(fig_risk)

# Verification Status Distribution (Pie Chart) 
status_counts = filtered_df['status'].value_counts().reset_index()
status_counts.columns = ['status', 'count']

fig_status = px.pie(
    status_counts,
    names='status',
    values='count',
    title='Verification Status Distribution',
    color='status',
    color_discrete_map={'Verified':'green', 'Pending':'orange', 'Flagged':'red'}
)
st.plotly_chart(fig_status)

# Customers by Country (Bar Chart) 
country_counts = filtered_df['country_code'].value_counts().reset_index()
country_counts.columns = ['country_code', 'count']

fig_country = px.bar(
    country_counts,
    x='country_code',
    y='count',
    title='Customers by Country',
    color='count',
    color_continuous_scale='Blues'
)
st.plotly_chart(fig_country)

# High-Risk Customers by Verification Status (Stacked Bar Chart) 
risk_status_counts = filtered_df.groupby(['status', 'risk_flag']).size().reset_index(name='count')

fig_risk_status = px.bar(
    risk_status_counts,
    x='status',
    y='count',
    color='risk_flag',
    title='High/Low Risk Customers by Verification Status',
    color_discrete_map={'High':'red', 'Low':'green'},
    barmode='stack'
)
st.plotly_chart(fig_risk_status)




# Folder kyc
# cd "C:\Users\afber\Documents\Data Analysis\Proyectos Code\Fintech_project\kyc_db"
# streamlit run kyc_dashboard.py
