#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
For stimuli formation and selection

Steps: 
1. (DONE)create a list that only have 12 pseudowords
2. (DONE)import the pseudoword list
3. (DONE)randomly select 6 out of the list of 12 pseudowords as the target words
4. (DONE)select 3 out of the 6 target words and divided 3-3 into High-CD and Low-CD conditions
5. (DONE)import all the pre-selected bunch of texts
6. divided all the pre-selected texts into the High-CD and Low-CD sets
7. randomly selelct a pair set of High-CD and Low-CD texts
8. insert the assigned pseudowords into the pair set of High-CD and Low-CD texts
# The pseudowords need to be inseted in the texts first, and then randomly choose from the texts set??

'''

# for stimuli
from pprint import pprint
import csv
import json
import random
from random import sample

# for LDT and Reading Comprehension Task
import psychopy
from psychopy import visual, core, event, clock   #from psychopy import visual, core, event, gui, prefs, sound, monitors, clock,parallel
#import json
#import random
import numpy as np
from datetime import datetime,date
import pandas as pd

# need to add feedbacks of scaling and texts records

def display_ins(STR, keyPressLIST = None):
    '''
    設定欲呈現的字串及指定的反應鍵後，將會呈現字串，並需按下指定反應鍵才會進到下一個字串。
    若未指定反應鍵，則任意鍵皆可換下一張刺激
    i.e display("啦啦啦", ['space'])
    '''
    instructionsLIST = STR.split("\\\\")
    keyPressLIST = keyPressLIST
        
    for t in instructionsLIST:
        instructions = visual.TextStim(win = win, text = t)
        instructions.draw()
        win.flip()
        event.waitKeys(keyList = keyPressLIST)
    win.flip()

def display_fix():
    '''
    呈現"+"於螢幕中央
    '''
    fixation = visual.TextStim(win = win, text = "+")
    fixation.draw()
    win.flip()


if __name__ == "__main__":
    stim_data_path = "C:/Users/user/Documents/DINGHSIN/2020_LTTC/Experiment_materials/2nd_Stim-Materials/"
    result_data_path = "C:/Users/user/Documents/DINGHSIN/2020_LTTC/Experiment_materials/2nd_Stim-results_selfP_PLDT/"
    text_data_path = "C:/Users/user/Documents/DINGHSIN/2020_LTTC/Experiment_materials/2nd_Stim-Materials/USE_Output/LTTC_modifiedTexts_output/"
    textSets_data_path = "C:/Users/user/Documents/DINGHSIN/2020_LTTC/Experiment_materials/2nd_Stim-Materials/USE_Output/LTTC_modifiedTexts_output/LTTC_TextSets/"
    #C:/Users/user/Documents/DINGHSIN/2020_LTTC/Experiment_materials/2nd_Stim-Materials/USE_Output/LTTC_modifiedTexts_output/LTTC_TextSets
    
    # Stimuli Section
    # insert the stim-forming code?? >> or just present the selected texts per paragraphs??
    
    
    # Wanted data
    day = date.today()
    dateLIST = []
    sub_idLIST = []
    self_paced_rtLIST=[]
    text_noLIST = []
    resultKeyLIST = []
    
    # For key-in the id of the subject
    sub_id = str(input("Subject: "))
    
    # setting up the display win conditions
    #win = visual.Window(size = [500, 500],color = [-1, -1, -1], units ="pix")
    win = visual.Window(color = [-1, -1, -1], units ="pix", fullscr = True)
    clock = core.Clock()
    #start_time = clock.getTime()

    # Setting the instructions and the response key
    instructions_1 = """接下來你會看到一篇文章，\n請依照實驗指示進行按鍵反應，\n當你準備好的時候，\n請按下空白鍵"""
    instructions_2 = """請問對於剛剛那一篇文章理解了多少？\n請在紙上評分，評分完畢後\n請按下空白鍵繼續"""
    keypress = ['space']
    
    # for pseudoword data
    tmpLIST = []
    tmpLIST_2 = []
    pseudoLIST = []
    targetPseudoLIST = []
    controlPseudoLIST = []
    words_high_CD_setLIST = []
    words_low_CD_setLIST = []
    texts_high_CD_setLIST = []
    texts_low_CD_setLIST = []
    
    
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
        
    
    # Load in the stim_texts
    # for the stim_texts data
    textSetsLIST_High = []
    textSetsLIST_Low = []
    new_High_textSetsLIST = []
    new_Low_textSetsLIST = []
    High_stimLIST = []
    High_stim_SetLIST = []
    Low_stimLIST = []
    Low_stim_SetLIST = []
    total_stimSetLIST = []
    shuffledTotalT_LIST = []
    rating_LIST = []
    
    
    # for calling out the sets individually
    HightSetsLIST = []
    LowtSetsLIST = []
    Setsinfo_LIST = []
    
    # High_CD Set TEXTS
    # texts_high_CD_setLIST = [345, 456, 567, 367, 347]
    HighCD_CallingLIST = [["3", "4", "5"], ["4", "5", "6"], ["5", "6", "7"], ["3", "6", "7"], ["3", "4", "7"]]
    LowCD_CallingLIST = [["1", "2", "8"], ["2", "8", "9"], ["8", "9", "10"], ["1", "9", "10"], ["1", "2", "10"]]
    HightSetsLIST = random.sample(HighCD_CallingLIST, 1)
    LowtSetsLIST = random.sample(LowCD_CallingLIST, 1)
    print(HightSetsLIST)
    print(HightSetsLIST[0][0])
    print(LowtSetsLIST)
    print(LowtSetsLIST[0][0])
    
    Setsinfo_LIST.extend(HightSetsLIST)
    Setsinfo_LIST.extend(LowtSetsLIST)    
    
    
    for sets in range(3):
        # High_CD Set TEXTS
        with open (textSets_data_path + "sets_{}_LIST.json".format(HightSetsLIST[0][sets]), "r", encoding = "utf-8") as jfile_3:
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
                
        # Low_CD Set TEXTS
        # texts_low_CD_setLIST = [128, 289, 890, 190, 120]
        with open (textSets_data_path + "sets_{}_LIST.json".format(LowtSetsLIST[0][sets]), "r", encoding = "utf-8") as jfile_4:
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
                
    pprint(new_High_textSetsLIST)
    print(len(new_High_textSetsLIST))
    pprint(new_Low_textSetsLIST)
    print(len(new_Low_textSetsLIST))
    
    # Combine the High & Low texts into one LIST
    total_stimSetLIST.extend(new_High_textSetsLIST)
    total_stimSetLIST.extend(new_Low_textSetsLIST)
    
    # Shuffle the texts so that the texts would be randomized
    random.shuffle(total_stimSetLIST)
    
    
    # Experiment section
    # Reading Comprehension Task STARTS
    for i in total_stimSetLIST:
        # display instructions for Reading Comprehension phase
        display_ins(instructions_1, keypress)
        #win.flip()
        core.wait(0.5)
        
        # display fixation in the central of the screen
        display_fix()
        core.wait(1)
        
        start_time = clock.getTime()
        # display the stimuli, which would be a series of short texts
        testing_text = i
        text = visual.TextStim(win = win, text = testing_text)
        print("text starts")
        text.draw()
        win.flip()
        
        # adding rating scale in here!!!!
        
        # setting up what keypress would allow the experiment to proceed
        keys = event.waitKeys(keyList = keypress)
        event.getKeys(keyList = keypress)
        print(keys)
        print("text ends")
        if keys == ["space"]:
            end_time = clock.getTime()
            time_duration = round(end_time - start_time, 3)*1000    # normally 以毫秒作為單位
            print(time_duration)
            print(type(time_duration))
            clock.reset()
        else:
            pass
        
        # making the wanted info into the List form for future use
        text_noLIST.append(int(total_stimSetLIST.index(i))+1)
        dateLIST.append(day)
        sub_idLIST.append(sub_id)
        resultKeyLIST.append(keys)
        self_paced_rtLIST.append(time_duration)
        shuffledTotalT_LIST.append([i])
        rating_LIST.append([""])
        
        core.wait(0.5)
        
        # ask the participant to evaluate how well they understand the presented text
        display_ins(instructions_2, keypress)
        
        
    # close the window  at the end of the experiment
    win.close()
    
    # Saving the self_paced_rt result into csv file
    dataDICT = pd.DataFrame({'Sub_id':sub_idLIST,
                       'Date':dateLIST,
                       'Texts_no':text_noLIST,
                       'Self-paced RT':self_paced_rtLIST,
                       'Rating Scale': rating_LIST,
                       'Text content': shuffledTotalT_LIST
                       })
    
    pseudoDICT = {"The TargetPseudo group_6":targetPseudoLIST,
                  "The ControlPseudo group_6": controlPseudoLIST,
                  "High_CD condition pseudowords_3":words_high_CD_setLIST,
                  "Low_CD condition pseudowords_3":words_low_CD_setLIST}
    
    textsDICT = {"The High-Low Set Group": Setsinfo_LIST,
                 "High_textSetsLIST": new_High_textSetsLIST,
                 "Low_textSetsLIST":new_Low_textSetsLIST,
                 "Total_stimSetLIST":total_stimSetLIST}
    
    
    #print(type(dataDICT))
    
    #data_path = "/Users/ting-hsin/Docs/Github/ICN_related"
    file_name = sub_id + '_Reading_task.csv'
    fsave_path = result_data_path + file_name
    dataDICT.to_csv(fsave_path, sep = "," ,index = False , header = True, encoding = "UTF-8")
    
    DICT_name = sub_id + '_pseudowordsDICT.json'
    Dsave_path = result_data_path + DICT_name
    with open(Dsave_path, "w", newline='', encoding="UTF-8") as jsfile:
        json.dump(pseudoDICT, jsfile, ensure_ascii=False)
        
    Text_name = sub_id + '_textsDICT.json'
    Tsave_path = result_data_path + Text_name
    with open(Tsave_path, "w", newline='', encoding="UTF-8") as jsfile_2:
        json.dump(textsDICT, jsfile_2, ensure_ascii=False)
        

    # close all the possible ongoing commands that could be running in the background
    core.quit()  # normally we would add it, in case that anything happen
