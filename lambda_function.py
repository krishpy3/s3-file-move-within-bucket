import boto3
from datetime import datetime


def lambda_handler(event, context):
    """
    Move file from one prefix to another, 
    if file is not present in destination prefix, 
    if present then append timestamp to file name 
    before copying to destination prefix.

    Args:
        bucket_name (str): Name of the bucket
        source_prefix (str): Full path of the source prefix
        destination_prefix (str): Full path of the destination prefix
        file_name (str): File name
    
    Example:
        if you want to move file 
        from: s3://bucket-name/source1/source2/file.txt 
        to:   s3://bucket-name/destination1/destination2/file.txt

        then bucket_name = bucket-name
        source_prefix = source1/source2/
        destination_prefix = destination1/destination2/
        file_name = file.txt
    """

    s3 = boto3.client('s3')
    bucket = event['bucket_name']
    source_prefix = event['source_prefix']
    destination_prefix = event['destination_prefix']
    file_name = event['file_name']
    source_file = source_prefix + file_name
    destination_file = destination_prefix + file_name
    source = {'Bucket': bucket, 'Key': source_file}
    try:
        s3.head_object(Bucket=bucket, Key=destination_file)
        print("File already exists in destination prefix")
        date = datetime.now().strftime("%m%d%Y%H%M")
        destination_file = f"{destination_prefix}{date}_{file_name}"
        s3.copy_object(Bucket=bucket, Key=destination_file, CopySource=source)
        s3.delete_object(Bucket=bucket, Key=source_file)
        print("File moved to destination prefix with timestamp")
    except:
        print("File does not exist in destination prefix")
        s3.copy_object(Bucket=bucket, Key=destination_file, CopySource=source)
        s3.delete_object(Bucket=bucket, Key=source_file)
        print("File moved to destination prefix")
    
    return {
        'statusCode': 200,
        'body': f'File:{file_name} moved to {destination_prefix}'
    }


print(lambda_handler({
    "file_name": "hi.txt",
    "destination_prefix": "folder1/sub1/ssub1/",
    "source_prefix" : "folder2/sub2/ssub2/",
    "bucket_name": "boto3-test-krishh"
}, {}))