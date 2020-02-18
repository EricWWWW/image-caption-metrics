from pycocoevalcap.eval import eval
import json

with open('examples/gts.json', 'r') as f: 
    gts = json.load(f)
with open('examples/res.json', 'r') as f:
    res = json.load(f)

if __name__ == '__main__':
    mp = eval(gts,res)
    print(mp)