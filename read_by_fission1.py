import sys
import boto3
import json
import time

def main():
	# start_time = time.time()
	# print("Start Time of Main --- %s seconds ---" % (start_time))
	session = boto3.Session(
			    aws_access_key_id='AKIAXBNIAY3OSGPM5GHY',
			    aws_secret_access_key='sP4JthlrxMA1ntR4EwQfEJhNuHZ5xyZh/0j61onQ',
			    region_name='us-east-1')
			    
	s3 = session.resource('s3')

	# get a handle on the bucket that holds your file
	bucket = s3.Bucket('test-case-1') # example: energy_market_procesing

	# get a handle on the object you want (i.e. your file)
	obj = bucket.Object(key='2.json') # example: market/zone1/data.csv

	# get the object
	response = obj.get()

	# read the contents of the file
	lines = response['Body'].read().decode()
	data = json.loads(lines)
	transactions = data['users']
	#transactions = data['dataset']['fields']
	#print(str(len(transactions)))
	# end_time = time.time()
	# print("Read the file from S3 at", end_time , "and time elapsed is  --> ", (end_time - start_time) )
	# return str(len(transactions))
	return "\n"
