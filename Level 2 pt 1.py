def answer(names):
    # This method takes a list of names and returns a descending sorted list based on the following two rules:
    # 1. Each name's score is the sum of each letter's position in the alphabet (e.g.: a=1, b=2, c=3, etc.)
    # 2. For names with identical scores, each name is ordered based on the score of the first letter (cx, then by, then az, etc.)
    
    if names.count(names[0])==len(names): return names # If all names are the same, return the list
    names=sorted(names,reverse=True) # Sort the name list reverse alphabetically; sets up for rule #2 above
    letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        
    # Intiate lists for appending
    scorelist = list()
        
    # Loop through the name list; score
    for a in names:
        temp=0
        if len(a)>0:
            for char in a:
                temp+=letters.index(char)+1
        scorelist.append(temp)
        
    # Zip score and name lists, sort by score list; reverse alphabetical sorting is preserved from first sorting
    final = [names for (scorelist, names) in sorted(zip(scorelist,names),key=lambda thing:thing[0],reverse=True)]
        
    return final