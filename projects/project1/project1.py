
# Using the us-500.csv file. Organize the data by state in alphabetical order.
# Let's create a script that organizes the data by state in alphabetical order



import pandas as pd

# Load the dataset
file_path = 'us-500.csv'
data = pd.read_csv(file_path)
# First, we'll sort the data by the 'state' column
# sorted_data = data.sort_values(by='state')

# # Now, we'll write the sorted data to a new CSV file
# sorted_file_path = 'sorted_us-500_by_state.csv'
# sorted_data.to_csv(sorted_file_path, index=False)

# sorted_file_path



# First, let's make a list of all columns with 'state' at the front
# columns = ['state'] + [col for col in data.columns if col != 'state']

# # Reorder the dataframe columns
# reordered_data = data[columns]

# # Now, we'll sort the data by the 'state' column again
# reordered_sorted_data = reordered_data.sort_values(by='state')

# # Write the reordered and sorted data to a new CSV file
# reordered_sorted_file_path = 'reordered_sorted_us-500_by_state.csv'
# reordered_sorted_data.to_csv(reordered_sorted_file_path, index=False)

# reordered_sorted_file_path


# To create a separate CSV file containing only the people in New York (NY) state, we filter the data

# Filtering the data for New York state
ny_data = data[data['state'] == 'NY']

# Write the New York data to a new CSV file
ny_file_path = 'ny_contacts.csv'
ny_data.to_csv(ny_file_path, index=False)

ny_file_path

