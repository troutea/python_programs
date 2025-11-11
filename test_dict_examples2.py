from dict_examples2 import dict_examples2

class TestDictExamples2:
    """Test suite for dict_examples2 function"""
    
    def test_returns_list(self):
        """Test that the function returns a list"""
        result = dict_examples2()
        print("the results is " , result)
        assert isinstance(result, list)
    
    def test_contains_expected_values(self):
        """Test that result contains all unique values from the dictionary"""
        result = dict_examples2()
        expected_values = {1, 2, 5, 6, 7, 8, 10, 11, 12}
        assert set(result) == expected_values
    
    def test_no_duplicates(self):
        """Test that the result has no duplicate values"""
        result = dict_examples2()
        assert len(result) == len(set(result))
    
    def test_correct_length(self):
        """Test that the result has the correct number of unique values"""
        result = dict_examples2()
        assert len(result) == 9  # There are 9 unique values
    
    def test_all_integers(self):
        """Test that all values in result are integers"""
        result = dict_examples2()
        assert all(isinstance(x, int) for x in result)
    
    def test_prints_output(self, capsys):
        """Test that the function prints the expected output"""
        dict_examples2()
        captured = capsys.readouterr()
        assert "the resulst is res" in captured.out
        assert "[" in captured.out  # Check that a list is printed


# # Additional edge case tests if you refactor the function
# class TestDictExamples2EdgeCases:
#     """Edge case tests (would require modifying the function to accept parameters)"""
    
#     def test_empty_dict_scenario(self):
#         """Example test for empty dictionary (requires parameterized version)"""
#         # This would test: d = {}
#         # Expected result: []
#         pass
    
#     def test_single_key_scenario(self):
#         """Example test for single key dictionary"""
#         # This would test: d = {'key': [1, 2, 3]}
#         # Expected result: [1, 2, 3]
#         pass
