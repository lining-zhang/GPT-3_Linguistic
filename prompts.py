def Tense_prompt(sentence):
    return f"""
    \n\nQ: Is the tense of the sentence "{sentence}" present or past?
    \nA:"""

def Subj_num_prompt(sentence):
    return f"""
    \n\nQ: Is the number of the subject of the sentence "{sentence}" singular or plural?
    \nA:"""

def Obj_num_prompt(sentence):
    return f"""
    \n\nQ: Is the number of the object of the sentence "{sentence}" singular or plural?
    \nA:"""

def Tense_prompt_general(sentence):
    return f"""
    \n\nQ: What is the tense of the sentence "{sentence}"?
    \nA:"""

def Subj_prompt_general(sentence):
    return f"""
    \n\nQ: What is the number of the subject of the sentence "{sentence}"?
    \nA:"""

def Obj_prompt_general(sentence):
    return f"""
    \n\nQ: What is the number of the object of the sentence "{sentence}"?
    \nA:"""