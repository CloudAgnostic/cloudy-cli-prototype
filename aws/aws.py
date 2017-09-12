

import boto3

# Make parent module available for import
import sys 
sys.path.append('..')

import provider

class Aws(provider.Provider):
    class storage(provider.Provider.storage):
        def cp(self, args):
            src_path = args.src_path
            dest_path = args.dest_path
            # TODO: Check if src/dest_path start with cloud:// or something, define convention
            s3_client = boto3.client('s3')
            bucket = dest_path[len('cloud://'):].split('/')[0]
            key = dest_path[len('cloud://') + len(bucket) + 1:]
            s3_client.upload_file(src_path, bucket, key)
            print('aws upload finished', args)
        def rm(self, args):
            path = args.path
            s3_client = boto3.client('s3')
            bucket = path[len('cloud://'):].split('/')[0]
            key = path[len('cloud://') + len(bucket) + 1:]
            s3_client.delete_object(Bucket=bucket, Key=key)
            print('aws delete finished', args)
