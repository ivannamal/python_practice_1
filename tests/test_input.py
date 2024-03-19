import pytest
from app.io.input import Input
def test_input_console():
    expected_result = "hello"
    input_res = Input(r"C:\Users\іванна\PycharmProjects\python-for-big-data-and-data-science\pythonProject4\example.txt")
    func_result = input_res.read_file()
    assert expected_result == func_result

def test_input_pandas():
    expected_result = """Empty DataFrame
Columns: [one,  two,  three,  four,  five]
Index: []"""
    input_res = Input(r"C:\Users\іванна\PycharmProjects\python-for-big-data-and-data-science\pythonProject4\example.csv")
    func_result = input_res.read_file_pandas()
    assert expected_result == func_result