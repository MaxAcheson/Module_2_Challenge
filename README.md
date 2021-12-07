# Loan Qualifier Tool for Module 2 Challenge

This loan application program is designed to give people a customized list of bank loans based on various points of information regarding their financial standing and history. 
Many people find it difficult to interact with a bank teller in order to figure out what loans are available for them. This program seeks to automate the whole process by filtering data from a spreadsheet full of daily loan rates from various banks.

## Technologies

This program was written in VS Code and executed in GitBash terminal on a PC running windows 10. The program should run smoothly on any operating system in any CLI terminal as long as the following minimum requirements are met:

python 3.7.10

questionary 0.2.5

fire 1.15.0

There is only one version of the program uploaded, so there should not be version errors. 

## Installation Guide

To install the updated version of fire, please enter the following in your terminal:

```pip install fire```

To install the updated version of questionary, please enter the following in your terminal:

```pip install questionary```

## Usage

To use this program in a CLI, clients must first enter dev mode in order to run the program. This can be achieved by using this code:

```conda activate dev```

Next, once in dev mode, a user must navigate to the file path where the program exists on their computer, and then run the program using this code:

```python app.py```

Once the program is running, the user must select the file path in which they would like to use to load the compelte list of bank loan options. This can be done by typing in the completed file path including the file name. The code will be similar to this, just with a different path:

```C:\Users\maxac\Documents\School\Challenges\Module_2_Challenge\Module_2_Challenge\Starter_Code\loan_qualifier_app\data\daily_rate_sheet.csv```

Next, the user will be asked to input several values in order to get a new filtered list of bank loans that fit their individual needs. They should use authentic values to increase their odds of finding loans that suit their needs. Please use integers only, and submit each answer by pressing enter. 

This animation should help:


![Watch this for help](https://media.giphy.com/media/kf7QuXtWyNhovAggtf/giphy.gif)

Once data is entered, the user will be told how many loans they are eligible for. If they are eligible for at least one loan, they will be prompted to save the list of loans as a csv file. The user can use y or n to select either yes or no, respectively. 

If the user selects to have the file saved to their computer, they will then be asked to provide the file path where they would like the file to be saved. Make sure this file path comtains the desired file name at the end, including the .csv file format.

This animation will show you what a path complete with a csv file name should look like:


![Watch this for help](https://media.giphy.com/media/DdudVObhV7Mma6FSby/giphy.gif)

Once the file is saved to the user's computer, they are free to consult the data to make their decision on which loan is right for them!

## Contributors

Max Acheson

maxacheson@gmail.com

[LinkedIn](https://www.linkedin.com/in/max-acheson-75093a19a/)

## Licenses

MIT License

Copyright (c) [2021] [Max Acheson]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

