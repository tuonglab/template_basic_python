import pandas as pd


def slice_dataframe_keep() -> pd.DataFrame:
    """
    This function wants to slice the dataframe to just row_num 1 and 2.

    Returns
    -------
    pd.DataFrame
        A sliced dataframe with only 2 specific rows.
    """
    original_df = pd.DataFrame(
        {
            "row_num": ["0", "1", "2", "3"],
            "label1": ["banana", "boy", "apple", "apple"],
            "label2": ["apple", "pie", "pie", "cheese"],
        }
    )
    new_df = original_df[original_df["row_num"] == ["1", "2"]]
    return new_df


def slice_dataframe_exclude() -> pd.DataFrame:
    """
    This function is wanting to exclude certain rows from the dataframe.

    Returns
    -------
    pd.DataFrame
        A sliced dataframe with without 2 specific rows.
    """
    original_df = pd.DataFrame(
        {
            "row_num": ["0", "1", "2", "3"],
            "label1": ["banana", "boy", "apple", "apple"],
            "label2": ["apple", "pie", "pie", "cheese"],
        }
    )
    new_df = original_df[original_df["label1"].isin(["pie"])]
    return new_df
