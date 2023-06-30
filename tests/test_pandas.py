from learn import learn_pandas


def test_slice_dataframe_keep():
    out_df = learn_pandas.slice_dataframe_keep()
    assert all(out_df.row_num == ["1", "2"])
    assert all(out_df.label1 == ["boy", "apple"])
    assert all(out_df.label2 == ["pie", "pie"])


def test_slice_dataframe_exclude():
    out_df = learn_pandas.slice_dataframe_exclude()
    assert all(out_df.row_num == ["0", "3"])
    assert all(out_df.label1 == ["banana", "apple"])
    assert all(out_df.label2 == ["apple", "cheese"])
