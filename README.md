# Loan Application Tool for the Module 2 Challenge

This loan application program is designed to give people a customized list of bank loans based on various points of information regarding their financial standing and history. 
Many people find it difficult to interact with a bank teller in order to figure out what loans are available for them. This program seeks to analyze the whole process by filtering data from a spreadsheet full of daily loan rates from various banks.

## Technologies

This program was written in VS Code and executed in GitBash terminal on a PC running windows 10. The program should run smoothly on any operating system in any terminal as long as the following minimum requirements are met:

python 3.7.10
questionary 0.2.5
fire 1.15.0

There is only one version of the program uploaded, so there should not be version errors. 

## Installation Guide

To install the updated version of fire, please enter the following in your terminal:
```pip install fire```

To install the updated version of questionary, please enter the following in your terminal:
```pip instal questionary```

## Usage

To use this program in a CLI, clients must first enter dev mode in order to run the program. This can be achieved by using this code:
```conda activate dev```

Next, once in dev mode, a user must navigate to the file path where the program exists on their computer, and then run the program using this code:
```python app.py```

Once the program is running, the user must select the file path in which they would like to use to load the compelte list of bank loan options. This can be done by typing in the completed file path including the file name. Your code will be similar to this, just with a different path:
```C:\Users\maxac\Documents\School\Challenges\Module_2_Challenge\Module_2_Challenge\Starter_Code\loan_qualifier_app\data\daily_rate_sheet.csv```

Next, the user will be asked to input several values in order to get a new filtered list of bank loans that fit their individual needs. Use authentic values to increase your odds of finding loans that suit your needs. Please use integers only, and submit each answer by pressing enter. This video should help:
![Watch this for help](https://media.giphy.com/media/kf7QuXtWyNhovAggtf/giphy.gif)

Once data is entered, the user will be told how many loans they are eligible for. If they are eligible for at least one loan, they will be prompted to save the list of loans as a csv file. The user can use y or no to select either yes or no, respectively. 