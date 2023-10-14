input = open("input.txt","r").read()
windowL = 14
window = {}
mostAppear = ["",0]

for c in input[:windowL] :
    if c not in window :
        window[c] = 0
    window[c]+=1
    if window[c] > mostAppear[1] :
        mostAppear[0] = c
        mostAppear[1] = window[c]

def main():
    l=0
    r=l+windowL-1
    while r < len(input):
        if mostAppear[1] == 1 : return r+1        
        window[input[l]]-=1
        l+=1
        r+=1
        if input[r] not in window :
            window[input[r]]=0
        window[input[r]]+=1
        mostAppear[1] = window[mostAppear[0]]
        for c in input[l:r+1]:
            if window[c] > mostAppear[1] :
                mostAppear[1] = window[c]
                mostAppear[0] = c
                

print(main())
            
        



    

