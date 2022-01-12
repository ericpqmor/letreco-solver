import json

json_file = open('wordlist.json')
raw_data = json.load(json_file)
wordlist = raw_data['array']

wordlist = list(dict.fromkeys(wordlist))
with open("clean_wordlist.json", "a") as output:
    output.write("{\n")
    output.write('\t"array":[\n')
    
    for word in wordlist[:-1]:
        output.write('\t\t"' + word + '",\n')
        
    # Last word has no comma
    output.write('\t\t"' + wordlist[-1] + '"\n')
     
    output.write("\t]\n")
    output.write("}\n")    
