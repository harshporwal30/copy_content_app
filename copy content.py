# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 20:01:00 2023

@author: Harsh
"""

def copy_content(source_file, destination_file):
    # Open the source file in read mode
    source = open(source_file, 'r')

    # Read the content of the source file
    content = source.read()

    # Close the source file
    source.close()

    # Open the destination file in write mode
    destination = open(destination_file, 'w')

    # Write the content to the destination file
    destination.write(content)

    # Close the destination file
    destination.close()

    print(f"Content copied from '{source_file}' to '{destination_file}' successfully.")

copy_content('source.txt', 'destination.txt')
