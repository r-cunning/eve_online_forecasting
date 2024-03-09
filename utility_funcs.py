import pandas as pd

import pandas as pd

def z_score_normalize_separate_types(df, columns, type_id_col, year_col):
    """
    Applies Z-score normalization to specified columns in a pandas DataFrame,
    separated by type_id, and then returns a DataFrame organized by year.

    Args:
    df (pandas.DataFrame): The DataFrame containing the data.
    columns (list): List of column names to be normalized.
    type_id_col (str): The column name for type_id.
    year_col (str): The column name for year.

    Returns:
    pandas.DataFrame: The DataFrame with normalized columns, organized by year.
    """

    # Create an empty list to hold the dataframes
    dfs = []

    # Iterate over each group
    for type_id, group_df in df.groupby(type_id_col):
        for col in columns:
            if col in group_df.columns:
                # Apply Z-score normalization
                mean = group_df[col].mean()
                std = group_df[col].std()
                group_df[col + '_ZScore'] = (group_df[col] - mean) / std
            else:
                print(f"Column {col} not found in DataFrame.")
        
        # Drop NA values if any
        group_df = group_df.dropna()

        # Append the processed group to the list
        dfs.append(group_df)

    # Concatenate all the dataframes
    result_df = pd.concat(dfs)

    # Sort by year
    if year_col in result_df.columns:
        result_df = result_df.sort_values(by=year_col)
    else:
        print(f"Year column {year_col} not found in DataFrame.")

    return result_df



def z_score_normalize(df, columns):
    """
    Applies Z-score normalization to specified columns in a pandas DataFrame.

    Args:
    df (pandas.DataFrame): The DataFrame containing the data.
    columns (list): List of column names to be normalized.

    Returns:
    pandas.DataFrame: The DataFrame with additional normalized columns.
    """

    for col in columns:
        if col in df.columns:
            # mean = df[col].mean()
            # std = df[col].std()
            # df[col + '_ZScore'] = (df[col] - mean) / std
            df[col + '_ZScore'] = df[col].sub(df[col].expanding().mean()).div(df[col].expanding().std())
        else:
            print(f"Column {col} not found in DataFrame.")
            
        df = df.dropna()
    return df

# Example usage:
# Assuming 'df' is your DataFrame and you want to normalize columns 'value1' and 'value2'
# df = z_score_normalize(df, ['value1', 'value2'])
def moving_avg(data, columns, window=20):
    for column in columns:
        data[f'{column}_{window}_day_ma'] = data[column].rolling(window=window).mean().fillna(data[column])
    return data



import matplotlib.pyplot as plt


def plot_ma(data, column, color):
    fig, ax1 = plt.subplots()
    ax1.plot(data['date'], data[column], color=color)
    ax1.set_xlabel('Date')
    ax1.set_ylabel(column, color=color)
    ax1.tick_params('y', colors=color)
    plt.show()