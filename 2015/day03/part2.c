#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>

int compare( const void* a, const void* b)
{
     int int_a = * ( (int*) a );
     int int_b = * ( (int*) b );
     
     if ( int_a == int_b ) return 0;
     else if ( int_a < int_b ) return -1;
     else return 1;
}


long map_to_natural(int n) {
    return (n >= 0) ? (2L * n) : (2L * -n - 1);
}

unsigned long get_truly_unique_index(int x, int y) {
    // Transform x and y to be non-negative
    unsigned long nx = map_to_natural(x);
    unsigned long ny = map_to_natural(y);
    
    // Apply Cantor Pairing Function
    return (nx + ny) * (nx + ny + 1) / 2 + ny;
}


void traverse(int *x, int *y,char dir){
    switch(dir){
        case '^':
            ++*y;
            break;
        case '>':
            ++*x;
            break;
        case 'v':
            --*y;
            break;
        case '<':
            --*x;
            break;
        default:
            break;
    }
}

int main(){
    FILE *file = fopen("real_input.txt","r");

    if(file == NULL){
        printf("ERROR: Could not open the file. Does it exist?\n");
        return 1;
    }

    int c; 
    long n = 0;

    while ((c = fgetc(file)) != EOF) {
        if(c == '^' || c == '>' || c == 'v' || c == '<'){
            n++;
        }
    }

    rewind(file);

    long *marks = calloc(n, sizeof(*marks));

    int x = 0;
    int y = 0;
    int x2 = 0;
    int y2 = 0;

    long pos;
    size_t index = 0;

    while ((c = fgetc(file)) != EOF) {
        if(c == '^' || c == '>' || c == 'v' || c == '<'){
            if(index % 2 == 0){
                traverse(&x, &y, c);
                pos = get_truly_unique_index(x,y);
            }else {
                traverse(&x2, &y2, c);
                pos = get_truly_unique_index(x2,y2);
            }

            marks[index++] = pos;
        }
    }

    qsort(marks, n, sizeof(*marks), compare);

    int result = 0;
    int prev;
    size_t i = 0;

    while(i < n){
        result++;
        prev = marks[i];

        while(i < n && marks[i] == prev){
            i++;
        }
    }

    if(marks[i-1] != prev) result++;

    free(marks);
    fclose(file);

    return 0;
};
