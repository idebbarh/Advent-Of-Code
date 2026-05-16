#include <alloca.h>
#include <stddef.h>
#include <stdio.h>
#include <string.h>
#include "../utils/hash_table.c"


#define MAX_CITIES 10

typedef struct {
    char from[64];
    char to[64];
    int distance;
} Route;


int is_visited(char* visited[100], char* target_city){
    for(size_t i = 0; i < 100; i++){
        char* vis_city = visited[i];

        if(vis_city == NULL || target_city == NULL) continue;

        if(strcmp(target_city, vis_city) == 0){
            return 1;
        }
    }

    return 0;
}


int get_route_distance(char* from, char* to, ht_hash_table* distances){
    char* from_to = malloc(strlen(from) + strlen(to) + 2);

    strcpy(from_to, from);
    strcat(from_to, ",");
    strcat(from_to, to);

    char* distance_str = ht_search(distances, from_to);
    char* end;
    int distance = strtol(distance_str, &end, 10);

    if(end == distance_str || *end != '\0') return -1;

    free(from_to);

    return distance;
}

void split(char* str, char* sep, char* tokens[MAX_CITIES]){
    char* token = strtok(str, sep);
    size_t count = 0;

    while(token != NULL){
        tokens[count++] = token;
        token = strtok(NULL, sep);
    }
}

int find_longest_distance(ht_hash_table* distances, ht_hash_table* graph, char* curr_from, int total_distance, char* visited[100], int visited_count, int total_cities){
    char* curr_to_raw = ht_search(graph, curr_from);

    if(visited_count >= total_cities) return total_distance;


    if(curr_to_raw == NULL) return -1;


    char* cities[MAX_CITIES] = {NULL};

    char curr_to[256];
    strncpy(curr_to, curr_to_raw, sizeof(curr_to) - 1);  // copy to stack
    curr_to[sizeof(curr_to) - 1] = '\0';

    split(curr_to, ",", cities);

    int longest_distance = -1;

    for(size_t i = 0; i < MAX_CITIES; i++){
        char* next_from = cities[i];

        if(next_from == NULL) continue;

        int distance = get_route_distance(curr_from, next_from, distances);

        if(distance == -1 || is_visited(visited, next_from)) continue;

        visited[visited_count] = next_from;

        int res = find_longest_distance(distances, graph, next_from, total_distance + distance, visited, visited_count+1, total_cities);

        visited[visited_count] = NULL;

        if(res >= 0 && (res > longest_distance)){
            longest_distance = res;
        }
    }

    return longest_distance;

}

int parse_route(Route* route, const char* line){
    int matches = sscanf(line, "%63s to %63s = %d", route->from, route->to, &route->distance);

    if(matches == 3) return 1;

    return 0;
}


void connect_cities(ht_hash_table* distances, ht_hash_table* graph, char* from, char* to, int distance, char* visited[100], int* total_cities){
    char* prev_to = ht_search(graph, from);

    if(!is_visited(visited, from)){
        visited[(*total_cities)++] = strdup(from);
    }

    if(!is_visited(visited, to)){
        visited[(*total_cities)++] = strdup(to);
    }

    if(prev_to != NULL){
        int new_to_size = strlen(prev_to) + strlen(to) + 2;
        char* new_to = malloc(new_to_size);

        if (new_to){
            strcpy(new_to, prev_to);
            strcat(new_to,",");
            strcat(new_to,to);

            ht_insert(graph, from, new_to);
            free(new_to);
        }
    }else {
      ht_insert(graph, from, to);
    }

    int from_to_size = strlen(from) + strlen(to) + 2;
    char* from_to = malloc(from_to_size);

    if(from_to){
        char distance_char[20];
        sprintf(distance_char, "%d", distance);

        strcpy(from_to, from);
        strcat(from_to, ",");
        strcat(from_to, to);

        ht_insert(distances, from_to, distance_char);
        free(from_to);
    }

}

void build_graph(ht_hash_table* distances, ht_hash_table* graph, char* line, char* visited[100], int* total_cities){
    Route route;

    if (parse_route(&route, line)) {
        connect_cities(distances, graph, route.from, route.to, route.distance, visited, total_cities);
        connect_cities(distances, graph, route.to, route.from, route.distance, visited, total_cities);
    } 
}


int main(){
    FILE *file = fopen("real_input.txt","r");


    if(file == NULL){
        printf("ERROR: Could not open the file. Does it exist?\n");
        return 1;
    }


    char buffer[256];


    ht_hash_table* graph = ht_new();
    ht_hash_table* distances = ht_new();
    

    char* cities[100] = {NULL};
    int total_cities = 0;

    while(fgets(buffer,sizeof(buffer),file) != NULL){
        buffer[strcspn(buffer, "\n")] = '\0';
        build_graph(distances, graph, buffer, cities, &total_cities);
    }


    int longest_distance = -1;

    for(int i = 0; i < total_cities; i++){
        if(cities[i] != NULL){
            char* visited[100] = {NULL};

            visited[0] = cities[i]; 

            int res = find_longest_distance(distances, graph, cities[i], 0, visited, 1, total_cities);

            if(res > longest_distance) {
                longest_distance = res;
            }

            free(cities[i]);
        }
    }


    printf("The longest distance is: %d\n", longest_distance);

    fclose(file);

    ht_delete_hash_table(graph);
    ht_delete_hash_table(distances);

    return 0;
}


