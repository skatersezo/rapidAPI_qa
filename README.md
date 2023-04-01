# Titles API testing

Python testing for one of Rapid API's free usage endpoints.
An excel document is included with all possible test cases thought for the endpoint GET `titles/` and GET `titles/{id}`.

## Prerequisites
* Python3 (this project was developed with Python@3.9)

## Setup

1. Clone this repository to your local machine.
2. Create the virtual environment
``` bash
python -m venv env
```
3. Activate the virtual environment:
```bash
source env/bin/activate # For unix based systems
env\Scripts\activate.bat # For Windows
```
4. Install the dependencies:
```bash
python -m pip install -r requirements.txt
```

## Running the tests
To run the tests and generate a report with the test results, use the following command:
```bash
python -m pytest --html=report.html
```
You can choose any filename you like, as long as it ends with the `.html` extension.

## Manual testing
A `titles.http` file has been included for manual testing with the [REST Client plugin](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) for [Visual Studio Code](https://code.visualstudio.com/).