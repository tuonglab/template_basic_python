from learn import learn_dict


def test_convert_all():
    assert learn_dict.convert_all() == [
        "apple",
        "boy",
        "pie",
        "cheese",
        "banana",
    ]


def test_convert_wrong():
    assert learn_dict.convert_wrong() == [
        "apple",
        "apple",
        "pie",
        "pie",
        "banana",
    ]
