# image-caption-metrics
a py3 lib for NLP & image-caption metrics : BLEU METEOR CIDEr ROUGE SPICE WMD 

Features below:
- python3 support
- add new metric `WMD`


## Requirements
- java 1.8+
- python 3 (Python2 has not been tested)
    - gensim
- Stanford CoreNLP 3.6.0[(download)](http://nlp.stanford.edu/software/stanford-corenlp-full-2015-12-09.zip)
    - add stanford-corenlp-3.6.0.jar to `pycocoevalcap/spice/lib/`
    - add stanford-corenlp-3.6.0-models.jar to `pycocoevalcap/spice/lib/`

- `google_word2vec_model` for WMD[(download)](https://docs.google.com/uc?export=download&id=0B7XkCwpI5KDYNlNUTTlSS21pQmM)
    - unzip it and add GoogleNews-vectors-negative300.bin to `pycocoevalcap/wmd/data`

## Usage
See in `demo.py`
- Note that the input format must be the same as the file in `examples/gts.json` and `examples/res.json`
- It seems can't run in windows(error about java), run it on Linux
```
import pycocoevalcap.eval as E

with open('examples/gts.json', 'r') as f: 
    gts = json.load(f)
with open('examples/res.json', 'r') as f:
    res = json.load(f)
    
ans = E.eval(gts,tes)
print(ans)
bleu = E.get_bleu(gts,res)
print(bleu)
cider = E.get_cider(gts,res)
print(cider)
```
## References
- WMD metric from [https://github.com/mtanti/coco-caption](https://github.com/mtanti/coco-caption)
- main code from [https://github.com/wangleihitcs/CaptionMetrics](https://github.com/wangleihitcs/CaptionMetrics)
