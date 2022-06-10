import sys
import boto3
import json
import time
def main():
	session = boto3.Session(
				aws_access_key_id="AKIAXBNIAY3O7IVJMMVH",
				aws_secret_access_key="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",
				region_name="ap-southeast-1")
	s3=session.resource('s3')
	bucket=s3.Bucket('bucket-to-fission')
	obj=bucket.Object(key='2.json')
	response=obj.get()
	# read the contents of the file
	lines = response['Body'].read().decode()
	data = json.loads(lines)
	transactions = data['users']
	#transactions = data['dataset']['fields']
	#print(str(len(transactions)))
	# end_time = time.time()
	# print("Read the file from S3 at", end_time , "and time elapsed is  --> ", (end_time - start_time) )
	return str(len(transactions))