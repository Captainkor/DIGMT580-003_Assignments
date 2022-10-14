import json
import os
import maya.standalone
import maya.cmds

save_dir_format = "{project}/assets/{asset}/{task}"
save_file_format = "{asset}.{task}.{artist}.{version}.{ext}"


def getAssetMetadata():
    """
    Read the asset metadata file
    """

    asset_dir = getAssetDirectory()
    asset_metadata_file = os.path.join(asset_dir, "metadata.json")
    metadata_file = open(asset_metadata_file)
    return json.load(metadata_file)


def getSaveFile(extension, version=None):
    """
    :param extension: extension of the file requested
    :param version: version of the asset requested, return the latest version if none specified
    :return: A save file correctly formatted based on the environment
    """
    metaFile = getAssetMetadata()
    latestVersion = metaFile["version"]

    asset_info = {
        "project": os.getenv('project'),
        "asset": os.getenv('asset'),
        "task": os.getenv('task'),
        "artist": os.getenv('USER'), # usually built-in
        "version": latestVersion if version is None else version,
        "ext": extension
    }

    dir_path = save_dir_format.format(**asset_info)
    filename = save_file_format.format(**asset_info)

    return os.path.join(dir_path, filename)


def getAssetDirectory():
    """
    Gets the asset directory for the current asset
    """

    asset_info = {
        "project": os.getenv('project'),
        "asset": os.getenv('asset'),
        "task": os.getenv('task'),
        "artist": os.getenv('USER'), # usually built-in
    }
    return save_dir_format.format(**asset_info)



def setAssetStatus(status):
    """
    Set the asset status
    """

    metadata = getAssetMetadata()
    metadata['status'] = status

    asset_dir = getAssetDirectory()
    asset_metadata_file = os.path.join(asset_dir, "metadata.json")
    metadata_file = open(asset_metadata_file, 'w')

    json.dump(metadata, metadata_file)

def setAssetVersion(version):
    """
    Set the asset status
    """

    metadata = getAssetMetadata()
    metadata['version'] = version

    asset_dir = getAssetDirectory()
    asset_metadata_file = os.path.join(asset_dir, "metadata.json")
    metadata_file = open(asset_metadata_file, 'w')

    json.dump(metadata, metadata_file)

def appendVersion(fileName):
    """
    Append the version of saved file and save to a new file with new version
    :param fileName: Old File Name
    :return: None
    """
    asset, task, artist, version, ext = fileName.split(".")

    version += 1
    newFileName = save_file_format.format(asset, task, artist, version, ext)

    maya.cmds.file(rename="{}.ma".format(newFileName))
    maya.cmds.file(save=True, type="mayaAscii")

    setAssetVersion(version)