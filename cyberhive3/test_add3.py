import pytest
import subprocess

from add3 import add_command
  
  
class TestAddCommand: 
    """Test suite for the 'add n' command."""
    
   # Test requirement: Running 'add n' produces output "Result: n+1"
    @pytest.mark.parametrize("n, expected", [
            (0, 1),
            (1, 2),
             (10, 11),
             (50, 51),
            (100, 101),
            (149, 150),
            (150, 151),
        ]) 
    
    
    def test_add_produces_correct_output(self,n, expected):
        returncode = add_command(n)
        print("The input value is",n ,"the expected value is",returncode )
        assert returncode == expected
    
     # Test requirement: Valid inputs are integers in range [0..150]
    @pytest.mark.parametrize("n", [0, 1, 75, 149, 150])
    def test_valid_input_range(self, n):
        returncode = add_command(n)
        print("The input value is",n ,"the expected value is",returncode )
        assert add_command(n)
    
     # Test requirement: Invalid inputs outside range 
    @pytest.mark.parametrize("n", [-1, -10, 151, 200, 1000])
    def test_invalid_input_range(self, n):
        # Application should still produce output and not crash
        returncode = add_command(n)
        print("The input value is",n ,"the expected value is",returncode )
        assert add_command(n)
        
    # Test requirement: Text parameters are unsupported
    @pytest.mark.parametrize("text_input", [
        "hello",
        "abc",
        "test",
        "123abc",
        "abc123",
    ])
   
    def test_text_parameters_unsupported(self, text_input):
        """Test that text parameters are handled appropriately."""
        returncode = add_command(text_input)
        print("The input value is",text_input ,"the expected value is",returncode )
        assert returncode == 'Invalid Input Text Characters not supported'
        
        
    # Test requirement: Results are consistent and deterministic
    def test_deterministic_results(self):
        """Test that running the same command multiple times produces same result."""
        test_value = 42
        results = []
        for _ in range(5):
            test_result = add_command(test_value)
            results.append(test_result)
        
        assert all(r == results[0] for r in results), \
            "Results should be consistent across multiple runs"
        assert results[0] == 43
       
        
   
   # Test requirement: Application always produces expected output and does not error
    def test_no_errors_on_valid_input(self):
        """Test that application doesn't error on valid inputs."""
        for n in range(0, 151):
             returncode = add_command(n)
             print("The input value is",n ,"the expected value is",returncode )
             assert (n + 1) == returncode
             
             
    import math      
    # Edge cases
    def test_float_input(self):
        """Test that float inputs are handled."""
        returncode = add_command(10.5)
        print("The input is float 10.5", "the result is ", returncode)
        assert returncode ==  11
             
    
   
    