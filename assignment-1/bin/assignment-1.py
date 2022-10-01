"""
Create specific number of spheres defined by user with random size and group them.
"""
import random

import maya.standalone
import maya.cmds
import argparse

"""
Create Argument Parser
"""

parser = argparse.ArgumentParser(description='Create number of spheres defined by user with random size and group then save')
parser.add_argument('--num_sphere', type=int, help="Number of cubes")
parser.add_argument('--name', type=str, help="File Name to save to")
parser.add_argument('--min', nargs='?', type=float, const=0.1, help="Minimum radius of the Sphere, Default 0.1")
parser.add_argument('--max', nargs='?', type=float, const=1, help="Maximum radius of the Sphere, Default 1")

args = parser.parse_args()

maya.standalone.initialize()

spheres = []        # Initiate the list for names of spheres

print("Creating {} sphere(s)...".format(args.num_sphere))
for i in range(args.num_sphere):
    print("Creating sphere Num.{}".format(i))
    spheres.append(maya.cmds.polySphere(r=random.uniform(args.min, args.max)))

for s in spheres:
    maya.cmds.group(s, n="Spheres")

maya.cmds.file(rename="{}.ma".format(args.name))
maya.cmds.file(save=True, type="mayaAscii")
