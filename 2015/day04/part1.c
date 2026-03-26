#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>



char *concat(char *str1, char *str2) {
    size_t len1 = strlen(str1);
    size_t len2 = strlen(str2);

    char *concated = malloc(len1+len2+1);

    if (!concated) return NULL;

    memcpy(concated,str1,len1);
    memcpy(concated + len1,str2,len2 + 1);

    return concated;
}

char *size_t_to_str(size_t n) {
    char *str = malloc(32);

    if (!str) return NULL;

    snprintf(str, 32, "%zu", n);

    return str;
}



uint8_t *pad_message(const uint8_t *message, size_t len,size_t *nl){
    size_t new_len = len+1;

    while(new_len % 64 != 56){
        new_len++;
    }

    uint8_t *buffer = malloc(new_len + 8);

    if (!buffer) return NULL;

    memcpy(buffer,message,len);

    size_t i = len;

    buffer[i++] = 0x80;

    while(i < new_len){
        buffer[i++] = 0x00;
    }

    uint64_t bit_len = len * 8;

    for (int j = 0; j < 8; j++) {
        buffer[i++] = (bit_len >> (8 * j)) & 0xFF;
    }

    *nl = new_len + 8;

    return buffer;
}


uint8_t* MD5(const uint8_t *message,size_t len){
    int s[64];
    uint32_t K[64];


    int r1[] = { 7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22 };
    int r2[] = { 5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20 };
    int r3[] = { 4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23 };
    int r4[] = { 6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21 };


    size_t j = 0;

    for(size_t i = 0; i < 64; i++){
        if(i <= 15) {
            s[i] = r1[j++];
        }else if(i <= 31){
            s[i] = r2[j++];
        }else if(i <= 47){
            s[i] = r3[j++];
        }else if(i <= 63){
            s[i] = r4[j++];
        }else {
            break;
        }

        if(j >= 16) {
            j = 0;
        }
    }


    for (size_t i = 0; i < 64; i++){
        K[i] = floor(4294967296.0 * fabs(sin(i + 1))); 
    }

     uint32_t a0 = 0x67452301;
     uint32_t b0 = 0xefcdab89;
     uint32_t c0 = 0x98badcfe;
     uint32_t d0 = 0x10325476;

    size_t new_len;

    uint8_t *buffer = pad_message(message, len, &new_len);

    for(size_t i = 0; i < (new_len / 64); i++){
        uint8_t *chunk = buffer + (i * 64);

        uint32_t A = a0, B = b0, C = c0, D = d0;

        uint32_t M[16];

        for (int j = 0; j < 16; j++) {
            M[j] = (uint32_t)chunk[j*4] |
                   ((uint32_t)chunk[j*4+1] << 8) |
                   ((uint32_t)chunk[j*4+2] << 16) |
                   ((uint32_t)chunk[j*4+3] << 24);
        }

        for(size_t k = 0; k < 64; k++){
            uint32_t F, g;

            if (k <= 15){
                F = (B & C) | (~B & D);
                g = k;
            }
            else if (k <= 31){
                F = (D & B) | (~D & C);
                g = (5*k + 1) % 16;
            }
            else if (k <= 47){ 
                F = B ^ C ^ D;
                g = (3*k + 5) % 16;
            }
            else {
                F = C ^ (B | ~D);
                g = (7*k) % 16;
            }

            F = F + A + K[k] + M[g];

            A = D;
            D = C;
            C = B;
            B = B + ((F << s[k]) | (F >> (32 - s[k])));
        }

        a0 += A;
        b0 += B;
        c0 += C;
        d0 += D;
    }

    uint8_t *digest = malloc(16);

    uint32_t words[4] = {a0, b0, c0, d0};

    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            digest[i*4 + j] = (words[i] >> (8 * j)) & 0xFF;
        }
    }


    free(buffer);

    return digest;
}


int main(){
    char base_input[] = "iwrupvqb";
    size_t result = 0;

    uint8_t *hash;
    char *lpn;
    char *final_input;

    while(1){
        lpn = size_t_to_str(result);
        final_input = concat(base_input,lpn); 
        hash = MD5((const uint8_t *)final_input,strlen(final_input));

        printf("The hashed value of '%s' is ", final_input);
        for (int i = 0; i < 16; i++) {
            printf("%02x", hash[i]);
        }
        printf("\n");

        if(hash[0] == 0x00 && hash[1] == 0x00 && (hash[2] & 0xF0) == 0x00) break;

        result++;
    }


    printf("The million dollar answer is: %ld\n",result);

    free(hash);
    free(lpn);
    free(final_input);
};

