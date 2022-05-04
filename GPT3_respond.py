import sys
import time
import openai
import pandas as pd
from prompts import Tense_prompt, Subj_num_prompt, Obj_num_prompt

openai.api_key = "" # get OpenAI API key

def load_data(path):
    results = []
    with open(path) as f:
        for line in f:
            label, sentence = line.split("\t")[0], line.split("\t")[1]
            results.append([sentence, label])
    return results

def write_csv_file(data_type, sentence_list, label_list, response_list):
    df = pd.DataFrame({"sentence": sentence_list,
                       "label": label_list,
                       "GPT-3_response": response_list})
    df.to_csv(data_type + "_result.csv", index=False)

def main(data_type, path):
    sentence_label = load_data(path)
    sentence_list = []
    label_list = []
    response_list = []

    if data_type == "tense":
        for i, s_l in enumerate(sentence_label):
            if (i + 1) % 100 == 0:
                print(f"Getting GPT-3 response for record {(i + 1)}...") 
            sentence = s_l[0]
            label = s_l[1]
            sentence_list.append(sentence)
            label_list.append(label)

            response = openai.Completion.create(engine="text-davinci-002",
                                                prompt=Tense_prompt(sentence),
                                                temperature=0)
            response = response["choices"][0]["text"]
            response_list.append(response)
            time.sleep(1)

    print("Writing results to csv file...")
    write_csv_file(data_type, sentence_list, label_list, response_list)

if __name__ == '__main__':
    path_dict = {
    "tense": "/Users/lining_zhang/Desktop/MSDS/1012--NLU/GPT-3_Linguistic/data/tense_data.txt",
    "subj_num": "/Users/lining_zhang/Desktop/MSDS/1012--NLU/GPT-3_Linguistic/data/subj_num_data.txt",
    "obj_num": "/Users/lining_zhang/Desktop/MSDS/1012--NLU/GPT-3_Linguistic/data/obj_num_data.txt",
    } # specify data path
    data_type = sys.argv[1]
    path = path_dict[data_type]
    main(data_type, path)

    