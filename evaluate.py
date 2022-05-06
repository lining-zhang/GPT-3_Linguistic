'''
Usage:
    $ python evaluate.py "tense_result.csv"
'''
import sys
import pandas as pd

def map_response_tense(df):
    label_dict = {"PAST":"past", "PRES":"present"}
    antonym_dict = {"PAST":"present", "PRES":"past"}
    if label_dict[df.label] in df["GPT3_response"]:
        return 1
    elif antonym_dict[df.label] in df["GPT3_response"]:
        return 2
    else:
        return 3

def map_response_num(df):
    label_dict = {"NN":"singular", "NNS":"plural"}
    antonym_dict = {"NN":"plural", "NNS":"singular"}
    if label_dict[df.label] in df["GPT3_response"]:
        return 1
    elif antonym_dict[df.label] in df["GPT3_response"]:
        return 2
    else:
        return 3

def main(file_path):
    data_type = file_path.split("/")[-1].split("_result")[0]
    df = pd.read_csv(file_path)

    if data_type == "tense":
        df["response_type"] = df.apply(map_response_tense, axis=1)
    else:
        df["response_type"] = df.apply(map_response_num, axis=1)

    print(f"{len(df[df.response_type==1])} out of {len(df)} records \
            ({len(df[df.response_type==1])/len(df)}) get correct answers from GPT-3")
    print(f"{len(df[df.response_type==2])} out of {len(df)} records \
            ({len(df[df.response_type==2])/len(df)}) get antonym answers from GPT-3")
    print(f"{len(df[df.response_type==3])} out of {len(df)} records \
            ({len(df[df.response_type==3])/len(df)}) get answers which do not make sense from GPT-3")

    df.to_csv(file_path.split("/")[-1].split(".")[0] + "_eval.csv", index=False)

if __name__ == '__main__':
    file_path = sys.argv[1]
    main(file_path)