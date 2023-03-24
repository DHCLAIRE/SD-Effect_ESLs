#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
Steps: 
1. (DONE)create a list that only have 12 pseudowords
2. (DONE)import the pseudoword list
3. (DONE)randomly select 6 out of the list of 12 pseudowords as the target words
4. (DONE)select 3 out of the 6 target words and divided 3-3 into High-CD and Low-CD conditions
5. (DONE)import all the pre-selected bunch of texts
6. (DONE)divided all the pre-selected texts into the High-CD and Low-CD sets
7. (KIND OF?)randomly selelct a pair set of High-CD and Low-CD texts
8. insert the assigned pseudowords into the pair set of High-CD and Low-CD texts
# The pseudowords need to be inseted in the texts first, and then randomly choose from the texts set??

'''


from pprint import pprint
import csv
import json
import random
from random import sample


if __name__ == "__main__":
    stim_data_path = "/Volumes/Neurolang_1/Project_Assistant/2021_Ongoing/2020_LTTC/Experiment_materials/2nd_Stim-Materials/"
    result_data_path = "/Volumes/Neurolang_1/Project_Assistant/2021_Ongoing/2020_LTTC/Experiment_materials/2nd_Stim-results_selfPRT_PLDT/"
    text_data_path = "/Volumes/Neurolang_1/Project_Assistant/2021_Ongoing/2020_LTTC/Experiment_materials/2nd_Stim-Materials/USE_Output/LTTC_modifiedTexts_output/"
    textSets_data_path = "/Volumes/Neurolang_1/Project_Assistant/2021_Ongoing/2020_LTTC/Experiment_materials/2nd_Stim-Materials/USE_Output/LTTC_modifiedTexts_output/LTTC_TextSets/"
    tmpLIST = []
    tmpLIST_2 = []
    pseudoLIST = []
    targetPseudoLIST = []
    controlPseudoLIST = []
    words_high_CD_setLIST = []
    words_low_CD_setLIST = []
    texts_high_CD_setLIST = []
    texts_low_CD_setLIST = []
    
    #texts_totalDICT = {}
    #texts_high_CD_setDICT = {}
    #texts_low_CD_setDICT = {}
    
    """
    # 1_Create the pseudoword LIST and save it into json file
    
    # Open the csv file that contains the info of 12 pseudowords
    with open (stim_data_path + "2nd_Pseudowords_12.csv", "r", encoding = "utf-8") as raw_file:
        fileLIST = raw_file.read().split("\n")
        #pprint(fileLIST)
    
    # Organized the csv into a more convenient form of structure, which is a list of lists that carry the info of each pseudoword
    for i in fileLIST:
        tmpLIST = i.split(",")
        tmpLIST_2.append(tmpLIST)
    # exclude the head title in the csv file
    tmpLIST_2.pop(0)
    print(tmpLIST_2)
    
    # Extract the pseudowords from the organized list
    for k in tmpLIST_2:
        pseudoSTR = k[0]
        pseudoLIST.extend([pseudoSTR])
    print(pseudoLIST)
    
    # Save the pseudoword LIST into a json file
    with open(stim_data_path + 'LTTC-pseudowordLIST.json', "w", newline='', encoding="UTF-8") as jsonfile:
        json.dump(pseudoLIST, jsonfile, ensure_ascii=False)
        """
    """
    # 2_Import the pseudoword list (in json file form)
    with open (stim_data_path + "LTTC-pseudowordLIST.json", "r", encoding = "utf-8") as jfile:
        pseudoLIST = json.load(jfile)
        print("12 pseudowords = ", pseudoLIST)
        
    # 3_Randomly select 6 out of the list of 12 pseudowords as the target words
        # randomly select 6 target pseudowords from the list
        targetPseudoLIST = sample(pseudoLIST, 6)
        
        # collect other 6 pseudowords as the control group
        for t in pseudoLIST:
            if t not in targetPseudoLIST:
                controlPseudoLIST.extend([t])
            else:
                pass
            
        print("The TargetPseudo words = ", targetPseudoLIST)
        print("The ControlPseudo words = ", controlPseudoLIST)
        
    # 4_Select 3 out of the 6 target words and divided 3-3 into High-CD and Low-CD conditions
        words_high_CD_setLIST = sample(targetPseudoLIST, 3)
        
        for w in targetPseudoLIST:
            if w not in words_high_CD_setLIST:
                words_low_CD_setLIST.extend([w])
            else:
                pass

        print("High-CD_set = ", words_high_CD_setLIST)
        print("Low-CD_set = ", words_low_CD_setLIST)
        
        
    
    # 5_Import all the pre-selected bunch of texts
    """
    """
    # reload the texts
    with open (text_data_path + "LTTC-modifiedText_OneLIST_present.json", "r", encoding = "utf-8") as jfile_2:
        textLIST = json.load(jfile_2)
        #pprint(textLIST[0:10])
        
        # divide all the sets into an individual LIST by topic
        # High-CD setsLIST (3/4/5/6/7)
        sets_3_LIST = textLIST[20:30]
        sets_4_LIST = textLIST[30:40]
        sets_5_LIST = textLIST[40:50]
        sets_6_LIST = textLIST[50:60]
        sets_7_LIST = textLIST[60:70]
        
        # Low-CD setsDICT (1/2/8/9/10)
        sets_1_LIST = textLIST[0:10]
        sets_2_LIST = textLIST[10:20]
        sets_8_LIST = textLIST[70:80]
        sets_9_LIST = textLIST[80:90]
        sets_10_LIST = textLIST[90:]
        
        print(sets_3_LIST)
    
        # save all the sets into an individual json file
        with open(textSets_data_path + "sets_10_LIST.json", "w", newline='', encoding="UTF-8") as setsfile:
            json.dump(sets_10_LIST, setsfile, ensure_ascii=False)
        """

    
    textSetsLIST_High = []
    textSetsLIST_Low = []
    new_High_textSetsLIST = []
    new_Low_textSetsLIST = []
    High_stimLIST = []
    High_stim_SetLIST = []
    Low_stimLIST = []
    Low_stim_SetLIST = []
    total_stimSetLIST = []
    suffledTotalT_LIST = []
    
    # High_CD Set TEXTS
    # texts_high_CD_setLIST = [345, 456, 567, 367, 347]
    for sets in range(3):
        with open (textSets_data_path + "sets_{}_LIST.json".format(sets+4), "r", encoding = "utf-8") as jfile_3:
            textSetsLIST_High = json.load(jfile_3)
            
            # randomly select 5 texts from the json file
            High_stimLIST = random.sample(textSetsLIST_High, 5)
            #pprint(High_stimLIST)
            #print(len(High_stimLIST))

            # replace {} to the assigned pseudowords by different condition
            for tSTR in High_stimLIST:
                new_tSTR = tSTR.replace("{}", words_high_CD_setLIST[sets])
                #pprint(new_tSTR)
                new_High_textSetsLIST.extend([new_tSTR])
                
    print(new_High_textSetsLIST)
    print(len(new_High_textSetsLIST))
     
     
     # Low_CD Set TEXTS
     # texts_low_CD_setLIST = [128, 289, 890, 190, 120]
    for sets in range(3):
        with open (textSets_data_path + "sets_{}_LIST.json".format(sets+8), "r", encoding = "utf-8") as jfile_4:
            textSetsLIST_Low = json.load(jfile_4)
            
            # randomly select 5 texts from the json file
            Low_stimLIST = random.sample(textSetsLIST_Low, 5)
            #pprint(Low_stimLIST)
            #print(len(Low_stimLIST))

            # replace {} to the assigned pseudowords by different condition
            for tSTR in Low_stimLIST:
                new_tSTR = tSTR.replace("{}", words_low_CD_setLIST[sets])
                #pprint(new_tSTR)
                new_Low_textSetsLIST.extend([new_tSTR])
                
    print(new_Low_textSetsLIST)
    print(len(new_Low_textSetsLIST))
    
    total_stimSetLIST.extend(new_High_textSetsLIST)
    total_stimSetLIST.extend(new_Low_textSetsLIST)
    
    print(len(total_stimSetLIST))
    random.shuffle(total_stimSetLIST)
    
    
    
    """
    pseudoDICT = {}
    
    sub_id = "001"
    
    DICT_name = sub_id + '_pseudowordsDICT.json'
    Dsave_path = result_data_path + DICT_name
    with open (Dsave_path, "r", encoding = "utf-8") as jfile:
        pseudoDICT = json.load(jfile)
        
        pprint(pseudoDICT)
        print(type(pseudoDICT["High_CD condition pseudowords_3"]))
        
        pseudoLIST.extend(pseudoDICT["The ControlPseudo group_6"])
        pseudoLIST.extend(pseudoDICT["The TargetPseudo group_6"])
        print(pseudoLIST)
        
        targetPseudoLIST.extend(pseudoDICT["The TargetPseudo group_6"])
        print(targetPseudoLIST)
        
        
    #剩把pseudoDICT的值叫出來
    pseudoLIST = []
    targetPseudoLIST = []
    controlPseudoLIST = []
    words_high_CD_setLIST = []
    words_low_CD_setLIST = []
    
    """
    
    """
                
        # High-CD setsDICT (3/4/5/6/7)
        sets_3_DICT = {'3':textLIST[20:30]}
        sets_4_DICT = {'4':textLIST[30:40]}
        sets_5_DICT = {'5':textLIST[40:50]}
        sets_6_DICT = {'6':textLIST[50:60]}
        sets_7_DICT = {'7':textLIST[60:70]}
        texts_high_CD_setDICT.update(sets_3_DICT)
        texts_high_CD_setDICT.update(sets_4_DICT)
        texts_high_CD_setDICT.update(sets_5_DICT)
        texts_high_CD_setDICT.update(sets_6_DICT)
        texts_high_CD_setDICT.update(sets_7_DICT)
        #pprint(texts_high_CD_setDICT)
        print(len(texts_high_CD_setDICT))

        # Low-CD setsDICT (1/2/8/9/10)
        sets_1_DICT = {'1':textLIST[0:10]}
        sets_2_DICT = {'2':textLIST[10:20]}
        sets_8_DICT = {'8':textLIST[70:80]}
        sets_9_DICT = {'9':textLIST[80:90]}
        sets_10_DICT = {'10':textLIST[90:]}
        
        texts_low_CD_setDICT.update(sets_1_DICT)
        texts_low_CD_setDICT.update(sets_2_DICT)
        texts_low_CD_setDICT.update(sets_8_DICT)
        texts_low_CD_setDICT.update(sets_9_DICT)
        texts_low_CD_setDICT.update(sets_10_DICT)
        #pprint(texts_low_CD_setDICT)
        print(len(texts_low_CD_setDICT))

        # texts_high_CD_setLIST = [345, 456, 567, 367, 347] >> we randomly choose one the set from these 5 sets
        tHigh_345LIST = []
        tHigh_345LIST.append(sets_3_LIST)
        tHigh_345LIST.append(sets_4_LIST)
        tHigh_345LIST.append(sets_5_LIST)
        #pprint(tHigh_345LIST)
        
        stim_345_LIST = []
        tmpLIST_3 = sample(sets_3_LIST, 5)
        tmpLIST_4 = sample(sets_4_LIST, 5)
        tmpLIST_5 = sample(sets_5_LIST, 5)
        stim_345_LIST.extend(tmpLIST_3)
        stim_345_LIST.extend(tmpLIST_4)
        stim_345_LIST.extend(tmpLIST_5)
        #print(stim_345_LIST)
        #print(len(stim_345_LIST))
        
        
        tHigh_345LIST = []
        tHigh_345LIST.append(sets_3_LIST)
        tHigh_345LIST.append(sets_4_LIST)
        tHigh_345LIST.append(sets_5_LIST)
        #pprint(tHigh_345LIST)
        
        stim_345_LIST = []
        tmpLIST_3 = sample(sets_3_LIST, 5)
        tmpLIST_4 = sample(sets_4_LIST, 5)
        tmpLIST_5 = sample(sets_5_LIST, 5)
        stim_345_LIST.extend(tmpLIST_3)
        stim_345_LIST.extend(tmpLIST_4)
        stim_345_LIST.extend(tmpLIST_5)
        #print(stim_345_LIST)
        #print(len(stim_345_LIST))

        realwords = ["premier", "butler" ,"thesis" ,"gimmick" ,"yogurt" , "palette", "eclipse", "marrow", "locust", "cabaret"]
        tmpLIST_X = []
        #for realw in range(len(stim_345_LIST)):
        for t in stim_345_LIST:
            print(len(t))
            if "thesis" in t:
                print("There's a word in here!")
                t.replace("thesis", "{}")
                pprint(t)
            elif "gimmick" in t:
                print("There's a word in here!")
                t.replace("gimmick", "{}")
                pprint(t)
            elif "yogurt" in t:
                print("There's a word in here!")
                t.replace("yogurt", "{}")
                pprint(t)
            else:
                print("NONE")
                #pass
            
            for realw in realwords:
                if realw in t:
                    pprint(t)
                    #t.replace("{}".format(realw), "{}")
                    #pprint(t)
                    #tmpSTR = [t]
                    #tmpLIST_X.extend(tmpSTR)
                else:
                    pass
            #stim_345_LIST = tmpLIST_X
        #pprint(stim_345_LIST)
        #pprint(len(stim_345_LIST))
        

        tHigh_456LIST = []
        tHigh_567LIST = []
        tHigh_367LIST = []
        tHigh_347LIST = []
        
        # Low-CD sets
        # texts_low_CD_setLIST = [128, 289, 890, 190, 120] >> we randomly choose one the set from these 5 sets
        tlow_128LIST = []
        tlow_289LIST = []
        tlow_890LIST = []
        tlow_190LIST = []
        tlow_120LIST = []
        """

