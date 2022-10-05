## Usage
Move file from one prefix to another, if file is not present in destination prefix, if present then append timestamp to file name before copying to destination prefix.

## Args:
```
bucket_name (str): Name of the bucket
source_prefix (str): Full path of the source prefix
destination_prefix (str): Full path of the destination prefix
file_name (str): File name
```

## Example:
If you want to move file 
from: `s3://bucket-name/source1/source2/file.txt`
to:   `s3://bucket-name/destination1/destination2/file.txt`

then you need to pass following arguments:
```
bucket_name = bucket-name
source_prefix = source1/source2/
destination_prefix = destination1/destination2/
file_name = file.txt
```