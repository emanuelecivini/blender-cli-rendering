# Imports
from lib2to3.pgen2 import token
from os import listdir, mkdir
from os.path import isdir
import json

# Constants

BUILD_DIR='Blend_My_NFTs Output/Generated NFT Batches'
TARGET_DIR='ElrondMetadata'
COLLECTION_NAME='BlendMyNFT'
IPFS_IMAGE_URL='https://gateway.ipfs.io/ipfs/Qimage.../'
IPFS_ANIMATION_URL='https://gateway.ipfs.io/ipfs/Qanimation.../'
IMAGE_FILE_FORMAT='png'
ANIMATION_FILE_FORMAT='mp4'

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
