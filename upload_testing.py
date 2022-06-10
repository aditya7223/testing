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
	obj=bucket.Object(key='splitted_file.txt')
	response=obj.get()
	content = response['Body'].read().decode('utf-8')
	return content