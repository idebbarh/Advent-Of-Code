#include <stdbool.h>
#include <stddef.h>
#include <stdio.h>
#include <string.h>
#include "hash_table.c"



int main(){
    FILE *file = fopen("real_input.txt","r");

    ht_hash_table* ht = ht_new();
    ht_del_hash_table(ht);

    if(file == NULL){
        printf("ERROR: Could not open the file. Does it exist?\n");
        return 1;
    }

    char buffer[256];

    while(fgets(buffer,sizeof(buffer),file) != NULL){
        buffer[strcspn(buffer, "\n")] = '\0';
    }

    return 0;
};

