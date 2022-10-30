import argparse
import csv
import datetime
import json
import os
from zipfile import ZipFile

"""
Create and setup argument parser
"""

parser = argparse.ArgumentParser(description='Rename and archive frames in directory')
parser.add_argument('--path', type=str, help="path to the frames")
parser.add_argument('--zip', type=bool, help="whether compress frames to a zip file")
parser.add_argument('--thumbnail', type=str, help="File Name to save to")

args = parser.parse_args()

frames = []
path = args.path
dir_list = os.listdir(path)
asset_info = {"project": os.getenv('project'),
              "asset": os.getenv('asset'),
              "task": os.getenv('task'),
              "artist": os.getenv('USER'),  # usually built-in
              }

print("Files and directories in '", path, "' :")

# prints all files
print(dir_list)


def getNamingConvention():
    """
    get naming convention from json file
    :return: naming convention for frames
    """
    convention_file_path = os.path.join(path, "namingConvention.json")
    convention_file = open(convention_file_path)

    return json.load(convention_file)['naming_convention']


naming_convention = getNamingConvention()

# rename files to naming convention
n = 0  # frame counter
for file in dir_list:
    asset_info["frame_number"] = n
    file_name = naming_convention.format(**asset_info)
    os.rename(file, file_name)
    n += 1

dir_list = os.listdir(path)   # Refresh dir_list

# Create zip archive if necessary
if args.zip:
    with ZipFile('archive.zip', 'w') as newzip:
        for file in dir_list:
            newzip.write(file)

# Create CSV file for thumbnails, file names and date
with open('archive.csv','wb') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(args.thumbnail)
    x = datetime.datetime.now()
    for file in dir_list:
        filewriter.writerow(file, x.strftime("%x"))
