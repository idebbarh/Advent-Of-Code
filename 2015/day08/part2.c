#include <stddef.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int is_hex_char(char c) {
    return isxdigit((unsigned char)c);
}

int get_chars_of_code_incoded(char *line){
    size_t line_size = strlen(line);
    int res = 4;

    if(line_size <= 2) return res; 

    for(size_t i = 1; i < line_size - 1; i++){
        if(line[i] == '\\' || line[i] == '"') {
            res++;
        }
    }

    return res;
}

int main(){
    FILE *file = fopen("real_input.txt","r");


    if(file == NULL){
        printf("ERROR: Could not open the file. Does it exist?\n");
        return 1;
    }


    char buffer[256];

    int char_of_code_count_incoded = 0;

    while(fgets(buffer,sizeof(buffer),file) != NULL){
        buffer[strcspn(buffer, "\n")] = '\0';
        char_of_code_count_incoded+=get_chars_of_code_incoded(buffer);
    }

    fclose(file);
    printf("The result is: %d\n", char_of_code_count_incoded);
    return 0;
}


