# AWS cp and rm prototype working

## CLI Prerequisites

1) Python 2 or 3 installed
2) boto3 library installed, can be done with pip or conda

## How to Test Prototype
1) clone this repo
2) `cd cloud-agnostic/prototype/cli`
3) run `AWS_ACCESS_KEY_ID=<access_key_id> AWS_SECRET_ACCESS_KEY=<secret_access_key> python positional_parser.py storage cp natee.txt cloud://cloud-agnostic-testing/natee.txt`
4) log into s3, see that natee.txt got uploaded
5) run `AWS_ACCESS_KEY_ID=<access_key_id> AWS_SECRET_ACCESS_KEY=<secret_access_key> python positional_parser.py storage rm cloud://cloud-agnostic-testing/natee.txt`
6) look back at s3 and see that natee.txt got deleted

Note: this code has been tested on Linux with Python 2 and 3

