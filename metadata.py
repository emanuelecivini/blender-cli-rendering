# Imports
from distutils.command.config import config
from os import listdir, mkdir
from os.path import isdir
from config import *
import json

# Get all batches
batches = []
for entry in listdir(BUILD_DIR):
    path = BUILD_DIR + '/' + entry
    if isdir(path):
        batches.append(path)

if not isdir(TARGET_DIR):
    mkdir(TARGET_DIR)

# Convert ERC721 metadata to Erlond format and add DNA
for batch in batches:
    metadataDir = batch + '/Erc721_metadata'
    files = sorted(listdir(metadataDir))
    
    for filename in files:
        metadataFilePath = metadataDir + '/' + filename 
        with open(metadataFilePath, "r") as metadataFile:
            print("Converting metadata for token", filename)
            erc721Metadata = json.load(metadataFile)
            
            # get dna
            dnaFileName = batch + '/BMNFT_data/Data_' + filename
            with open(dnaFileName, "r") as dnaFile:
                dnaData = json.load(dnaFile)
                possibleDnas = list(dnaData["nft_dna"].keys()) # should always be one
                dna = possibleDnas[0]

            tokenId = filename.replace(COLLECTION_NAME + "_", '')
            tokenId = tokenId.replace(".json", '')

            metadata = {
                "id": int(tokenId),
                "animation": IPFS_ANIMATION_URL + tokenId + '.' + ANIMATION_FILE_FORMAT,
                "pfp": IPFS_IMAGE_URL + tokenId + '.' + IMAGE_FILE_FORMAT,
                "dna": dna,
                "description": erc721Metadata["description"],
                "attributes": erc721Metadata["attributes"]
            }

            # TODO: Upload image and animation to Pinata
            targetFileName = TARGET_DIR + '/' + filename.replace(COLLECTION_NAME + "_", '')
            targetFile = open(targetFileName, "w+")
            json.dump(metadata, targetFile, indent=2)
            targetFile.close()
