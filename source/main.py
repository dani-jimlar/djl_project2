"""
This fun prints descriptive analytics of a data set
"""

import pandas as pd
 
def print_ds_info(data):
    """
    parameter:data
    uses data.columns and describe() to print descriptive info of dataset
    """
    print("The variables in this data set are the following:",list(data.columns))
    print("Data behaves as follows:\n", data.describe())


if __name__ == "__main__":

    # Read the CSV file
    my_data = pd.read_csv("djl_project2/source/m2s2p20_cnije2022.csv", encoding="ISO-8859-1")

    # Print dataset info
    print_ds_info(my_data)



