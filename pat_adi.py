import sys
import boto3
import json
import time
def main():
    start_time = time.time()
    #return("Start Time of Main --- %s seconds ---" % (start_time))
    num1 = 5
    num2 = 6
     
    # Add two numbers
    sum = float(num1) + float(num2)
     
    # Display the sum
    end_time = time.time()
    return ('The START IS {0} and END IS {1}'.format(start_time, end_time ))
    
    #return("Read the file from S3 at", end_time , "and time elapsed is  --> ", (end_time - start_time) )
