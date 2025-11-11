import sys

if len(sys.argv) > 1:
    try:
        n = int(sys.argv[1])
        print(f"Result: {n + 1}")
    except ValueError:
        print("Error: Invalid input")
else:
    print("Error: No parameter provided")