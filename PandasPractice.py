import pandas as pd

# TASK #6: UNDERSTAND PANDAS FUNDAMENTALS
# Define a two-dimensional Pandas DataFrame
bank_client_df = pd.DataFrame({"Bank Client ID":[111, 222, 333, 444],
                              "Bank Client Name":["Chanel", "Steve", "Mitch", "Ryan"],
                              "Net Worth [$]":[3500, 29000, 10000, 2000],
                              "Years with bank":[3, 4, 9, 5]})
print(bank_client_df)

# View first or last rows using .head() and .tail()
print(bank_client_df.head(2))
print(bank_client_df.tail(1))