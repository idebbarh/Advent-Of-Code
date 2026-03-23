#include <errno.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h> 


long string_to_num(char *str,int *success){
    char *endptr;
    long num;

    errno = 0;
    num = strtol(str, &endptr, 10);

    if(endptr == str || *endptr != '\0' || errno == ERANGE){
        *success = 0;
        fprintf(stderr, "Error: Conversion failed or out of range.\n");
        return 0;
    }else {
        *success = 1;
        return num;
    }
}

//2*l*w + 2*w*h + 2*h*l + s1*s2;
long get_total_feet_of_ribbon(char *line){
    int nc = 0;
    int vc = 0;
    char current_value[100];
    char *str_values[3] = {NULL, NULL, NULL}; 

    while(*line != '\0' && *line != '\n' && vc < 3){
        if(*line == 'x'){
            current_value[nc] = '\0';
            str_values[vc] = malloc(strlen(current_value)+1);
            strcpy(str_values[vc], current_value);

            vc++;
            nc = 0;
        }else {
            current_value[nc++] = *line;
        }

        line++;
    } 

    if(nc > 0 && vc < 3){
        current_value[nc] = '\0';
        str_values[vc] = malloc(strlen(current_value)+1);
        strcpy(str_values[vc],current_value);
    }


    int rows = sizeof(str_values) / sizeof(str_values[0]);

    long num_values[3];
    int cs;
    long num;

    for (size_t i = 0; i < rows; ++i){
        char *str = str_values[i];

        num = string_to_num(str,&cs);

        if(str_values[i]){
            free(str_values[i]);
        }

        if(cs){
            num_values[i] = num;
        }else {
            printf("Conversion failed\n");
            return 0;
        }

    }

    long l = num_values[0];
    long w = num_values[1];
    long h = num_values[2];

    long s1 = 0;
    long s2 = 0;

    if(l >= w && l >= h){
        s1 = w;
        s2 = h;
    }else if(w >= l && w >=h){
        s1 = l;
        s2 = h;
    }else if(h >= l && h >= w){
        s1 = l;
        s2 = w;
    }

    return l*w*h + (s1*2)+(s2*2);
}


int main(){
    FILE *file = fopen("real_input.txt","r");

    if(file == NULL){
        printf("ERROR: Could not open the file. Does it exist?\n");
        return 1;
    }

    char buffer[256];

    long result = 0;

    while(fgets(buffer,sizeof(buffer),file) != NULL){
       result+=get_total_feet_of_ribbon(buffer);
    }

    printf("The total square feet of wrapping paper: %ld\n",result);

    fclose(file);

    return 0;
};

