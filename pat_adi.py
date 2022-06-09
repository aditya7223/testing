import sys
import boto3
import json
import time
def main():
    num1 = 5
    num2 = 6
 
    # Add two numbers
    sum = float(num1) + float(num2)
 
    # Display the sum
    return('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
