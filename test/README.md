# Welcome to the PolyFlow test suite 

## Getting started
The PolyFlow test suite utilizes Pytest which makes testing very easy.

1. Install Pytest to your PolyFlow or custom venv:

`pip install -U pytest`

2. Use the 'pytest' command from the 'test' directory to run the test suite:

`pytest test_flow`

This will run the entire test suite using pytest. To pick a single test just 
use the -k flag and specify the test:

`pytest test_flow/preprocessing -k test_load_data`



