input = open("real-input.txt","r").read()

def solution():
    l,r = 0,0
    res = 0

    while r < len(input):
        current = input[l:r+1]

        if current == "mul":
            start_index = r+1
            open = input[start_index]
            start_index+=1
            n1="" 

            while input[start_index].isdigit(): 
                n1+=input[start_index]
                start_index+=1

            s = input[start_index]
            start_index+=1
            n2= ""

            while input[start_index].isdigit(): 
                n2+=input[start_index]
                start_index+=1

            close = input[start_index]

            if open == "(" and close == ")" and s == ",":
                res+=(int(n1)*int(n2))

            r+=1
            l=r
        elif current in "mul":
            r+=1
        else:
            l+=1
            if l >= r:
                r=l

    return res

print("solution: ",solution())






    
    








