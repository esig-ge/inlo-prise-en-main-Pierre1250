import unittest
def get_string():
    return "Selenium"

def get_list():
    return ["dog", "cat"]

def test_string_equal():
   assert get_string() == "Selenium"

def test_in_list():
    assert "elephant" in get_list()


if __name__ == "__main__":
    unittest.main()