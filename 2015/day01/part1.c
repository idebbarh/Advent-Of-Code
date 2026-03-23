#include <stdio.h>
#include <string.h>

int decode_instructions(const char *str){
    int floor = 0;


    while(*str != '\0'){
        switch (*str) {
            case '(':
                floor++;
                break;
            case ')':
                floor--;
                break;
            default:
                break;
        }

        str++;
    }


    return floor;
};



int main(){
    FILE *file = fopen("real_input.txt","r");


    if(file == NULL){
        printf("ERROR: Could not open the file. Does it exist?\n");
        return 1;
    }


    char buffer[256];


    printf("--- File Contents ---\n");

    int result = 0;


    while(fgets(buffer,sizeof(buffer),file) != NULL){
        result+=decode_instructions(buffer);
    }

    printf("The floor is: %d\n",result);

    return 0;
};

