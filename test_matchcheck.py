import mock 
import pytest
from mock import MagicMock

from mock import patch

from pytest_mock import mocker 
#from  mathcheck import sums
import mathcheck

@patch('mathcheck.sums')
def test_answer(mock_sums):
    mock_sums.return_value = 5
    result =  mathcheck.sums(3,8)
    ###assert result == 5
    mock_sums.assert_called_once_with(3,8)


def test_answer1():
    mathcheck.sums = MagicMock(return_value=3,name ="test")
    result =  mathcheck.sums(3,8)
    assert result == 3
    mathcheck.sums.assert_called_once_with(3,9)
