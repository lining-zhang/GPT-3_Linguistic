import random
random.seed(12)

def data_fetch(path):
    with open(path) as f:
        result_list = []
        for line in f:
            label, sentence = line.split("\t")[1], line.split("\t")[2].replace("\n", "")
            result_list.append(label + "\t" + sentence)

    pair_list = random.sample(result_list, 500)
    return pair_list

def write_txt(filename, content_list):
    with open(filename + ".txt", "w") as f:
        for item in content_list:
            f.write("%s\n" % item)

def main():
    tense_path = "/Users/lining_zhang/Desktop/MSDS/1012--NLU/past_present.txt"
    obj_path = "/Users/lining_zhang/Desktop/MSDS/1012--NLU/obj_number.txt"
    subj_path = "/Users/lining_zhang/Desktop/MSDS/1012--NLU/subj_number.txt"

    tense_pair_list = data_fetch(tense_path)
    obj_pair_list = data_fetch(obj_path)
    subj_pair_list = data_fetch(subj_path)

    write_txt("tense_data", tense_pair_list)
    write_txt("obj_num_data", obj_pair_list)
    write_txt("subj_num_data", subj_pair_list)

if __name__ == '__main__':
    main()