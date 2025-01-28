The Command Line Cup:

# 1.Enter the maze:
>>For this task first of all i cloned the repo TheCommandLineCup using the command [git clone https://github.com/KshitijThareja/TheCommandLineCup.git]
>>Then created the new directory in the same repository named "codes" using the command [mkdir codes]

# 2. First challenge:
>>found x=6 and y=5 
>>In the current repo went inside the directory 06 [cd 06], then read the spell_05.txt[cat spell_05.txt],got the spell Impedimenta then searched inside the directory spellbook for the code related to this spell and then got the code "aHR0cHM6Ly9naX" [cat Impedimenta.py]
>> inside the directory codes created a new file Part_1.txt then added the code using the command [echo "aHR0cHM6Ly9naX" > Part_1.txt]
>> then for pushed this folder to my repo by cloning my repo using the command [git clone https://github.com/sree-24066/amfoss-tasks.git], then craeated a new folder task-01[mkdir task-01] then pushed the code using the commands below
[git add codes/Part_1.txt]
[git commit -m "pushed Part_1.txt with the secret code aHR0cHM6Ly9naX"]
[git push origin main]

# 3. Second challenge:
>>found x=3 and y=2 
>>In the current repo went inside the directory 02 [cd 02], then read the spell_03.txt[cat spell_03.txt],got the spell Stupefy then searched inside the directory spellbook for the code related to this spell and then got the code "RodWIuY29tL1RoZ" [cat Stupefy.py]
>> inside the directory codes created a new file Part_2.txt then added the code using the command [echo "RodWIuY29tL1RoZ" > Part_2.txt]
>> then pushed this folder to the direc amfoss-tasks inside the folder task-01 using the commands below
[git add codes/Part_2.txt]
[git commit -m "pushed Part_2.txt with the secret code RodWIuY29tL1RoZ"]
[git push origin main]

# 4. Third challenge:
>>The branch name is defenseAgainstTheDarkArts and the spell is Riddikulus
checked the current branch using the command [git branch],then changed the branch using [git switch defenseAgainstTheDarkArts]
then searched for the spell Riddikulus in this branch inside the spellbook and got the code Uh1bnRzbWFuNC9U using the command [cat spellbook/Riddikulus.py] 
>> inside the directory codes created a new file Part_3.txt then added the code using the command [echo "Uh1bnRzbWFuNC9U" > Part_3.txt]
>> then pushed this folder to the direc amfoss-tasks inside the folder task-01 using the commands below
[git add codes/Part_3.txt]
[git commit -m "pushed Part_3.txt with the secret code Uh1bnRzbWFuNC9U"]
[git push origin main]

# 5. Fourth challenge:
>> checked the commit logs in the repo using the command [git log]

# 6. The End:
>>created a new folder in codes called finalcode.txt, then concatenated all the parts to this folder using the command [cat Part_1.txt Part_2.txt Part_3.txt Part_4.txt > finalcode.txt],After concatenating deleted all the files except finalcode.txt using the command [rm Part1.txt Part2.txt Part3.txt Part4.txt]
>>then decoded the finalcode.txt using the command [base64 -d finalcode.txt] and got the repo link (https://github.com/TheHuntsman4/TheFinalSpel)





















