import sys
import shutil
import os

def zip_directory(directory_path, zip_file_path):
    shutil.make_archive(zip_file_path, 'zip', directory_path)

# Get normal string input from user for directory path and zip file path
directory_path = input("Enter the path of the directory to be archived (e.g. C:\\example\\directory): ")
zip_file_path = input("Enter the path of the zip file to be created (e.g. C:\\example\\directory) (without .zip extension): ")

# Convert normal string inputs into raw string inputs
directory_path = r"{}".format(directory_path)
zip_file_path = r"{}".format(zip_file_path)

# Example usage
zip_directory(directory_path, zip_file_path)
