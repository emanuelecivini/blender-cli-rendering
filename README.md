# Blender Cli Rendering Automation

These scripts automate the rendering procedure for a NFT collection made with Blender and Blend My NFTs.

## Dependencies
In order to use this suite you must have Python3 (tested with Python3.9.6) installed. 
On Ubuntu `sudo apt install python3`

You will also have to install Blender
On Ubuntu `sudo apt install blender`

## Setup
Before generating the NFTs when must setup the environment. These are the steps needed:
1. `python3 setup.py`
2. Download the config.cfg BlendMyNFTs file from Blender UI in the root of the project
3. Open render.py and edit the variables on top according to the requirements and environment

## Rendering
To start the rendering just run `python3 render.py`. It will take a while.

## Convert metadata
Before doing this keep in mind that you should have already uploaded both the images and animations on IPFS through Pinata.
If this is the case, edit the variables in metadata.py by adding the links to these two.
After that, if you want to convert the generated metadata (ERC721 format) into the Elrond format, run `python3 metadata.py`.