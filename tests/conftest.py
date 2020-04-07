import sys
import os


# Add project root dir to sys path
file_dir = os.path.dirname(os.path.realpath(__file__))
project_dir = os.path.abspath(os.path.join(file_dir, ".."))
sys.path.insert(0, project_dir)
