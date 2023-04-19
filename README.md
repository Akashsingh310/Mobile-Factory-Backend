# Mobile-Factory-Backend

This repository contains a simple Flask app that provides an API for processing orders.

Prerequisites to be installed - Python3

## Installation

1. First fork this repo and then clone this repository by using the command `git clone` and install the required dependencies using `pip`.

2. Open main.py and run `python main.py`.

3. Now open new termial and paste `Invoke-WebRequest -Method POST -ContentType "application/json" -Body '{"components": ["I","A","D","F","K"]}' -Uri http://127.0.0.1:5000/orders` this command you give you output

## Output

![output](https://github.com/Akashsingh310/Mobile-Factory-Backend/blob/main/1.png)


## Testing

4 different test cases have been provided in test.py where each case checks if the total sum of a combination equals the expected data already given in the case. If so, it is declared to pass, else it fails.
For running this you can use the command `python test.py`.
`

