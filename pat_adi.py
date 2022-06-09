import time
def main():
    start_time = time.time()
    # print("Start Time of Main --- %s seconds ---" % (start_time))
    num1 = 5
    num2 = 6
     
    # Add two numbers
    sum = float(num1) + float(num2)
     
    # Display the sum
    #return('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
    end_time = time.time()
    return("Read the file from S3 at", end_time , "and time elapsed is  --> ", (end_time - start_time) )
