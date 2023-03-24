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


# for MEG's Audio tapes
turn the produced texts into audio files as gTTS
'''


from pprint import pprint
import csv
import json
import random
from random import sample
import os
from gtts import gTTS
import pandas as pd
import time

# for audio file alternation
from scipy.io import wavfile
import scipy.signal
from pydub import AudioSegment

if __name__ == "__main__":
    stim_data_path = "/Volumes/Neurolang_1/Project_Assistant/2021_Ongoing/2020_LTTC/Experiment_materials/LTTC_material_2nd/2nd_Stim-Materials/"
    result_data_path = "/Volumes/Neurolang_1/Project_Assistant/2021_Ongoing/2020_LTTC/Experiment_materials/LTTC_audio_behavioral/"
    text_data_path = "/Volumes/Neurolang_1/Project_Assistant/2021_Ongoing/2020_LTTC/Experiment_materials/LTTC_material_2nd/2nd_Stim-Materials/USE_Output/LTTC_modifiedTexts_output/"
    textSets_data_path = "/Volumes/Neurolang_1/Project_Assistant/2021_Ongoing/2020_LTTC/Experiment_materials/LTTC_material_2nd/2nd_Stim-Materials/USE_Output/LTTC_modifiedTexts_output/LTTC_TextSets/"
    
    
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
    #"""
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
    #"""
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
    for count in range(21, 31):
        #print(count)
        #print(type(count))
        sub_id = "%.3d" %count 
    
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
    
        replace_pwDICT = {'aegliy':"aeggli",
                          'baepay':"badpie",
                          'baydiy':"bidey",
                          'browmey':"bromay",
                          'chaeviy':"chavi",
                          'laelaxst':"lalust",
                          'laeviy':"strlavvi",
                          'maeskiy':"masgi",
                          'paenliy':"panli",
                          'payliy':"piely",
                          'vaesow':"vasle",
                          'weyaet':"way-at"}
        
    
        Setsinfo_LIST.extend(HightSetsLIST)
        Setsinfo_LIST.extend(LowtSetsLIST)
    
        print(Setsinfo_LIST)
    

        
    
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
                    if words_high_CD_setLIST[sets] != replace_pwDICT.get(words_high_CD_setLIST[sets]):
                        new_tSTR = tSTR.replace("{}", replace_pwDICT.get(words_high_CD_setLIST[sets]))
                        #print(words_high_CD_setLIST[sets])
                        #print(replace_pwDICT.get(words_high_CD_setLIST[sets]))
                        #pprint(new_tSTR)
                        new_High_textSetsLIST.extend([new_tSTR])
                    else:
                        pass
                
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
                        if words_low_CD_setLIST[sets] != replace_pwDICT.get(words_low_CD_setLIST[sets]):
                            new_tSTR = tSTR.replace("{}", replace_pwDICT.get(words_low_CD_setLIST[sets]))
                            #pprint(new_tSTR)
                            new_Low_textSetsLIST.extend([new_tSTR])
                        else:
                            pass
                
        pprint(new_High_textSetsLIST)
        print(len(new_High_textSetsLIST))
        pprint(new_Low_textSetsLIST)
        print(len(new_Low_textSetsLIST))
    
        total_stimSetLIST.extend(new_High_textSetsLIST)
        total_stimSetLIST.extend(new_Low_textSetsLIST)
    
        print(len(total_stimSetLIST))
        random.shuffle(total_stimSetLIST)
    
    
        dateLIST = []
        sub_idLIST = []
        #self_paced_rtLIST=[]
        text_noLIST = []
        #resultKeyLIST = []
    
    
        # create and save the audio files and the csv file form of textsets at once
        for stim_textSTR in total_stimSetLIST:
            ## AUDIO CREATION SECTION ##
        
            # Set the value of the transcripts
            stimtext = stim_textSTR
        
            # Language in which you want to convert
            language = 'en'
        
            # Passing the text and language to the engine, here we have marked slow=False. Which tells the module that the converted audio should have a high speed
            stim_audio = gTTS(text=stimtext, lang=language, slow=False)
            stim_audio_numINT = int(total_stimSetLIST.index(stim_textSTR))+1
        
            # Saving the converted audio in a mp3 file
            stim_audio.save(result_data_path + "S%s_behavioral_textaudio_%d.mp3" %(sub_id, stim_audio_numINT))
            time.sleep(15)
            
            # Turn the mp3 file into wav file form
            src = result_data_path + "S%s_behavioral_textaudio_%d.mp3" %(sub_id, stim_audio_numINT)
            dst = result_data_path + "S%s_behavioral_textaudio_%d.wav" %(sub_id, stim_audio_numINT)
            
            # convert wav to mp3
            sound = AudioSegment.from_mp3(src)
            sound.export(dst, format="wav")
            """
            # Upsample (24kHz to 44.1kHz) at the same time
            new_fs = 44100
            # read the target wavfile
            sample_rate, data = wavfile.read(result_data_path + "S%s_textaudio_%d.wav" %(sub_id, stim_audio_numINT))
        
            #print(sample_rate)
            #print("The data points of tape", i+1,"is" ,len(data))
            
            # resample data
            new_num_samples = round(len(data)*float(new_fs)/sample_rate)
            data = scipy.signal.resample(data, new_num_samples).astype(np.int16)  # no astype(np.int16)'s dtype == float64
            #data_dtype = data.dtype
            #print(data_dtype)
            value = data[-1]  # what does this means??   # data[-1]== -1, <class 'numpy.int16'>
            new_data = np.append(data, value)
            
            wavfile.write(filename=(result_data_path + "S%s_upsampled_textaudio_%d.wav" %(sub_id, stim_audio_numINT)), rate=44100, data=new_data)
            """
            # making the wanted info into the List form for future use
            text_noLIST.append(stim_audio_numINT)
            dateLIST.append([""])
            sub_idLIST.append(sub_id)
            #resultKeyLIST.append(keys)
            #self_paced_rtLIST.append(time_duration)
            shuffledTotalT_LIST.append([stim_textSTR])
            rating_LIST.append([""])
    
    
        # Saving the self_paced_rt result into csv file
        dataDICT = pd.DataFrame({'Sub_id':sub_idLIST,
                                 #'Date':dateLIST,
                                'Texts_no':text_noLIST,
                                #'Self-paced RT':self_paced_rtLIST,
                                #'Rating Scale': rating_LIST,
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
    
        #data_path = "/Users/ting-hsin/Docs/Github/ICN_related"
        file_name = "S%s" %sub_id + '_Listening_task.csv'
        fsave_path = result_data_path + file_name
        dataDICT.to_csv(fsave_path, sep = "," ,index = False , header = True, encoding = "UTF-8")
    
        DICT_name = "S%s" %sub_id + '_pseudowordsDICT.json'
        Dsave_path = result_data_path + DICT_name
        with open(Dsave_path, "w", newline='', encoding="UTF-8") as jsfile:
            json.dump(pseudoDICT, jsfile, ensure_ascii=False)
        
            Text_name = "S%s" %sub_id + '_textsDICT.json'
            Tsave_path = result_data_path + Text_name
            with open(Tsave_path, "w", newline='', encoding="UTF-8") as jsfile_2:
                json.dump(textsDICT, jsfile_2, ensure_ascii=False)
        print(sub_id, "is DONEEE!!!")
        time.sleep(100)
    print("ALL DONE~~")
    
    
    
    
    # Creat a new file just for the designate subs
    #sub_data_path = os.mkdir(result_data_path +"Test{}".format(2))
    
    # To create audio files from the scipts
    # https://gtts.readthedocs.io/en/latest/
    # GOOGLE gTTS >> worked but pause at the strange point  >> Try other's method first
    
    """ 
    # Convert the text you wanted into audio files
    for stim_textSTR in total_stimSetLIST[:5]:   #range(len(total_stimSetLIST)):
        #print(stim_textSTR)
        #print(type(stim_textSTR))
            
        stimtext = stim_textSTR
    
        # Language in which you want to convert
        language = 'en'
        
        # Passing the text and language to the engine, here we have marked slow=False. Which tells the module that the converted audio should have a high speed
        stim_audio = gTTS(text = stimtext, lang = language, slow = False)
        stim_audio_numINT = int(total_stimSetLIST.index(stim_textSTR))+1
        # Saving the converted audio in a mp3 file
        stim_audio.save(result_data_path + "Text_Test_original%d.mp3" %stim_audio_numINT)
    print("DONE")
    """
