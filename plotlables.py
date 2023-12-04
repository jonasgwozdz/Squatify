import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_movement_data(csv_file_path):
    # Read the data from the CSV file
    data = pd.read_csv(csv_file_path, delimiter=';')

    # Calculate the average hip height
    data['Average_Hip_Height'] = (data['Left hip_y'] + data['Right hip_y']) / 2

    # Define custom color mapping for movement types
    custom_color_mapping = {'Pause': 'yellow', 'Ascending': 'green', 'Descending': 'red'}

    # Plotting the data
    plt.figure(figsize=(15, 6))
    sns.scatterplot(x=data['Timestamp'], y=data['Average_Hip_Height'], 
                    hue=data['Label'], palette=custom_color_mapping)

    plt.title('Average Hip Height with Movement Labels')
    plt.xlabel('Timestamp')
    plt.ylabel('Average Hip Height')
    plt.legend(title='Movement Type')
    plt.show()

# Usage
csv_file_path = 'tracking_data/Tracking_Video02_lable.csv'  # Replace with your CSV file path
plot_movement_data(csv_file_path)
