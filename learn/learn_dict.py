ORIGINAL_LIST = ["0", "1", "2", "3", "4"]


def convert_all() -> list:
    """
    This function wants to convert the numbers as a string to new labels.

    Returns
    -------
    list
        A list containing the new labels.
    """
    convert_dict = {"0": "apple", "1": "boy", "2": "pie", "3": "cheese", "4": "banana"}
    new_list = convert_dict[ORIGINAL_LIST]
    return new_list


def convert_wrong() -> list:
    """
    This function wants to convert the numbers as a string to new labels but something goes wrong.
    Can you spot the mistake(s)?

    Returns
    -------
    list
        A list containing the new labels.
    """
    convert_dict = {"1": "apple", "1": "pie", "2": "pie", "3": "cheese", "4": "banana"}
    new_list = [convert_dict[x] for x in ORIGINAL_LIST]
    return new_list
