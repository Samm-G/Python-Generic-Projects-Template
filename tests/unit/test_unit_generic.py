import pytest
from python_generic.custom_exception import GenericException


good_data = [("Hi there!"), ("Hope you are fine"), ("Sam Here!")]

# Should throw exception for all these.
bad_data = [([1, 2, 3]), (124), ({"ssda"})]

# Check if all these are strings.
# This decorator automatically runs the test for 'good_data'
@pytest.mark.parametrize("input_param", good_data)
def test_check_if_string(input_param):
    assert isinstance(input_param, str)


@pytest.mark.parametrize("input_param", bad_data)
def test_check_if_string_failed(input_param):
    with pytest.raises(GenericException):
        if isinstance(input_param, str) == False:
            raise GenericException
