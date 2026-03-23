#include <stddef.h>
#include <stdio.h>
#include <string.h>

int decode_instructions(const char *str,int *floor){
    size_t count = 1;
    int local_floor = *floor;

    while(*str != '\0'){
        switch (*str) {
            case '(':
                local_floor++;
                break;
            case ')':
                local_floor--;
                break;
            default:
                break;
        }


        if(local_floor < 0){
            return count;
        }

        str++;
        count++;
    }


    *floor = local_floor;

    return 0;
};



int main(){
    FILE *file = fopen("real_input.txt","r");

    if(file == NULL){
        printf("ERROR: Could not open the file. Does it exist?\n");
        return 1;
    }

    char buffer[256];

    int floor = 0;
    int position = 0;
    int result = 0;

    while(fgets(buffer,sizeof(buffer),file) != NULL && position == 0){
       position = decode_instructions(buffer,&floor);

        if(position == 0){
           result+=(strlen(buffer));
        }
    }

    printf("The position is: %d\n",result+position);

    fclose(file);

    return 0;
};
