# generate_mock_customers.py

from faker import Faker
import pandas as pd
import random
import os

fake = Faker()

# Number of mock clients
num_clients = 1000

# List to hold client data
clients = []

# High-risk countries for example purposes
high_risk_countries = ['NG', 'PK', 'IR', 'KP', 'SD']

for _ in range(num_clients):
    first_name = fake.first_name()
    last_name = fake.last_name()
    dob = fake.date_of_birth(minimum_age=18, maximum_age=80)
    country = fake.country_code()
    id_number = fake.ssn()
    email = fake.email()
    phone = fake.phone_number()

# Simple KYC risk flag example
    risk_flag = 'High' if country in high_risk_countries or random.random() < 0.05 else 'Low'

    clients.append({
    'first_name': first_name,
    'last_name': last_name,
    'dob': dob,
    'country_code': country,
    'id_number': id_number,
    'email': email,
    'phone': phone,
    'risk_flag': risk_flag,
    'status': random.choice(['Verified', 'Pending', 'Flagged'])
})

# Convert to DataFrame
df = pd.DataFrame(clients)

# --- Add Verification Status ---
df['status'] = [random.choice(['Verified', 'Pending', 'Flagged']) for _ in range(len(df))]


# CSV Saving 

# 1. Set the folder where you want the CSV to be saved
save_folder =r"C:\Users\afber\Documents\Data Analysis\Proyectos Code\Fintech_project\kyc_db\kyc_csv"   # raw string for backslashes

# 2. Make sure the folder exists
os.makedirs(save_folder, exist_ok=True)

# 3. Full path for CSV
csv_path = os.path.join(save_folder, 'mock_customers_large.csv')

# 4. Save the DataFrame
df.to_csv(csv_path, index=False)

# 5. Print confirmation and first 5 rows
print(f"CSV file generated at: {csv_path}")
print(df.head())

