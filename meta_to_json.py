import pandas as pd
import os
import glob
import json

#画像生成時にできたフォルダに移動
dir = '/Users/woo/generative-art-nft-allaugh/output/edition_7777'#自分のフォルダパスに変更(woo,edition_7777の部分を変更するパターンが多いです)
os.chdir(dir)

#生成されたmedadata.csvを読み込み
metadata = pd.read_csv('metadata.csv')

#↓変更必要
name = 'testname'#自分のNFTに表示する名前（ここの名前 #1のような感じで表示される）
description = 'testdis'#NFTの説明（各自更新）
ipfs = 'QmR3BJU3kmF9xwVK1L4inzRRSJsUmNA6NWMPTtRbqZVYWq'#pinataで画像をアップロードしたフォルダのCIDアドレスを各自記載
#↑変更必要

#読み込んだmedadata.csvから１行ずつjsonで出力
for index, row in metadata.iterrows():
    tmp = {
    "name": name+" #" + str(index+1),
    "description":description,
    "image":"ipfs://"+ipfs+"/"+str(index+1)+".png",
    "attributes":[
        
        #↓変更必要  NFTに表示したい属性を下記に記載
        {
            "trait_type":"TYPE",
            "value":row['ear']
        },
        {
            "trait_type":"OUTER",
            "value":row['cloth']
        },
        {
            "trait_type":"TOPS",
            "value":row['shirt']
        },
        {
            "trait_type":"PANTS",
            "value":row['pants']
        },
        {
            "trait_type":"EYE",
            "value":row['eye']
        },
        {
            "trait_type":"NECK",
            "value":row['neck']
        },
        {
            "trait_type":"ITEM",
            "value":row['head_accessory']
        },
        #↑変更必要
        
    ]
    }
    
    #メタデータ用のフォルダを作成しJSONファイルを出力
    os.makedirs("metadatas", exist_ok=True)
    with open('metadatas/'+str(index+1)+'.json', 'w') as f:
        json.dump(tmp, f, ensure_ascii=False, indent=2)
