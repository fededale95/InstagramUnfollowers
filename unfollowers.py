#importo libreria per gestire i json e os per pausa script
import json
import os

#carico i file json followers_1 e following dalla stessa cartella dell'eseguibile
with open('followers_1.json', 'r') as file0:
    followers = json.load(file0)
    
with open('following.json', 'r') as file1:
    following = json.load(file1)
    following = following['relationships_following']

#confronto
unfollowers = []              
for seguito in following:
    mutual=False
    for seguace in followers:
        if(seguito['string_list_data'][0]['value']==seguace['string_list_data'][0]['value']):
            mutual=True
    if(not(mutual)):
        unfollowers.append(seguito['string_list_data'][0]['value'])

#stampa su file   
result = open("unfollowers.txt", "w")
result.write('----------------UNFOLLOWERS By Fede16----------------\n\n')
result.write('Followers: '+str(len(followers))+'\n')
result.write('Following: '+str(len(following))+'\n\n')

result.write('Unfollowers: '+str(len(unfollowers))+'\n\n')
result.write('List:\n\n')
for item in unfollowers:
    result.write(item+'\n')
result.close()

#fine
print('----------------UNFOLLOWERS By Fede16----------------\n\n')
print('All result saved in unfollowers.txt file.\n\n')
os.system("pause")
