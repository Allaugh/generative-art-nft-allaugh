# Generative NFT Art

## Introduction

The `generative-art-nft-allaugh` repository is a library for creating generative art. It was developed for the purpose of creating NFT avatar & collectible projects. This library was used to generate the artwork for the [Allaugh](https://allaughs.com/) project.

## Features

### Generate over a million distinct images with less than 60 traits
The library allows you to generate images every distinct possible combination of your traits. For context, if you had trait art for a project like [Bored Apes](https://boredapeyachtclub.com/#/home), the library could generate upwards of 1.2 billion distinct apes.

### Add rarity weights
The library also allows you to configure the image generation process in such a way that you have complete control over how rare each and every trait is.

### Generate compliant JSON metadata for your NFTs
There is now an added functionality to generate JSON metadata for your NFTs that are in compliance with OpenSea metadata requirements (and by extension, the general NFT metadata standard).

### Fuzzy friendly
You can use this library even if you do not know how to program (in Python or otherwise). Do check out the [Tutorial](https://medium.com/scrappy-squirrels/tutorial-create-generative-nft-art-with-rarities-8ee6ce843133) for more details on how to use (non-technical) and extend (technical) the library.

## Installation

**Clone this repository**

```git clone https://github.com/Allaugh/generative-art-nft-allaugh.git```

**Install required packages**

```pip install Pillow pandas progressbar2 os glob json```

Upload your input assets in the `assets` folder, fill up the `config.py` file, and then run `python nft.py`.
Upload NFT images on pinata. fill up the `meta_to_json.py` file, and then run `python meta_to_json.py`.
Upload NFT metadatas(.json) on pinata.

## Usage

This project is forked from Scrappy Squirrels. Scrappy Squirrels have good Document. Check it out [here](https://medium.com/scrappy-squirrels/tutorial-create-generative-nft-art-with-rarities-8ee6ce843133)

The following features have been added to this program.
- The output metadata is now compatible with [HashLips](https://github.com/HashLips/hashlips_nft_contract) and [ThirdWeb](https://thirdweb.com/).
- Added support for one-to-one parts, such as front hair and back hair.
- Added DockerFile, .gitignore, etc.

## About Allaugh Project

<img src='Creamon.png' height="500" width="500" />

This library was created as part of the Allaugh DAO project "Sprimal".

Sprimal is a collection of 7,777 randomly generated NFTs. Allaugh DAO is a charity project that makes all of the world laugh with NFT.

The community is Built by Allaugh. Allaugh is charity DAO community.