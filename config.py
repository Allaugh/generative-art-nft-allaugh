# This file MUST be configured in order for the code to run properly

# Make sure you put all your input images into an 'assets' folder.
# Each layer (or category) of images must be put in a folder of its own.

# CONFIG is an array of objects where each object represents a layer
# THESE LAYERS MUST BE ORDERED.

# Each layer needs to specify the following
# 1. id: A number representing a particular layer
# 2. name: The name of the layer. Does not necessarily have to be the same as the directory name containing the layer images.
# 3. directory: The folder inside assets that contain traits for the particular layer
# 4. required: If the particular layer is required (True) or optional (False). The first layer must always be set to true.
# 5. rarity_weights: Denotes the rarity distribution of traits. It can take on three types of values.
#       - None: This makes all the traits defined in the layer equally rare (or common)
#       - "random": Assigns rarity weights at random.
#       - array: An array of numbers where each number represents a weight.
#                If required is True, this array must be equal to the number of images in the layer directory. The first number is  the weight of the first image (in alphabetical order) and so on...
#                If required is False, this array must be equal to one plus the number of images in the layer directory. The first number is the weight of having no image at all for this layer. The second number is the weight of the first image and so on...

# Be sure to check out the tutorial in the README for more details.

METADATA = {
    #thirdwebを使う場合はこちらを変更
    "name": "Sprimal",
    "description": "Sprimal is a Generative Charity NFT Collection. 20% of sales will be donated to pet protection activities.Make all of the earth laugh.",
    "external_url": "https://allaughs.com/",
    "background_color": "FFFFFF",
    #    "youtube_url": ""
}

CONFIG = [
    #ここは変更必須
    {
        "id": 1,
        "name": "background",
        "directory": "background",
        "required": True,
        "rarity_weights": None,
    },
    {
        "id": 2,
        "name": "body_back",
        "directory": "body_back",
        "required": True,
        "rarity_weights": [2,2,2,2,2,2,2,2,100,2,2,2,2,2],
    },
    {
        "id": 3,
        "name": "body",
        "directory": "body",
        "required": True,
        "rarity_weights": None,
    },
    {
        "id": 4,
        "name": "pants",
        "directory": "pants",
        "required": True,
        "rarity_weights": [10,10,10,10,10,100,10,10,10,10,10,10,10,10,10,10],
    },
    {
        "id": 5,
        "name": "shirt",
        "directory": "shirt",
        "required": True,
        "rarity_weights": None,
    },
    {
        "id": 6,
        "name": "pants_sub",
        "directory": "pants_sub",
        "required": True,
        "rarity_weights": None,
        "link": {
            "overall-beige.png" : "overall-beige2.png",
            "overall-black.png" : "overall-black2.png",
            "overall-blue.png" : "overall-blue2.png",
            "overall-green.png" : "overall-green2.png",
            "overall-pink.png" : "overall-pink2.png",
            "jeans-beige.png" : "none_pantsub.png",
            "jeans-black.png" : "none_pantsub.png",
            "jeans-pink.png" : "none_pantsub.png",
            "jeans.png" : "none_pantsub.png",
            "nappy.png" : "none_pantsub.png",
            "none.png" : "none_pantsub.png",
            "shorts-black.png" : "none_pantsub.png",
            "shorts-green.png" : "none_pantsub.png",
            "shorts-red.png" : "none_pantsub.png",
            "tights-gray.png" : "none_pantsub.png",
            "tights-pink.png" : "none_pantsub.png",
        },
    },
    {
        "id": 7,
        "name": "cloth",
        "directory": "cloth",
        "required": True,
        "rarity_weights": None,
        "rarity_weights": [5,5,5,5,5,100,5,5,5],
    },
    {
        "id": 8,
        "name": "neck",
        "directory": "neck",
        "required": True,
        "rarity_weights": [
            1,  # Gold
            100,  # Nomal
            2,  # Silver
        ],
    },
    {
        "id": 9,
        "name": "body_accessory",
        "directory": "body_accessory",
        "required": True,
        "rarity_weights": [5,5,5,5,100,2],
    },
    {
        "id": 10,
        "name": "head_back",
        "directory": "head_back",
        "required": True,
        "rarity_weights": [100,100,100,100,100,100,100,100,100,100,100,100,100],
    },
    {
        "id": 11,
        "name": "head",
        "directory": "head",
        "required": True,
        "rarity_weights": None,
    },
    {
        "id": 12,
        "name": "head_pattern",
        "directory": "head_pattern",
        "required": True,
        "rarity_weights": None,
        # "rarity_weights": [10,10,100,10,10],
        "link": {
            "none-headback01.png" : "none-pattern.png",
            "none-headback02.png" : "none-pattern.png",
            "none-headback03.png" : "none-pattern.png",
            "none-headback04.png" : "none-pattern.png",
            "none-headback05.png" : "none-pattern.png",
            "none-headback06.png" : "none-pattern.png",
            "none-headback07.png" : "none-pattern.png",
            "none-headback08.png" : "none-pattern.png",
            "none-headback09.png" : "giraffe-pattern.png",
            "lion-back.png" : "none-pattern.png",
            "none-headback10.png" : "panda-pattern.png",
            "none-headback11.png" : "panda-pattern.png",
            "none-headback12.png" : "tiger-pattern.png",
        },
    },
    {
        "id": 13,
        "name": "eye",
        "directory": "eye",
        "required": True,
        "rarity_weights": None,
    },
    {
        "id": 14,
        "name": "head_pattern2",
        "directory": "head_pattern2",
        "required": True,
        "rarity_weights": [2,100],

    },
    {
        "id": 15,
        "name": "subitem",
        "directory": "subitem",
        "required": True,
        "rarity_weights": [2,2,2,2,2,2,100,2,2,2,2,2],
    },
    {
        "id": 16,
        "name": "head_pattern3",
        "directory": "head_pattern3",
        "required": True,
        "rarity_weights": None,
        # "rarity_weights": [2,2,2,2,2,2,1000,2,2,2,2,2],
        "link": {
            "big-right.png" : "noneeye1.png",
            "big.png" : "noneeye2.png",
            "confusion.png" : "noneeye3.png",
            "cute-right.png" : "noneeye4.png",
            "cute-wink.png" : "noneeye5.png",
            "disgusted.png" : "noneeye6.png",
            "dollar.png" : "noneeye7.png",
            "down.png" : "noneeye8.png",
            "droopy.png" : "noneeye9.png",
            "dull.png" : "noneeye10.png",
            "eyelashes.png" : "noneeye11.png",
            "glare.png" : "noneeye12.png",
            "left.png" : "noneeye13.png",
            "nobi.png" : "noneeye14.png",
            "right.png" : "noneeye15.png",
            "sleepy.png" : "noneeye16.png",
            "smile.png" : "noneeye17.png",
            "smirk.png" : "noneeye18.png",
            "square.png" : "noneeye19.png",
            "strong.png" : "noneeye20.png",
            "up.png" : "noneeye21.png",
            "white.png" : "noneeye22.png",
            "wink.png" : "noneeye23.png",
            "zombie.png" : "zombie2.png",


            
        },
    },
    {
        "id": 17,
        "name": "ear",
        "directory": "ear",
        "required": True,
        "rarity_weights": None,
        "link": {
            "none-headback01.png" : "bear.png",
            "none-headback02.png" : "buck.png",
            "none-headback03.png" : "cat.png",
            "none-headback04.png" : "doe.png",
            "none-headback05.png" : "dog.png",
            "none-headback06.png" : "doggo.png",
            "none-headback07.png" : "doggy.png",
            "none-headback08.png" : "fox.png",
            "none-headback09.png" : "giraffe.png",
            "lion-back.png" : "lion.png",
            "none-headback10.png" : "panda.png",
            "none-headback11.png" : "raccoon-dog.png",
            "none-headback12.png" : "tiger.png",
        },
    },
    {
        "id": 18,
        "name": "head_accessory",
        "directory": "head_accessory",
        "required": True,
        "rarity_weights": None,
        "link": {
            "angel-wing.png" : "angel.png",
            "none-bodyback01.png" : "cap-green.png",
            "none-bodyback02.png" : "cap-red.png",
            "none-bodyback03.png" : "cap-yellow.png",
            "none-bodyback04.png" : "eyepatch.png",
            "none-bodyback05.png" : "foxmask-blue.png",
            "none-bodyback06.png" : "foxmask-red.png",
            "none-bodyback07.png" : "king.png",
            "none-bodyback08.png" : "none.png",
            "none-bodyback09.png" : "poo.png",
            "none-bodyback10.png" : "queen.png",
            "none-bodyback11.png" : "sunglass-black.png",
            "none-bodyback12.png" : "sunglass-blue.png",
            "none-bodyback13.png" : "tengu.png",
        },
    },
    {
        "id": 19,
        "name": "subitem2",
        "directory": "subitem2",
        "required": True,
        "rarity_weights": None,
        "link": {
            "drool.png" : "none-sub.png",
            "mask-black.png" : "none-sub1.png",
            "mask-blue.png" : "none-sub2.png",
            "mask-red.png" : "none-sub3.png",
            "mask-white.png" : "none-sub4.png",
            "mask-yellow.png" : "none-sub5.png",
            "none-mask.png" : "none-sub6.png",
            "pipe.png" : "pipe2.png",
            "ring.png" : "none-sub7.png",
            "snot-double.png" : "none-sub8.png",
            "snot-long.png" : "none-sub9.png",
            "snot.png" : "none-sub10.png",
        },
    },
]
