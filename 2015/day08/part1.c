#include <stddef.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int is_hex_char(char c) {
    return isxdigit((unsigned char)c);
}

int get_chars_in_memory(char *line){
    int res = 0;
    size_t line_size = strlen(line);

    if(line_size <= 2) return 0; 

    for(size_t i = 1; i < line_size - 1; i++){
        if(line[i] != '\\' || i == line_size - 2) {
            res++;
            continue;
        }

        char next_char = line[i+1];

        if(next_char == '\\' || next_char  == '"') {
            i++;
        }else if(next_char == 'x' && i + 3 < line_size - 1){
            char next_next_char = line[i+2];
            char next_next_next_char = line[i+3];

            if(is_hex_char(next_next_char) && is_hex_char(next_next_next_char)){
              i+=3;
            }
        }

        res++;

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

    int char_of_code_count = 0;
    int char_in_memory_count = 0;

    while(fgets(buffer,sizeof(buffer),file) != NULL){
        buffer[strcspn(buffer, "\n")] = '\0';
        char_of_code_count+=strlen(buffer);
        char_in_memory_count+=get_chars_in_memory(buffer);
    }

    fclose(file);
    printf("The result is: %d\n", char_of_code_count - char_in_memory_count);
    return 0;
}


