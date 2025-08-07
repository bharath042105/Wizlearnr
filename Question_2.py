import numpy as np

def calculate_rms(data):
 data_array = np.array(data)
 mean_of_squares = np.mean(data_array**2)
 rms_value = float(np.sqrt(mean_of_squares))
 return rms_value
numbers = [1, 2, 3, 4, 5]
result = calculate_rms(numbers)
print(f"The calculated RMS is: {result}")
