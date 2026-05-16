#include <stdbool.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../utils/hash_table.c"

void int_to_str(int number, char *buffer, int size) {
    snprintf(buffer, size, "%d", number);
}

int str_to_int(const char *str, int *result) {
    char *endptr;

    long value = strtol(str, &endptr, 10);

    /* invalid characters found */
    if (*endptr != '\0') {
        return 0;
    }

    *result = (int)value;

    return 1;
}

int is_number(const char *s) {

    char *endptr;

    strtol(s, &endptr, 10);

    return *endptr == '\0';
}

void parse_line(char *line, char *parts[5]){
    char cur = *line;
    char part[100];
    int char_index = 0;
    int part_index = 0;

    while(cur != '\0'){
        if(cur == ' '){
            part[char_index] = '\0';

            if(strcmp(part,"->") != 0){
                parts[part_index] = malloc(strlen(part)+1);
                strcpy(parts[part_index],part);
                part_index++;
            }

            char_index = 0;
        }else{
            part[char_index++] = cur;
        }

        line++;
        cur = *line;
    }

    part[char_index] = '\0';

    if(part_index != 4 && strcmp(part,"->") != 0){
        parts[part_index] = malloc(strlen(part)+1);
        strcpy(parts[part_index],part);
        part_index++;
    }
}

int get_value(char* target, char** lines[339], ht_hash_table* ht){
    char *lookup = ht_search(ht, target);

    if(lookup != NULL){
        if(is_number(lookup)){
            int number;
            if(str_to_int(lookup, &number)){
                return number;
            }
        }
    };

    for(size_t i = 0; i < 339; i++){
        char **line = lines[i];
        char **cur = line;
        size_t line_size = 0;

        while(*cur != NULL){
            cur++;
            line_size++;
        }

        char *key = line[line_size-1];
        int number;


        if(strcmp(target, key) == 0){
            /* printf("%s->",target); */
            int return_value = 0;
            if(line_size == 2){
                if(is_number(line[0])){
                    if(str_to_int(line[0], &number)){
                        return_value =  number;
                    }
                }else{
                    return_value = get_value(line[0],lines,ht);
                }
            }else if(line_size == 3){
                if(is_number(line[1])){
                    if(str_to_int(line[1], &number)){
                        return_value = ~number;
                    }
                }else {
                    return_value = ~get_value(line[1],lines,ht);
                }
            }else if(line_size == 4){
                char *op = line[1];
                int n1;
                int n2;
                int left_n = 0;
                int right_n = 0;

                if(is_number(line[0])){
                    if(str_to_int(line[0],&n1)){
                        left_n = n1;
                    }
                }else {
                    left_n = get_value(line[0], lines,ht);
                }


                if(is_number(line[2])){
                    if(str_to_int(line[2],&n2)){
                        right_n = n2;
                    }
                }else {
                    right_n = get_value(line[2], lines,ht);
                }

                if(strcmp(op,"AND") == 0){
                    return_value =  left_n & right_n;
                }


                if(strcmp(op,"OR") == 0){
                    return_value = left_n | right_n;
                }


                if(strcmp(op,"LSHIFT") == 0){
                    return_value =  left_n << right_n;
                }


                if(strcmp(op,"RSHIFT") == 0){
                    return_value =  left_n >> right_n;
                }

            }

            char buffer[20];

            snprintf(buffer, sizeof(buffer), "%d", return_value);

            ht_insert(ht, target, buffer);

            return return_value;
        }
    }
    return 0;
}



int main(){
    FILE *file = fopen("real_input.txt","r");

    if(file == NULL){
        printf("ERROR: Could not open the file. Does it exist?\n");
        return 1;
    }

    char buffer[256];

    ht_hash_table* ht = ht_new();

    char **parsed_lines[339] = {NULL};
    int line_index = 0;

    while(fgets(buffer,sizeof(buffer),file) != NULL){
        char **parts = calloc(5, sizeof(char *));
        buffer[strcspn(buffer, "\n")] = '\0';
        parse_line(buffer,parts);
        parsed_lines[line_index++] = parts;
    }

    int v = get_value("a",parsed_lines,ht);

    printf("the wire a value is: %d",v);

    return 0;
};

