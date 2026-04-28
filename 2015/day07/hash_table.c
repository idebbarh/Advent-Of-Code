#include <math.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include "hash_table.h"
#include "prime.c"

static ht_item HT_DELETED_ITEM = {NULL, NULL};

static void ht_resize(ht_hash_table* ht, const int base_size);

static ht_item* ht_new_item(const char* k, const char* v){
    ht_item* i = malloc(sizeof(ht_item));

    i->key = strdup(k);
    i->value = strdup(v);
    
    return i;
}

ht_hash_table* ht_new_sized(const int base_size){
    ht_hash_table* ht = malloc(sizeof(ht_hash_table));

    ht->base_size = base_size;
    ht->size = next_prime(ht->size);
    ht->count = 0;
    ht->items = calloc((size_t)ht->size, sizeof(ht_item*));

    return ht;
}

ht_hash_table* ht_new(){
    return ht_new_sized(HT_INITIAL_BASE_SIZE);
}


static void ht_delete_item(ht_item* i){
    free(i->key);
    free(i->value);
    free(i);
}

void ht_delete_hash_table(ht_hash_table* ht){
    for(size_t i = 0; i < ht->size; i++){
        ht_item* item = ht->items[i];

        if(item != NULL) {
            ht_delete_item(item);
        }
    }

    free(ht->items);
    free(ht);
} 

static int ht_hash(const char* s, const int a, const int m){
    long hash = 0;
    const int len_s = strlen(s);

    for(size_t i = 0; i < len_s; i++){
        hash += (long)pow(a, len_s - (i+1)) * s[i];
        hash = hash % m;
    }

    return (int)hash;
}

static int ht_get_hash(const char* s, const int num_buckets, const int attemps){
    const int hash_a = ht_hash(s, HT_PRIME_1, num_buckets);
    const int hash_b = ht_hash(s, HT_PRIME_2, num_buckets);

    return (hash_a + (attemps * (hash_b + 1))) % num_buckets;
}


static void ht_resize_up(ht_hash_table* ht){
    const int new_size = ht->base_size * 2;
    ht_resize(ht, new_size);
}


static void ht_resize_down(ht_hash_table* ht){
    const int new_size = ht->base_size / 2;
    ht_resize(ht, new_size);
}

void ht_insert(ht_hash_table* ht, const char* key, const char* value){
    const int load = ht->count * 100 / ht->size;

    if(load > 70){
        ht_resize_up(ht);
    }

    ht_item* item = ht_new_item(key, value);
    int index = ht_get_hash(item->key, ht->size, 0);

    ht_item* cur_item = ht->items[index];
    int attemps = 1;

    bool dup = strcmp(cur_item->key, key) == 0;

    while(cur_item != NULL && cur_item != &HT_DELETED_ITEM && !dup){
        index = ht_get_hash(item->key, ht->size, attemps++);
        cur_item = ht->items[index];
        dup = strcmp(cur_item->key, key) != 0;
    }

    if(dup){
        ht_delete_item(cur_item);
    }

    ht->items[index] = item;
    ht->count++;
}

char* ht_search(ht_hash_table* ht, const char* key){
    int index = ht_get_hash(key, ht->size, 0);
    ht_item* item = ht->items[index];
    int attemps = 1;

    while(item != NULL){
        if(item != &HT_DELETED_ITEM){
            if(strcmp(key, item->key) == 0){
                return item->value;
            }
        }

        index = ht_get_hash(key, ht->size, attemps++);
        item = ht->items[index];
    }

    return NULL;
}

void ht_delete(ht_hash_table* ht, const char* key){
    int index = ht_get_hash(key, ht->size, 0);
    ht_item* item = ht->items[index];
    int attemps = 1;

    const int load = ht->size * 100 / ht->size;

    if(load < 10) {
        ht_resize_down(ht);
    }

    while(item != NULL){
        if (item != &HT_DELETED_ITEM) {
            if(strcmp(key, item->key) == 0){
                 ht_delete_item(item);
                 ht->items[index] = &HT_DELETED_ITEM;
                 ht->count--;
                 return; 
            }
        }

        index = ht_get_hash(key, ht->size, attemps++);
        item = ht->items[index];
    }
}



static void ht_resize(ht_hash_table* ht, const int base_size) {
    if(base_size < HT_INITIAL_BASE_SIZE) {
        return;
    }

    ht_hash_table* new_ht = ht_new_sized(base_size);

    for(size_t i = 0; i < ht->size; i++){
        ht_item* cur_item = ht->items[i];

        if(cur_item != NULL && cur_item != &HT_DELETED_ITEM){
            ht_insert(new_ht, cur_item->key, cur_item->value);
        }
    }


    ht->base_size = new_ht->base_size;
    ht->count = new_ht->count;

    const int tmp_size = ht->size;
    ht->size = new_ht->size;
    new_ht->size = tmp_size;


    ht_item** tmp_items = ht->items;
    ht->items = new_ht->items;
    new_ht->items = tmp_items;

    ht_delete_hash_table(new_ht);
}


