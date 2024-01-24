import pandas as pd

# Load data from the Excel file
data = pd.read_excel(r"C:\Users\perfr\PycharmProjects\pythonProject\token_wallets_withrepetetivs.xlsx", usecols=[0])

# Extract unique items from the DataFrame
items = data.iloc[:, 0].tolist()
unique_items = list(set(items))
# Save the unique items to a new Excel file
output_data = pd.DataFrame({'Unique_Items': unique_items})
output_file_path = r"C:\Users\perfr\PycharmProjects\pythonProject\singleuniquewallet.xlsx"
output_data.to_excel(output_file_path, index=False)

print("Task completed. Unique items have been saved to:", output_file_path)

