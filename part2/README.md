# 2nd Tutorial Session
    
## Description:
```
For Part 2 you will complete the code in collatzSteps so that when you type the following url(see part2.jpg) into your browser. Your flask app will calculate the collatz value for the integer that you specify.

See the following documentation on how to use the Flask request object.

https://flask.palletsprojects.com/en/1.1.x/api/?highlight=request#flask.request
   
```

## How to run this app:
```
Option 1:

1. Starting your web application -> From the menu on the top click 'Window' and then click 'New Terminal'
2. Go the directory where the collatzSteps.py file is
3. Type: python collatzSteps.py

Option 2: Click the green run button.
```    
    
## Instructions:
```
1. Your task is to compelte the code in collatzSteps.py buy parsing the integer from the url and setting the variable "n" with this value. Use the request object to get the number passed in via the url. Make sure to validate that the input is an integer or throw an error.
2. Find the public ip of your instance by using the following command: 

dig +short myip.opendns.com @resolver1.opendns.com


4. You can see your webpage at the following example url (replace this ip with the one you got from step 3) http://3.231.155.231:5000/ 
```