import argparse
import maya.standalone

maya.standalone.initialize()

import maya.cmds

print("creating a cube...")
maya.cmds.polyCube()
print(maya.cmds.ls(geometry=True))

parser = argparse.ArgumentParser(description = '')