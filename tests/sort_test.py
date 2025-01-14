"""Tests for sort module"""
from unittest.mock import patch, MagicMock

import pytest

from sort import sort


@patch('sort.sort.write_txt')
def test_sort(mock_write_txt, capsys):
    """Test output validity"""
    expected_list = sort.read_txt('res/expected.txt')

    args = MagicMock(file='res/input.txt', backup=False)
    sort.main(args)

    mock_write_txt.assert_called_once()
    _, sorted_list = mock_write_txt.call_args[0]
    assert sorted_list == expected_list

    captured_stdout = capsys.readouterr()
    assert captured_stdout.out == 'Wrote 3 entries to file!\n'


@patch('sort.sort.check_list_lengths')
@patch('sort.sort.write_txt')
def test_sort_error(mock_write_txt, mock_check_list_lengths):
    """Test ValueError raise"""
    mock_check_list_lengths.return_value = False
    args = MagicMock(file='res/input.txt', backup=False)

    with pytest.raises(ValueError):
        sort.main(args)

    mock_write_txt.assert_not_called()


def test_datablocks_to_list():
    """Test datablocks_to_list() function"""
    expected_list = sort.read_txt('res/expected.txt')
    datablocks = sort.list_to_datablocks(expected_list)
    sorted_blocks = sort.sort_datablocks(datablocks)
    sorted_list = sort.datablocks_to_list(sorted_blocks)

    assert sorted_list == expected_list


def test_check_list_lengths():
    """Test check_list_lengths() function"""
    expected_list = sort.read_txt('res/expected.txt')
    datablocks = sort.list_to_datablocks(expected_list)
    sorted_blocks = sort.sort_datablocks(datablocks)
    sorted_list_eq = sort.datablocks_to_list(sorted_blocks)
    sorted_list_neq = sorted_list_eq[:len(sorted_list_eq)-2]

    assert sort.check_list_lengths(sorted_list_eq, expected_list)
    assert not sort.check_list_lengths(sorted_list_neq, expected_list)
