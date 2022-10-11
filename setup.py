# imports
from os import system
from sys import exit

# configurations
BLENDER_NAME='Blender'
BLEND_FILE_PATH='example.blend'
BLEND_MY_NFTS_REPO="https://github.com/torrinworx/Blend_My_NFTs.git"

###############################################################################
# git installation
"""
cmd = "apt install git zip -y"
if system(cmd) != 0:
    print("Uanble to install git and zip via apt")
    exit(1)
"""

###############################################################################
# Blender installation
"""
cmd = "apt install blender -y"
if system(cmd) != 0:
    print("Unable to install blender via apt")
    exit(1)
"""

###############################################################################
# Blend My NFTs download
cmd = "git clone " + BLEND_MY_NFTS_REPO
if system(cmd) != 0:
    print("Uanble to clone BlendMyNFTs")
    exit(1)

###############################################################################
# Blend My NFTs zip
"""
cmd = "zip -r Blend_My_NFTs.zip Blend_My_NFTs"
if system(cmd) != 0:
    print("Uanble to zip BlendMyNFTs")
    exit(1)
"""

###############################################################################
# Blend My NFTs installation
# TODO: ref https://blender.stackexchange.com/questions/73759/install-addons-in-headless-blender
