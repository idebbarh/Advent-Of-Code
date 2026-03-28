#include <stdbool.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

#define ROWS 1000
#define COLS 1000

int toggle(int state) {
    return state ^ 1;
}

int off(int state) {
    return state & 0;
}

int on(int state){
    return state | 1;
}

long string_to_num(char *str){
    char *endptr;
    long num;

    errno = 0;
    num = strtol(str, &endptr, 10);

    if(endptr == str || *endptr != '\0' || errno == ERANGE){
        fprintf(stderr, "Error: Conversion failed or out of range.\n");
        return 0;
    }else {
        return num;
    }
}

void get_pos(char *str_pair, int *x, int *y) {
    int left_size = 0;
    int right_size = 0;

    char *cur = str_pair;

    bool pass_middle = false;

    while(*cur != '\0') {
        if(*cur == ','){
            pass_middle = true;
        }else {
            if(!pass_middle){
                left_size++;
            }else{
                right_size++;
            }
        }
        cur++;
    }

    char *left_val = malloc(left_size + 1);
    memcpy(left_val, str_pair, left_size);
    left_val[left_size] = '\0';

    char *right_val = malloc(right_size + 1);
    memcpy(right_val, str_pair + left_size + 1, right_size);
    right_val[right_size] = '\0';

    *x = string_to_num(right_val);
    *y = string_to_num(left_val);

    free(left_val);
    free(right_val);
}

void apply_instruction(char *instruction,int *grid){
    char *ins_parts[5] = {NULL,NULL,NULL,NULL,NULL};
    size_t pi = 0;

    for(size_t i = 0; instruction[i] != '\0'; i++){
        if(instruction[i] == ' ') continue;

        size_t j = i;
        while(instruction[j] != ' ' && instruction[j] != '\0') j++;

        if(i == j) continue;

        if(pi < 5) {
            size_t len = j - i;

            ins_parts[pi] = malloc(len + 1); 
            if(!ins_parts[pi]) break;

            memcpy(ins_parts[pi], instruction + i, len);
            ins_parts[pi][len] = '\0';

            pi++;
        };

        i = j - 1;
        
        if(instruction[j] == '\0' || pi >= 5) break;
    }

    char *finst = ins_parts[0];

    int x1, y1, x2, y2; 

    char *fpair;
    char *spair;

    int(* op_func)(int);

    if(finst != NULL){ 
        if(strcmp(finst,"toggle") == '\0'){
            fpair = ins_parts[1];
            spair = ins_parts[3];
            op_func = &toggle;

        }else if(strcmp(finst,"turn") == '\0'){
            char *sinst = ins_parts[1];

            if(sinst != NULL){
                fpair = ins_parts[2];
                spair = ins_parts[4];

                if(strcmp(sinst,"on") == '\0'){
                    op_func = &on;
                }else if(strcmp(sinst,"off") == '\0'){
                    op_func = &off;
                }
            }
        }

        get_pos(fpair, &x1, &y1);
        get_pos(spair, &x2, &y2);

        for(size_t row = y1; row <= y2; row++){
            for(size_t col = x1; col <= x2; col++){
                int state = grid[row * COLS + col];
                grid[row * COLS + col] = op_func(state);
            }
        }

        free(ins_parts[0]);
        free(ins_parts[1]);
        free(ins_parts[2]);
        free(ins_parts[3]);

        if(ins_parts[4]){
            free(ins_parts[4]);
        }
    }
}

int main(){
    FILE *file = fopen("real_input.txt","r");

    if(file == NULL){
        printf("ERROR: Could not open the file. Does it exist?\n");
        return 1;
    }

    char buffer[256];
    int result = 0;
    int *grid = calloc(ROWS * COLS, sizeof(int));

    while(fgets(buffer,sizeof(buffer),file) != NULL){
        buffer[strcspn(buffer, "\n")] = '\0';
        apply_instruction(buffer, grid);
    }


    for(size_t row = 0; row < ROWS; row++){
        for(size_t col = 0; col < COLS; col++){
            result+=(grid[row * COLS + col]);
        }
    }

    printf("The result is: %d\n",result);

    free(grid);

    return 0;
};

