"""
Create an empty group in a Maya scene with that asset name
"""

import maya.standalone
import maya.cmds
import argparse


# Create and set up arguments
parser = argparse.ArgumentParser(description='Create an empty group in a Maya scene with that asset name')
parser.add_argument('--name', type=str, help="Asset Name")

args = parser.parse_args()

# Initiate Maya
maya.standalone.initialize()

# Create Group
maya.cmds.group(em=True, n=args.name)

# Save to File
maya.cmds.file(rename="{}.ma".format(args.name))
maya.cmds.file(save=True, type="mayaAscii")


