import pytest
import os
from io import StringIO
import sys
from hello_world import hello_world

def test_hello_world():
    captured_output = StringIO()
    sys.stdout = captured_output  

    hello_world() 
    sys.stdout = sys.__stdout__ 

    expected_output = (
        "***************************************\n"
        "*                                     *\n"
        "*           Hello, World!!!           *\n"
        "*                                     *\n"
        "***************************************\n"
    )

    assert captured_output.getvalue() == expected_output
    

def check_folder_exists(folder_name):
    """Check if a folder exists."""
    folder_path = os.path.join("Movie Mixup", folder_name)
    assert os.path.exists(folder_path), f"Folder {folder_name} is missing."

def check_files_in_folder(folder_name, expected_files):
    """Check if the correct files exist in a folder."""
    folder_path = os.path.join("Movie Mixup", folder_name)
    actual_files = set(f for f in os.listdir(folder_path) if f != ".DS_Store")
    expected_files_set = set(expected_files)
    assert actual_files == expected_files_set, (
        f"Mismatch in files for folder {folder_name}:\n"
        f"Expected: {expected_files_set}\n"
        f"Found: {actual_files}"
    )

def check_no_extra_folders(expected_folders):
    """Check if there are no unexpected folders in the root directory."""
    root_folder = "Movie Mixup"
    actual_folders = set(f for f in os.listdir(root_folder) if f != ".DS_Store")
    assert actual_folders == expected_folders, (
        f"Mismatch in folders:\nExpected: {expected_folders}\nFound: {actual_folders}"
    )

def test_monday_folder():
    check_folder_exists("Monday")
    check_files_in_folder("Monday", ["Shrek.png"])

def test_tuesday_folder():
    check_folder_exists("Tuesday")
    check_files_in_folder("Tuesday", ["Barbie.jpg"])

def test_wednesday_folder():
    check_folder_exists("Wednesday")
    check_files_in_folder("Wednesday", ["Avengers.png"])

def test_thursday_folder():
    check_folder_exists("Thursday")
    check_files_in_folder("Thursday", ["Shrek.png"])

def test_friday_folder():
    check_folder_exists("Friday")
    check_files_in_folder("Friday", ["Jaws.png"])

def test_no_extra_folders():
    correct_structure = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"}
    check_no_extra_folders(correct_structure)

