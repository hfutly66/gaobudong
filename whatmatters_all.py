import json
import os
from tqdm import tqdm
import random

# python /vlm/yanluo/llava-glint/whatmatters_all.py

json_root = '/vlm/data/finetune_data/'
image_root = '/vlm/data/train_images'
json_path = os.path.join('/vlm/data/finetune_data/whatmatters_230M.json')

# 缺失数据集，gsd,wikisql,sqa,wtq,lnarratives, 论文里写的infovqa，我感觉是写错了，应该是infographic_vqa
# localized_narratives写成了 LNarratives
# 本来应该是mimic-it，他在hugging face上写成了mimic_cgd，在论文里写成了gsd。因为他的latex文档里是这篇文章，然后数量也对应都是70.9k
vqav2 = json.load(open(os.path.join(json_root,'vqav2.json'),'r'))
cocoqa = json.load(open(os.path.join(json_root,'cocoqa.json'),'r'))
visual7w = json.load(open(os.path.join(json_root,'visual7w.json'),'r'))
aokvqa = json.load(open(os.path.join(json_root,'aokvqa.json'),'r'))
tallyqa = json.load(open(os.path.join(json_root,'tallyqa.json'),'r'))
okvqa = json.load(open(os.path.join(json_root,'okvqa.json'),'r'))
hateful_memes = json.load(open(os.path.join(json_root,'hateful_memes.json'),'r'))
vqarad = json.load(open(os.path.join(json_root,'vqarad.json'),'r'))

localized_narratives = json.load(open(os.path.join(json_root,'localized_narratives.json'),'r'))
screen2words = json.load(open(os.path.join(json_root,'screen2words.json'),'r'))
vsr = json.load(open(os.path.join(json_root,'vsr.json'),'r'))

rendered_text = json.load(open(os.path.join(json_root,'rendered_text.json'),'r'))
docvqa = json.load(open(os.path.join(json_root,'docvqa.json'),'r'))
textcaps = json.load(open(os.path.join(json_root,'textcaps.json'),'r'))
textvqa = json.load(open(os.path.join(json_root,'textvqa.json'),'r'))
st_vqa = json.load(open(os.path.join(json_root,'st_vqa.json'),'r'))
ocrvqa = json.load(open(os.path.join(json_root,'ocrvqa.json'),'r'))
visualmrc = json.load(open(os.path.join(json_root,'visualmrc.json'),'r'))
iam = json.load(open(os.path.join(json_root,'iam.json'),'r'))
infographic_vqa = json.load(open(os.path.join(json_root,'infographic_vqa.json'),'r'))
diagram_image_to_text = json.load(open(os.path.join(json_root,'diagram_image_to_text.json'),'r'))

chart2text = json.load(open(os.path.join(json_root,'chart2text.json'),'r'))
dvqa = json.load(open(os.path.join(json_root,'dvqa.json'),'r'))
vistext = json.load(open(os.path.join(json_root,'vistext.json'),'r'))
chartqa = json.load(open(os.path.join(json_root,'chartqa.json'),'r'))
plotqa = json.load(open(os.path.join(json_root,'plotqa.json'),'r'))
figureqa = json.load(open(os.path.join(json_root,'figureqa.json'),'r'))
mapqa = json.load(open(os.path.join(json_root,'mapqa.json'),'r'))

tabmwp = json.load(open(os.path.join(json_root,'tabmwp.json'),'r'))
tat_qa = json.load(open(os.path.join(json_root,'tat_qa.json'),'r'))
hitab = json.load(open(os.path.join(json_root,'hitab.json'),'r'))
# multihiertt = json.load(open(os.path.join(json_root,'multihiertt.json'),'r'))
finqa = json.load(open(os.path.join(json_root,'finqa.json'),'r'))
wikisql = json.load(open(os.path.join(json_root,'llm/wikisql.json'),'r'))
msr_sqa = json.load(open(os.path.join(json_root,'llm/msr_sqa.json'),'r'))
wtq = json.load(open(os.path.join(json_root,'llm/wtq.json'),'r'))

geomverse = json.load(open(os.path.join(json_root,'geomverse.json'),'r'))
clevr_math = json.load(open(os.path.join(json_root,'clevr-math.json'),'r'))
clevr = json.load(open(os.path.join(json_root,'clevr.json'),'r'))
iconqa = json.load(open(os.path.join(json_root,'iconqa.json'),'r'))
raven = json.load(open(os.path.join(json_root,'raven_single.json'),'r'))
intergps = json.load(open(os.path.join(json_root,'intergps.json'),'r'))

ai2d = json.load(open(os.path.join(json_root,'ai2d.json'),'r'))
tqa = json.load(open(os.path.join(json_root,'tqa.json'),'r'))
scienceqa = json.load(open(os.path.join(json_root,'scienceqa.json'),'r'))

# nlvr2 = json.load(open(os.path.join(json_root,'nlvr2.json'),'r'))
# mimic_cgd = json.load(open(os.path.join(json_root,'mimic_cgd.json'),'r'))
# spot_the_diff = json.load(open(os.path.join(json_root,'spot_the_diff.json'),'r'))

websight = json.load(open(os.path.join(json_root,'websight.json'),'r'))
datikz = json.load(open(os.path.join(json_root,'datikz.json'),'r'))

openhermes = json.load(open(os.path.join(json_root,'llm/openhermes_25.json'),'r'))
lima = json.load(open(os.path.join(json_root,'llm/lima.json'),'r'))
dolly = json.load(open(os.path.join(json_root,'llm/dolly.json'),'r'))
metamathqa = json.load(open(os.path.join(json_root,'llm/metamathqa.json'),'r'))
mathinstruct = json.load(open(os.path.join(json_root,'llm/mathinstruct.json'),'r'))
orcamath = json.load(open(os.path.join(json_root,'llm/orcamath.json'),'r'))
camelaimath = json.load(open(os.path.join(json_root,'llm/camelaimath.json'),'r'))
atlasmathsets = json.load(open(os.path.join(json_root,'llm/atlasmathsets.json'),'r'))
goat = json.load(open(os.path.join(json_root,'llm/goat.json'),'r'))

result_ann = []

id  = 0
add_data = {}
for item in tqdm(vqav2+cocoqa+visual7w+aokvqa+tallyqa+okvqa+hateful_memes+vqarad+\
                 localized_narratives+screen2words+vsr+\
                 rendered_text+docvqa+textcaps+textvqa+st_vqa+ocrvqa+visualmrc+iam+infographic_vqa+diagram_image_to_text+\
                 chart2text+dvqa+vistext+chartqa+plotqa+figureqa+mapqa+\
                 tabmwp+tat_qa+hitab+\
                 #multihiertt+
                 finqa+\
                 wikisql+msr_sqa+wtq+\
                 geomverse+clevr_math+clevr+iconqa+raven+intergps+\
                 ai2d+tqa+scienceqa+\
                #  nlvr2+mimic_cgd+spot_the_diff+\
                 websight+datikz+\
                 openhermes+lima+dolly+metamathqa+mathinstruct+orcamath+camelaimath+atlasmathsets+goat
                 ):
    cur_dit = {}
    if 'images' not in item:
        cur_dit['id'] = str(id).zfill(15)
        cur_dit['conversations'] = item['conversations']
        cur_dit['source'] = item['source']
        id += 1
        
        dataset_name = cur_dit['source']
        if dataset_name not in add_data.keys():
            add_data[dataset_name] = 1
        else:
            add_data[dataset_name] += 1

        result_ann.append(cur_dit)
        continue
    image_path = os.path.join(image_root,item['images'][0])
    if not os.path.exists(image_path):
        continue
    dataset_name = item['images'][0].split('/')[0]
    if dataset_name not in add_data.keys():
        add_data[dataset_name] = 1
    else:
        add_data[dataset_name] += 1
    cur_dit['id'] = str(id).zfill(15)

    cur_dit['image'] = item['images'][0]
    cur_dit['conversations'] = item['conversations']
    cur_dit['source'] = item['source']
    id += 1
    result_ann.append(cur_dit)

print('id=',id)
print('number:',len(result_ann))
random.shuffle(result_ann)
with open(json_path,'w', encoding='utf-8') as f:
        json.dump(result_ann, f, ensure_ascii=False, indent=4)
print("done")
print(add_data)

# 23153427
# {'vqav2': 82772, 'cocoqa': 46287, 'visual7w': 14366, 'aokvqa': 16539, 'tallyqa': 98680, 
# 'hateful_memes': 8500, 'vqarad': 313, 'localized_narratives': 199998, 'screen2words': 15730, 
# 'vsr': 2157, 'rendered_text': 10000, 'docvqa': 10189, 'textcaps': 21953, 'textvqa': 21953, 
# 'st_vqa': 17247, 'ocrvqa': 165746, 'visualmrc': 3027, 'iam': 5663, 'infographic_vqa': 2118, 
# 'diagram_image_to_text': 300, 'chart2text': 26323, 'dvqa': 200000, 'vistext': 9969, 
# 'chartqa': 18265, 'plotqa': 157070, 'figureqa': 100000, 'mapqa': 37417, 'tabmwp': 22722, 
# 'tat_qa': 2199, 'hitab': 2500, 'multihiertt': 7619, 'finqa': 5276, 'wikisql': 56355, 
# 'msr_sqa': 12276, 'wtq': 56586, 'geomverse': 9303, 'clevr': 70000, 'iconqa': 27307, 
# 'raven': 42000, 'intergps': 1280, 'ai2d': 2434, 'tqa': 1493, 'scienceqa': 4976, 
# 'websight': 10000, 'datikz': 47974, 'openhermes_25': 1001551, 'lima': 1029, 'dolly': 15011, 
# 'metamathqa': 395000, 'mathinstruct': 262040, 'orcamath': 200035, 'camelaimath': 50000, 
# 'atlasmathsets': 17807579, 'goat': 1746300}