from learn import learn_list


def test_concat_list():
    assert learn_list.concat_lists() == [
        "1",
        "2",
        "3",
        "4",
        "apple",
        "boy",
        "pie",
        "cheese",
    ]


def test_merging_contents_of_two_lists():
    assert learn_list.merging_contents_of_two_lists() == [
        "1_apple",
        "2_boy",
        "3_pie",
        "4_cheese",
    ]


def test_unique_items():
    assert learn_list.unique_items() == {
        "leek",
        "apple",
        "pie",
        "banana",
        "boy",
        "cheese",
    }


def test_unique_list_format():
    assert sorted(learn_list.unique_list_format()) == [
        "apple",
        "banana",
        "boy",
        "cheese",
        "leek",
        "pie",
    ]
