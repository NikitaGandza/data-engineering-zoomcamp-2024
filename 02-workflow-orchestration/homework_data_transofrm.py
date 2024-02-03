if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    data = data.loc[data["passenger_count"] != 0]
    data = data.loc[data["trip_distance"] != 0]
    data["lpep_pickup_date"] = data["lpep_pickup_datetime"].dt.date
    data.columns = (data.columns.str.replace(" ", "_").str.lower())
    print(data["vendorid"].unique())
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'


@test 
def test_output_passengers(output, *args) -> None:
    assert output['passenger_count'].isin([0]).sum() == 0, '0 in passenger_count'


@test
def test_output_trip_distance(output, *args) -> None:
    assert output['trip_distance'].isin([0]).sum() == 0, '0 in trip_distance'


@test
def test_output_vendor(output, *args) -> None:
    # assert output['vendorid'].isin([1, 2]).sum() != 0, 'vendorid not in the list'
    assert output['vendorid'].isin([1,2]).all(), 'vendorid not in 1,2'