# imports
from os import system
from sys import exit

# configurations
BLENDER_NAME='Blender'
BLEND_FILE_PATH='example.blend'
BLEND_MY_NFT_CONFIG='config.cfg'
BATCH_NUMBER_START=5
BATCH_NUMBER_END=5

###############################################################################
# Create DNA
cmd=BLENDER_NAME + " -b " + BLEND_FILE_PATH +  " --python Blend_My_NFTs/__init__.py -- --config-file " + BLEND_MY_NFT_CONFIG + " --operation create-dna"
print(cmd)
if system(cmd) != 0:
    print("Unable to create dna")
    exit(1)

###############################################################################
# Generate NFT
"""
for i in range(BATCH_NUMBER_START, BATCH_NUMBER_END + 1):
    cmd=BLENDER_NAME + " -b " + BLEND_FILE_PATH +  " --python Blend_My_NFTs/__init__.py -- --config-file " + BLEND_MY_NFT_CONFIG + " --operation generate-nfts --batch-number " + str(i)
    print(cmd)
    if system(cmd) != 0:
        print("Unable to generate NFTs")
        exit(1)
"""

print("Rendering completed")
