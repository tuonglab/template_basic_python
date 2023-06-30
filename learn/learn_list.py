LIST1 = ["1", "2", "3", "4"]
LIST2 = ["apple", "boy", "pie", "cheese"]
LIST3 = ["banana", "boy", "leek", "apple"]


def concat_lists() -> list:
    """
    This function is trying to concatenate the two lists together.
    Can you tell what this current code is doing?

    Returns
    -------
    list
        A new list that is the combination of 2 lists.
    """
    return LIST1 ^ LIST2


def merging_contents_of_two_lists() -> list:
    """
    This function is trying to create a new list so that I end up with
    my output is "1_apple", "2_boy" and so on.
    Can you tell why this is not working?

    Returns
    -------
    list
        A new list with outputs being "1_apple", "2_boy" and so on.
    """
    return [x + "_" + y for x, y in (LIST1 + LIST2)]


def unique_items() -> list:
    """
    Extracting unique elements in list.

    Returns
    -------
    list
        A list containing only unique elements.
    """
    return LIST2 + LIST3


def unique_list_format() -> list:
    """
    Extracting unique elements in list and output as list.

    Returns
    -------
    list
        A list containing only unique elements.
    """
    return set(LIST2 + LIST3)
