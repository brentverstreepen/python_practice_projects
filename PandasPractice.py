import pandas as pd

# TASK #6: UNDERSTAND PANDAS FUNDAMENTALS
print("---TASK 6---")
# Define a two-dimensional Pandas DataFrame
bank_client_df = pd.DataFrame({"Bank Client ID": [111, 222, 333, 444],
                              "Bank Client Name": ["Chanel", "Steve", "Mitch", "Ryan"],
                              "Net Worth [$]": [3500, 29000, 10000, 2000],
                              "Years with bank": [3, 4, 9, 5]})
print(bank_client_df)

# View first or last rows using .head() and .tail()
print(bank_client_df.head(2))
print(bank_client_df.tail(1))

# MINI CHALLENGE #6:
# A portfolio contains a collection of securities such as stocks, bonds and ETFs. Define a dataframe named 'portfolio_df' that holds 3 different stock ticker symbols, number of shares, and price per share (feel free to choose any stocks)
# Calculate the total value of the portfolio including all stocks
print("\nMINI CHALLENGE #6:")
portfolio_df = pd.DataFrame({"Stock Ticker": ["AAPL", "NVDA", "NFLX"],
                             "Amount of Shares": [100, 50, 250],
                             "Price per Share ($)": [228.68, 131.41, 658.97]})
print(portfolio_df)
sumPortfolio = portfolio_df["Amount of Shares"] * portfolio_df["Price per Share ($)"]
print(f"Total value of portfolio: ${sumPortfolio.sum()}")

# TASK #7: PANDAS WITH CSV AND HTML DATA
print("\n---TASK 7---")
# Import data with .read_ command
house_prices = pd.read_html("https://www.livingin-canada.com/house-prices-canada.html")
print(house_prices[0])

# MINI CHALLENGE #7:
# Write a code that uses Pandas to read tabular US retirement data
# You can use data from here: https://www.ssa.gov/oact/progdata/nra.html
print("\nMINI CHALLENGE #7:")
retirement_df = pd.read_html("https://www.ssa.gov/oact/progdata/nra.html")
print(retirement_df)

# TASK #8: PANDAS OPERATIONS
print("\n---TASK 8---")
# Pick rows that satisfy a certain criteria (+5 years with bank for example)
bank_client_df = pd.DataFrame({"Bank Client ID": [111, 222, 333, 444],
                              "Bank Client Name": ["Chanel", "Steve", "Mitch", "Ryan"],
                              "Net Worth [$]": [3500, 29000, 10000, 2000],
                              "Years with bank": [3, 4, 9, 5]})
loyal_df = bank_client_df[bank_client_df["Years with bank"] >= 5]
print(loyal_df)

# Delete a column from a DataFrame
del bank_client_df["Bank Client ID"]
print(bank_client_df)

# MINI CHALLENGE #8:
# Using "bank_client_df" DataFrame, leverage pandas operations to only select high networth individuals with minimum $5000
# What is the combined networth for all customers with 5000+ net worth?
print("\nMINI CHALLENGE #8:")
networth_df = bank_client_df[bank_client_df["Net Worth [$]"] >= 5000]
print(networth_df["Net Worth [$]"].sum())

# TASK #9: PANDAS WITH FUNCTIONS
print("\n---TASK 9---")
# Increase all clients networth by a fixed value of 20% (for simplicity sake) with a function
def increase_networth(networth):
    return networth * 1.2
print(bank_client_df["Net Worth [$]"].apply(increase_networth))

# MINI CHALLENGE #9:
# Define a function that triples the net worth and then adds $200
# Apply the function to the DataFrame
# Calculate the updated total networth of all clients combined
def increase_price(price):
    return (price * 3) + 200
print(bank_client_df["Net Worth [$]"].apply(increase_price))

# TASK #10: PERFORM SORTING AND ORDERING IN PANDAS
print("\n---TASK 10---")
# Sort the values in the DataFrame according to number of years with bank
bank_client_df = pd.DataFrame({'Bank client ID': [111, 222, 333, 444],
                               'Bank Client Name': ['Chanel', 'Steve', 'Mitch', 'Ryan'],
                               'Net worth [$]': [3500, 29000, 10000, 2000],
                               'Years with bank': [3, 4, 9, 5]})
print(bank_client_df.sort_values(by="Years with bank"))

# Set inplace = True to ensure that change has taken in memory
(bank_client_df.sort_values(by="Years with bank", inplace=True))
print(bank_client_df)

# TASK #11: PERFORM CONCATENATING AND MERGING WITH PANDAS
print("\n---TASK 11---")
# Concatenate two DataFrames together
df1 = pd.DataFrame({"A": ["A0", "A1", "A2", "A3"],
                    "B": ["B0", "B1", "B2", "B3"],
                    "C": ["C0", "C1", "C2", "C3"],
                    "D": ["D0", "D1", "D2", "D3"]}, index=[0, 1, 2, 3])
print(df1)
df2 = pd.DataFrame({"A": ["A4", "A5", "A6", "A7"],
                    "B": ["B4", "B5", "B6", "B7"],
                    "C": ["C4", "C5", "C6", "C7"],
                    "D": ["D4", "D5", "D6", "D7"]}, index=[4, 5, 6, 7])
print(df2)
df3 = pd.DataFrame({"A": ["A8", "A9", "A10", "A11"],
                    "B": ["B8", "B9", "B10", "B11"],
                    "C": ["C8", "C9", "C10", "C11"],
                    "D": ["D8", "D9", "D10", "D11"]}, index=[8, 9, 10, 11])
print(df3)
print(pd.concat([df1, df2, df3]))

# TASK #12: PROJECT AND CONCLUDING REMARKS
print("\n---TASK 12---")
# Define a dataframe named 'Bank_df_1' that contains the first and last names for 5 bank clients with IDs = 1, 2, 3, 4, 5
# Assume that the bank got 5 new clients, define another dataframe named 'Bank_df_2' that contains a new clients with IDs = 6, 7, 8, 9, 10
# Let's assume we obtained additional information (Annual Salary) about all our bank customers (10 customers)
# Concatenate both 'bank_df_1' and 'bank_df_2' dataframes
# Merge client names and their newly added salary information using the 'Bank Client ID'
# Let's assume that you became a new client to the bank
# Define a new DataFrame that contains your information such as client ID (choose 11), first name, last name, and annual salary.
# Add this new dataframe to the original dataframe 'bank_df_all'.

# Create first DF
bank_df_1 = pd.DataFrame({"Bank Client ID": [1, 2, 3, 4, 5],
                          "First Name": ["Nancy", "Alex", "Jeff", "Max", "Jerome"],
                          "Last Name": ["Pelosi", "Agnew", "Bezos", "Verstappen", "Powell"]
                          })
print(bank_df_1)
# Create second DF
bank_df_2 = pd.DataFrame({"Bank Client ID": [6, 7, 8, 9, 10],
                          "First Name": ["John", "Dom", "Elon", "James", "Mule"],
                          "Last Name": ["Summit", "Dolla", "Musk", "Hype", "Skinner"]
                          })
print(bank_df_2)
# Create DF with extra data
extra_data = {"Bank Client ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
              "Annual Salary in $": [25000, 35000, 45000, 85000, 60000, 32000, 71000, 50000, 42000, 48000]
              }
bank_salary_df = pd.DataFrame(extra_data, columns=["Bank Client ID", "Annual Salary in $"])
print(bank_salary_df)
# Concatenate DataFrames
bank_df_all = pd.concat([bank_df_1, bank_df_2])
print(bank_df_all)
# Merge DataFrames on "Bank Client ID"
bank_df_all = pd.merge(bank_df_all, bank_salary_df, on="Bank Client ID")
print(bank_df_all)
# Add new client
new_client = {"Bank Client ID": [11],
              "First Name": ["Brent"],
              "Last Name": ["Verstreepen"],
              "Annual Salary in $": [1000000]
              }
new_client_df = pd.DataFrame(new_client, columns=["Bank Client ID", "First Name", "Last Name", "Annual Salary in $"])
# Concatenate both dataframes #1 and #2
bank_df_all = pd.concat([bank_df_all, new_client_df])
print(bank_df_all)

print(bank_df_all.columns)
