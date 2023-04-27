## Material Preparation Steps

### Text preparation (based on the real words)
1. List the 5th-8th 1000 test vocabulary in VST
2. Find the vocabulary info from MALD (Copy & Paste) into a excel file, and then refile into a csv file
3. Filter out the unfitted words based on its POS(Noun), frequencyCOCA(lowFreq), NumSylls(2-3), PhonLev(5.~7.) until only 10 words left
4. We want 100 texts in total, therefore every words need 10 articles in hands(10*10)
5. Select the paragraph that contains the chosen target real words
6. manually modified the paragraph into equal length(150 words) and only 1 appearance of the target real words per texts
7. group the modified texts into text sets according to the target real words (10 words into 10 text sets)
8. (Within group) calculate the semantic similarity (using USE) of between texts in every sets, and get the mean similarity of the group
9. (Between group) Divided 10 sets into 2 CD condition sets based on the averaged similarity(H-CD above 0.5, L-CD below 0.5)
10.  Switch every target real words in the 2 CD sets into a big curly brackets{} for later pseudowords insertion

### Stimuli formation (Pseudowords insertion & 30 stim selection)
11. Select the pseudowords from MALD based on the NumSylls(2), PhonLev(5.~7.), and the duration(400much~500much)(12 pseudos in total, this amount is based on how many texts you want to present to the participants)
12. (i.e. 12 -> 6/6) Randomly select half of the pseudowords as the target pseudowords in the CD conditions, and consider the rest half of the pseudowords as the control group
13. (i.e. 6/6 -> 6/(3/3)) Randomly chose half of target pseudowords as High CD target pseudos, and the other half pseudos as the Low CD targets. 
14. (Step 12 & 13 were repeated in every experiment conducted on each participants)
15. Form the set combinations based on the CD condition without repetition(3 out of 5, C(3, 5)), and then hand-pick the repeated combinations out of the result, which shown each combination consists 3 text sets labeling the same CD condition (i.e. HCD = [345, 547]; LCD = [128, 289])
16. Randomly select 1 set combination each from the 2 CD sets (HCD=[345];LCD[128]), in which contains 10 texts in each set number listed in the combination, 60 texts in the selected combinations in both condition
17. Randomly select 5 texts out of each listed set conclude in the combination, therefore 15 per condition, 30 texts in total
18. Insert the target pseudos into the texts by the assigned CD conditions accordingly
19. Shuffle the presentation sequence to the display of the texts in both conditions. 
