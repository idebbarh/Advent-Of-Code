#include <stddef.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>


bool is_evil(const char *str,const char *evil_str){
    const char *start = evil_str;

    while(*str != '\0' && *start != '\0') {
        if(*str == *start){ 
            start++;
        }else {
            start = evil_str;
        };

        str++;
    }

    return *start == '\0';
}

bool contains_vowels(char *str,size_t count) {
    char *vowels = "aeiou";
    size_t vc = 0;

    while(*str != '\0' && vc < count){
        if(strchr(vowels,*str) != NULL) vc++;
        str++;
    }

    return vc >= count;
}

bool contains_char_twice_in_row(char *str){
    size_t i = 0;
    size_t str_len = strlen(str);

    while(i < str_len - 1){
        if(str[i] == str[i+1]) break;
        i++;
    }

    return i < str_len - 1;
}


bool is_nice(char *str){
    if(!contains_vowels(str,3)){
        return false;
    };

    if(!contains_char_twice_in_row(str)){ 
        return false;
    };

    char *evil_list[] = {"ab", "cd", "pq", "xy"};
    size_t n = sizeof(evil_list) / sizeof(evil_list[0]);

    for(size_t i = 0; i < n; i++){
        if(is_evil(str,evil_list[i])){ 
            return false;
        }
    }

    return true;
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

