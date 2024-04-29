import json
import pandas as pd
from datasets import load_dataset

def get_python_data():
    data=[]
    d = load_dataset("codeparrot/xlcost-text-to-code", "Python-program-level")
    for i, entry in enumerate(d["train"]):
        data.append(entry)
        if i == 999:
            break
    
    return data


def get_cSharp_data():
    data=[]
    a = load_dataset("codeparrot/xlcost-text-to-code", "Csharp-program-level")
    for i, entry in enumerate(a["train"]):
        data.append(entry)
        if i == 999:
            break
    
    return data


def get_javascript_data():
    data=[]
    a = load_dataset("codeparrot/xlcost-text-to-code", "Javascript-program-level")
    for i, entry in enumerate(a["train"]):
        data.append(entry)
        if i == 999:
            break
    
    return data


def addToDict(dictionary,language,code="",text=""):
  dictionary["language"].append(language)
  dictionary["code"].append(code)
  dictionary["text"].append(text)


def add_data():
    dataset = {
        "language":[],
        "code": [],
        "text": []
        }
    data=[]

    python = get_python_data()
    cSharp = get_cSharp_data()
    javascript = get_javascript_data()

    for p in python:
        addToDict(dataset, "Python", p["code"], p["text"])
    for c in cSharp:
        addToDict(dataset, "C#", c["code"], c["text"])
    for j in javascript:
        addToDict(dataset, "Javascript", j["code"], j["text"])

    df = pd.DataFrame(dataset)
    df.to_csv("dataset.csv", sep=";", encoding='utf-8-sig', index=False)


add_data()
'''
@misc{zhu2022xlcost,
     title = {XLCoST: A Benchmark Dataset for Cross-lingual Code Intelligence},
     url = {https://arxiv.org/abs/2206.08474},
     author = {Zhu, Ming and Jain, Aneesh and Suresh, Karthik and Ravindran, Roshan and Tipirneni, Sindhu and Reddy, Chandan K.},
     year = {2022},
     eprint={2206.08474},
     archivePrefix={arXiv}
}
'''