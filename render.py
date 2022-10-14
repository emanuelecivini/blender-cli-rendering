# imports
from distutils.command.upload import upload
from os import system, getenv, walk, path
from sys import exit
from config import *
import boto3

from dotenv import load_dotenv
load_dotenv() 

###############################################################################
# Upload files to AWS S3 
def upload_files(path):
    session = boto3.Session(
        aws_access_key_id=getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=getenv('AWS_ACCESS_SECRET_KEY'),
        region_name=getenv('REGION_NAME')
    )
    s3 = session.resource('s3')
    bucket = s3.Bucket(getenv('BUCKET_NAME'))
 
    for subdir, dirs, files in walk(path):
        for file in files:
            full_path = path.join(subdir, file)
            with open(full_path, 'rb') as data:
                bucket.put_object(Key=full_path[len(BUILD_DIR) + 1:], Body=data)

###############################################################################
# Create DNA
cmd = BLENDER_NAME + " -b " + BLEND_FILE_PATH +  " --python Blend_My_NFTs/__init__.py -- --config-file " + BLEND_MY_NFT_CONFIG + " --operation create-dna"
print(cmd)
if system(cmd) != 0:
    print("Unable to create dna")
    exit(1)

###############################################################################
# Generate NFT
for i in range(BATCH_NUMBER_START, BATCH_NUMBER_END + 1):
    cmd = BLENDER_NAME + " -b " + BLEND_FILE_PATH +  " --python Blend_My_NFTs/__init__.py -- --config-file " + BLEND_MY_NFT_CONFIG + " --operation generate-nfts --batch-number " + str(i)
    print(cmd)
    if system(cmd) != 0:
        print("Unable to generate NFTs")
        exit(1)

    # Upload folder to AWS S3
    taregtPath = BUILD_DIR + '/Batch' + str(i)
    upload_files(taregtPath)

print("Rendering completed")
