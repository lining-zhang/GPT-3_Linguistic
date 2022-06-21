'''
Usage:
    $ python evaluate.py "tense_result.csv"
'''
import sys
from num2words import num2words
import pandas as pd

# def map_response_tense(df):
#     label_dict = {"PAST":"past", "PRES":"present"}
#     antonym_dict = {"PAST":"present", "PRES":"past"}
#     if label_dict[df.label] in df["GPT3_response"]:
#         return 1
#     elif antonym_dict[df.label] in df["GPT3_response"]:
#         return 2
#     else:
#         return 3

# def map_response_num(df):
#     label_dict = {"NN":"singular", "NNS":"plural"}
#     antonym_dict = {"NN":"plural", "NNS":"singular"}
#     if label_dict[df.label] in df["GPT3_response"]:
#         return 1
#     elif antonym_dict[df.label] in df["GPT3_response"]:
#         return 2
#     else:
#         return 3

def map_response_tense(df):
    label_dict = {"PAST":"past", "PRES":"present"}
    antonym_dict = {"PAST":"present", "PRES":"past"}
    if label_dict[df.label] in df["GPT3_response"].lower().replace(" ",""):
        return 1
    elif antonym_dict[df.label] in df["GPT3_response"].lower().replace(" ",""):
        return 2
    else:
        return 3

lst = [str(i) for i in range(100)]
num_lst = ['is'+i for i in lst]
alpha_lst = ['is'+num2words(num) for num in lst]
def map_response_num(df):
    label_dict = {"NN":['is 1', 'is one', "singular"], 
                  "NNS":["plural"]+num_lst+alpha_lst}
    antonym_dict = {"NN":['plural']+num_lst+alpha_lst,
                    "NNS":['is 1', 'is one', "singular"]}
    for label in label_dict[df.label]:
        if label in df["GPT3_response"].lower().replace(" ",""): return 1
    for label in antonym_dict[df.label]:
        if label in df["GPT3_response"].lower().replace(" ",""): return 2
    else:
        return 3

def main(file_path):
    # data_type = file_path.split("/")[-1].split("_result")[0]
    df = pd.read_csv(file_path)
    df = df[df['GPT3_response']!=' There is no object in the sentence.']
    # if data_type == "temp09pyt_general_prompt_tense":
    # if data_type == "tense":
    if prompt_type in ['tense', 'tense_prompt']:
        df["response_type"] = df.apply(map_response_tense, axis=1)
    else:
        df["response_type"] = df.apply(map_response_num, axis=1)

    print(f"{len(df[df.response_type==1])} out of {len(df)} records \
            ({len(df[df.response_type==1])/len(df)}) get correct answers from GPT-3")
    print(f"{len(df[df.response_type==2])} out of {len(df)} records \
            ({len(df[df.response_type==2])/len(df)}) get antonym answers from GPT-3")
    print(f"{len(df[df.response_type==3])} out of {len(df)} records \
            ({len(df[df.response_type==3])/len(df)}) get answers which do not make sense from GPT-3")

    df.to_csv('eval/' + temp + prompt_type + "_eval.csv", index=False)

if __name__ == '__main__':
    temp = sys.argv[1]
    prompt_type = sys.argv[2]
    file_path = 'result/' + temp + prompt_type + '_result.csv'
    main(file_path)