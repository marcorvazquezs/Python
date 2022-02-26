#!/bin/bash

# Author:                 Marco Vazquez
# Purpose:                Solution Class 3

# Ask user to input a directory
echo "Input a directory path:"
read input_dir

echo "Input a three-digit security settings"
read input_permissions

chmod -R $input_dir $input_permissions

ls -al $input_dir
