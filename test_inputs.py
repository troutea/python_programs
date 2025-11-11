# test_inputs = [1,2,10,50,100,149,150]
# expected_results = [2,3,11,51,101,150,151]
# for test_input in test_inputs, expected_results:
#     print(test_input)
#     test_value = test_input
#     print("the test value is ", test_value)
    
    
test_inputs = [1, 2, 10, 50, 100, 149, 150]
expected_results = [2, 3, 11, 51, 101, 150, 151]

# Loop through both arrays at the same time
for input_val, expected in zip(test_inputs, expected_results):
    print(f"Input: {input_val}, Expected: {expected}")
    
    