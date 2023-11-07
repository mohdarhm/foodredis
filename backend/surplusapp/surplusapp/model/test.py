import os

current_directory = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(current_directory, "generated_data.csv")

print(file_path)