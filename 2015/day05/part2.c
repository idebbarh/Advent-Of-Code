#include <stddef.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>


bool has_frule(const char *str){
    size_t str_len = strlen(str);

    for(size_t i = 0; i < str_len; i++){
        for(size_t j = i+2; j < str_len - 1; j++){
            if(str[i] == str[j] && str[i + 1] == str[j + 1]){
                return true;
            }
        }
    }

    return false;
}


bool has_srule(const char *str) {
    size_t str_len = strlen(str);

    for(size_t i = 1; i < str_len - 1; i++){
        if(str[i-1] == str[i+1]){
            return true;
        }
    }

    return false;
}


bool is_nice(char *str){
    return has_frule(str) && has_srule(str);
};



int main(){
    FILE *file = fopen("real_input.txt","r");


    if(file == NULL){
        printf("ERROR: Could not open the file. Does it exist?\n");
        return 1;
    }


    char buffer[256];

    int result = 0;


    while(fgets(buffer,sizeof(buffer),file) != NULL){
        buffer[strcspn(buffer, "\n")] = '\0';

        if(is_nice(buffer)) {
            result++;
        }
    }

    printf("The nice total is: %d\n",result);

    return 0;
};

