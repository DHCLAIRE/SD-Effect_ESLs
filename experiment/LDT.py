#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import psychopy
from psychopy import visual, core, event, clock
import json
import random
from random import sample
import numpy as np
from datetime import datetime,date
import pandas as pd
from pprint import pprint

'''
key press: need to be set (we'll use 2 bottons in here')
reaction time: need to be recorded
'''

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
    
    # Step_0: load in all the stimuli
    # testing stimuli (realwordLIST & pseudowordLIST)
    #realwordLIST = ["blue", "green", "yellow", "red", "orange"]
    #pseudowordLIST = ["thorpt", "rairn", "coan", "flatch", "meeg"]
    
    
    #sub_id = str(input("Subject: "))
    stim_data_path = "/Volumes/Neurolang_1/Project_Assistant/2021_Ongoing/2020_LTTC/Experiment_materials/LTTC_material_2nd/2nd_Stim-Materials/"
    result_data_path = "/Volumes/Neurolang_1/Project_Assistant/2021_Ongoing/2020_LTTC/Experiment_materials/LTTC_material_2nd/2nd_Stim-results_selfPRT_PLDT/"
    
    # setting up usable dataLIST
    pseudoLIST = []
    targetPseudoLIST = []
    controlPseudoLIST = []
    words_high_CD_setLIST = []
    words_low_CD_setLIST = []
    PLDT_LIST = []
    """
    # 2_Import the pseudoword list (in json file form)
    with open (stim_data_path + "LTTC-pseudowordLIST.json", "r", encoding = "utf-8") as jfile:
        pseudoLIST = json.load(jfile)
        #print("12 pseudowords = ", pseudoLIST)
        
    # 3_Randomly select 6 out of the list of 12 pseudowords as the target words
        # randomly select 6 target pseudowords from the list
        targetPseudoLIST = sample(pseudoLIST, 6)
        
        # collect other 6 pseudowords as the control group
        for t in pseudoLIST:
            if t not in targetPseudoLIST:
                controlPseudoLIST.extend([t])
            else:
                pass
            
        #print("The TargetPseudo words = ", targetPseudoLIST)
        #print("The ControlPseudo words = ", controlPseudoLIST)
        
    # 4_Select 3 out of the 6 target words and divided 3-3 into High-CD and Low-CD conditions
        words_high_CD_setLIST = sample(targetPseudoLIST, 3)
        
        for w in targetPseudoLIST:
            if w not in words_high_CD_setLIST:
                words_low_CD_setLIST.extend([w])
            else:
                pass

        #print("High-CD_set = ", words_high_CD_setLIST)
        #print("Low-CD_set = ", words_low_CD_setLIST)

        random.shuffle(pseudoLIST)
        """
    
    # key in number for notifying which subject it is
    sub_id = str(input("Subject: "))
    
    #剩把pseudoDICT的值叫出來
    pseudoLIST = []
    targetPseudoLIST = []
    controlPseudoLIST = []
    words_high_CD_setLIST = []
    words_low_CD_setLIST = []
    
    
    DICT_name = sub_id + '_pseudowordsDICT.json'
    Dsave_path = result_data_path + DICT_name
    
    with open (Dsave_path, "r", encoding = "utf-8") as jfile:
        pseudoDICT = json.load(jfile)
        pprint(pseudoDICT)
        #print(pseudoDICT["High_CD condition pseudowords_3"])
        pseudoLIST.extend(pseudoDICT["The ControlPseudo group_6"])
        pseudoLIST.extend(pseudoDICT["The TargetPseudo group_6"])
        
        targetPseudoLIST.extend(pseudoDICT["The TargetPseudo group_6"])
        
    pass



    # LDT Wanted data
    day = date.today()
    dateLIST = []
    sub_idLIST = []
    resultKeyLIST = []
    stimLIST = []
    conditionLIST = []
    LDT_rtLIST = []
    correctnessLIST = []
    responseLIST = []
    correctLIST = []
    
    # key in number for notifying which subject it is
    #sub_id = str(input("Subject: "))
    
    # Step_1: Show the instructions
    # Setting the presented window
    #win = visual.Window(size = [500, 500],color = [-1, -1, -1], units ="pix")
    win = visual.Window(color = [-1, -1, -1], units ="pix", fullscr = True)
    clock = core.Clock()
    #start_time = clock.getTime()  >>change position to make the calculation correct

    # Setting the instructions and the response key
    instructions_1 = """接下來你會看到一連串的字詞，\n請依照實驗指示進行按鍵反應，\n當你準備好的時候，\n請按下空白鍵"""
    instructions_2 = """看過請按z 沒看過請按/\n請按空白鍵繼續\\\\將你的左食指輕放在z鍵，右食指輕放在/鍵。\n請按空白鍵繼續\\\\當字詞出現時，請盡快且正確的進行按鍵反應。\n請按空白鍵繼續"""
    keypress = ['space']
    
    core.wait(3)
    
    #Display the instructions
    display_ins(instructions_1, keypress)
    display_ins(instructions_2, keypress)
    
    core.wait(3)
    
    # 假詞all重新排列後依序送出，整個LIST重複送10次
    # Step_4: show the stimuli(real words or pseudowords), and remain the stimuli for 400ms  # randomly display would also be crucial!!
    for i in range(10):
        
        # randomly select the wanted pseudoword from the list  
        random.shuffle(pseudoLIST)
        for stim_wordSTR in pseudoLIST:
            # display fixation in the central of the screen
            display_fix()
            core.wait(1)
            
            start_time = clock.getTime()
            # Show the testing stimulus
            testing_stimuli = visual.TextStim(win = win, text = stim_wordSTR)  # how to control that every words only
            testing_stimuli.draw()
            win.flip()  # always add this after an item was presented
        
            #setting up what keypress would allow the experiment to proceed
            keys = event.waitKeys(maxWait = 5, keyList = ['z', 'slash'])
            event.getKeys(keyList = ['z', 'slash'])
            print(keys)
        
            # 再加上if else的判斷決定是否要收或是要怎麼紀錄這反應
            if keys == ["z"]:
                conditionLIST = ["seen"]
                end_time = clock.getTime()
                time_duration = round(end_time - start_time, 3)*1000    # normally 以毫秒作為單位
                print(time_duration)
                #print(type(time_duration))
                clock.reset()
        
            elif keys == ["slash"]:
                conditionLIST = ["unseen"]
                end_time = clock.getTime()
                time_duration = round(end_time - start_time, 3)*1000    # normally 以毫秒作為單位
                print(time_duration)
                #print(type(time_duration))
                clock.reset()
            
            else:
                keys = ["Wrong!!"]
                conditionLIST = ["N/A"]
                time_duration = 0
                print(time_duration)
                clock.reset()
        
            # calculate the correctness of the LDT response
            if stim_wordSTR in targetPseudoLIST:
                #conditionLIST = ["seen"]
                if keys == ["z"]:
                    correctLIST = ["True"]
                #conditionLIST = ["unseen"]
                elif keys == ["slash"]:
                    correctLIST = ["False"]
                else:
                    correctLIST = ["N/A"]
        
            elif stim_wordSTR not in targetPseudoLIST:
                #conditionLIST = ["seen"]
                if keys == ["z"]:
                    correctLIST = ["False"]
                #conditionLIST = ["unseen"]
                elif keys == ["slash"]:
                    correctLIST = ["True"]
                else:
                    correctLIST = ["N/A"]
            else:
                pass
            
        
            # making the wanted info into the List form for future use
            sub_idLIST.append(sub_id)
            dateLIST.append(day)
            stimLIST.append(stim_wordSTR)
            resultKeyLIST.append(keys)
            responseLIST.append(conditionLIST)
            LDT_rtLIST.append(time_duration)
            correctnessLIST.append(correctLIST)
        
            #core.wait(0.5)
        
            # close the window  at the end of the experiment
    win.close()
        
        
    # Saving the self_paced_rt result into csv file
    dataDICT = pd.DataFrame({'Sub_id':sub_idLIST,
                           'Date':dateLIST,
                           'Stimuli':stimLIST,
                           'Keypress':resultKeyLIST,
                           'Response':responseLIST,
                           'LDT_RT':LDT_rtLIST,
                           'Correctness':correctnessLIST
                           })
    
    #data_path = "/Users/ting-hsin/Docs/Github/ICN_related/"
    file_name = sub_id + '_LDT_results.csv'
    save_path = result_data_path + file_name
    dataDICT.to_csv(save_path, sep = "," ,index = False , header = True, encoding = "UTF-8")
    
    # close all the possible ongoing commands that could be running in the background
    core.quit()  # normally we would add it, in case that anything happen

    """
       # turn all info into dataframe, and then save it as a csv file  # >> rewrite the following info
    data=pd.DataFrame({'sid':sub_id,
                   'trial_list':trial,
                   'duration':interval,
                   'trial_no':trial_no,
                    'date':date,
                    'trigger':trial_trigger,
                    'response_key':response,
                    'rt':response_time
                    })
    
    # close all the possible ongoing commands that could be running in the background
    core.quit()  # normally we would add it, in case that anything happen
    
    # Below is the testing zone for testing RatingScale function.
    win = visual.Window(size = [500, 500],color = [-1, -1, -1], units ="pix")
    
    ratingScale = visual.RatingScale(win)
    item = visual.TextStim(win = win, text = "THIS IS A TESTING SENTENCE!")
    
    
    while ratingScale.noResponse:
        item.draw()
        ratingScale.draw()# the rating scale could work,but don't know why it can not be clicked
        keys = event.waitKeys(maxWait = 10, keyList = ['z', 'slash'])
        event.getKeys(keyList = ['z', 'slash'])
        
        
        if keys == ["z"]:
            keys = ["real_word"]
            #end_time = clock.getTime()
            #time_duration = round(end_time - start_time, 4)*1000    # normally 以毫秒作為單位
            #print(time_duration)
            #clock.reset()
        
        elif keys == ["slash"]:
            keys = ["pseudoword"]
            #end_time = clock.getTime()
            #time_duration = round(end_time - start_time, 4)*1000    # normally 以毫秒作為單位
            #print(time_duration)
            #clock.reset()
            
        else:
            keys = ["Wrong!!"]
            #time_duration = 0
            #print(time_duration)
            #clock.reset()
        

        resultKeyLIST.append(keys)
        
        
        
        
        
        win.flip()
    print(resultKeyLIST)
    
    rating = ratingScale.getRating()
    decisionTime = ratingScale.getRT()
    choiceHistory = ratingScale.getHistory()
    
    """




    """
    # NOTES:
    
    from psychopy.visual  # 主要用這個
    
    # 前面要先設定螢幕視窗
    # win = psychopy.visual.Window(size = [500, 500], units ="pix")
    
    # key = psychopy.event.waitKeys()  # 按任何按鍵都會跳到下一張
    # event.getKeys(keyList = ['space'])  # 指定按鍵才可以跳到下一張  
    # 若指定按鍵沒有收到作業，這裡同時紀錄時間的要歸零，不然system會卡住
    
    #需要在寫if else 決定她按鍵反應時要怎記錄時間，然後press到哪個才會做反應
    
    # 按鍵反應 + 按鍵時間（RT）+ (trigger_for 腦波) + 正確與否
    # basic info = trails數（的第幾題）,trai_list(第幾次trial), sub_num, date, duration
    """