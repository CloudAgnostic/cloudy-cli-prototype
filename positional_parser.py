import argparse

from aws import aws
from gcloud import gcloud

providers = []
# TODO: set up default provider and provider parsing
providers.append(aws.Aws())
providers.append(gcloud.GCloud())

command_parser = argparse.ArgumentParser()
command_parser.add_argument('command')
command_parser.add_argument('-c', '--credentials')
command_parser.add_argument('-p', '--provider')
subcommand_parsers = command_parser.add_subparsers()

storage_command = 'storage'
cp_parser = subcommand_parsers.add_parser('cp')
cp_parser.set_defaults(command=storage_command, subcommand='cp')
cp_parser.add_argument('-r', '--recursively')
cp_parser.add_argument('src_path')
cp_parser.add_argument('dest_path')

rm_parser = subcommand_parsers.add_parser('rm')
rm_parser.set_defaults(command=storage_command, subcommand='rm')
rm_parser.add_argument('path')

args = command_parser.parse_args()

for provider in providers:
    command = getattr(provider, args.command)
    subcommand = getattr(command, args.subcommand)
    subcommand(command(), args)
