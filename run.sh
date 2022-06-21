eval "$(conda shell.bash hook)"
conda activate py38

# for tempt in '0' '0.5' '0.7' '0.9'; 
# do for prompt in 'tense' 'tense_prompt' 'obj' 'obj_prompt' 'subj' 'subj_prompt'; 
# do echo 'begin generating' $tempt $prompt;
# python GPT3_respond.py $tempt $prompt;
# done;
# done

# for tempt in '0' '0.5' '0.7' '0.9'; 
# do for prompt in 'subj_prompt';
# do echo 'begin evaluating' $tempt $prompt;
# python GPT3_respond.py $tempt $prompt;
# done;
# done

for tempt in '0' '0.5' '0.7' '0.9'; 
do for prompt in 'tense' 'tense_prompt' 'obj' 'obj_prompt' 'subj' 'subj_prompt'; 
do echo 'begin evaluating' $tempt $prompt;
python evaluate.py $tempt $prompt;
done;
done

