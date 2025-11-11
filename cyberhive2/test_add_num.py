import pytest
import subprocess


def run_add_command(args):
    """
    Helper function to run the 'add' command with given arguments.
    Adjust the command based on your actual implementation.
    """
    # Replace 'python add.py' with your actual command
    cmd = ['python', 'add_num.py'] + args
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.strip(), result.stderr.strip(), result.returncode


class TestAddCommand:
    """Test suite for the 'add n' command."""

    # Test requirement: Running 'add n' produces output "Result: n+1"
    @pytest.mark.parametrize("n,expected", [
        (0, "Result: 1"),
        (1, "Result: 2"),
        (10, "Result: 11"),
        (50, "Result: 51"),
        (100, "Result: 101"),
        (149, "Result: 150"),
        (150, "Result: 151"),
    ])
    def test_add_produces_correct_output(self, n, expected):
        """Test that 'add n' produces 'Result: n+1'."""
        stdout, stderr, returncode = run_add_command([str(n)])
        assert stdout == expected, f"Expected '{expected}', got '{stdout}'"
        assert returncode == 0, "Command should exit successfully"

    # Test requirement: Valid inputs are integers in range [0..150]
    @pytest.mark.parametrize("n", [0, 1, 75, 149, 150])
    def test_valid_input_range(self, n):
        """Test that integers in range [0..150] are accepted."""
        stdout, stderr, returncode = run_add_command([str(n)])
        assert stdout.startswith("Result: "), f"Should produce valid output for {n}"
        assert returncode == 0, "Command should not error for valid input"

    # Test requirement: Invalid inputs outside range
    @pytest.mark.parametrize("n", [-1, -10, 151, 200, 1000])
    def test_invalid_input_range(self, n):
        """Test that integers outside range [0..150] are handled."""
        stdout, stderr, returncode = run_add_command([str(n)])
        # Application should still produce output and not crash
        assert returncode == 0, "Application should not error even with invalid range"

    # Test requirement: Results are consistent and deterministic
    def test_deterministic_results(self):
        """Test that running the same command multiple times produces same result."""
        test_value = 42
        results = []
        for _ in range(5):
            stdout, _, _ = run_add_command([str(test_value)])
            results.append(stdout)
        
        assert all(r == results[0] for r in results), \
            "Results should be consistent across multiple runs"
        assert results[0] == "Result: 43", "Result should be deterministic"

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
        stdout, stderr, returncode = run_add_command([text_input])
        # Application should produce output and not crash
        assert returncode == 0, "Application should not error with text input"
        # Should produce some output (even if it's an error message)
        assert stdout or stderr, "Application should produce some output"

    # Test requirement: Additional parameters are ignored
    @pytest.mark.parametrize("n,extra_params", [
        (5, ["10", "15"]),
        (20, ["extra", "params"]),
        (30, ["100"]),
    ])
    def test_additional_parameters_ignored(self, n, extra_params):
        """Test that additional parameters beyond the first are ignored."""
        # Run with just the first parameter
        stdout_single, _, _ = run_add_command([str(n)])
        
        # Run with additional parameters
        stdout_multiple, _, returncode = run_add_command([str(n)] + extra_params)
        
        # Results should be the same (additional params ignored)
        assert stdout_single == stdout_multiple, \
            "Additional parameters should be ignored"
        assert returncode == 0, "Command should not error with extra parameters"

    # Test requirement: Application always produces expected output and does not error
    def test_no_errors_on_valid_input(self):
        """Test that application doesn't error on valid inputs."""
        for n in range(0, 151):
            stdout, stderr, returncode = run_add_command([str(n)])
            assert returncode == 0, f"Application errored on valid input {n}"
            assert stdout, f"Application produced no output for {n}"

    def test_empty_parameters(self):
        """Test behavior with no parameters."""
        stdout, stderr, returncode = run_add_command([])
        # Should produce output and not crash
        assert returncode == 0, "Application should not crash with no parameters"

    # Edge cases
    def test_float_input(self):
        """Test that float inputs are handled."""
        stdout, stderr, returncode = run_add_command(["10.5"])
        assert returncode == 0, "Application should not error with float input"

    def test_special_characters(self):
        """Test that special characters are handled."""
        for char in ["!", "@", "#", "$", "%"]:
            stdout, stderr, returncode = run_add_command([char])
            assert returncode == 0, f"Application should not crash with '{char}'"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])