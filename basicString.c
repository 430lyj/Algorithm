#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool solution(const char* s) {
    bool answer = true;
    int length = strlen(s);
    int counter = 0;
    if(length == 4 || length == 6) {
        for(int i = 0; i < length; i++){
            if(48<= s[i] && s[i] <= 57) counter++;
        }
        if(counter == length) answer = true;
        else answer = false;
    }
    return answer;
}

int main(void){
    char* s = malloc(sizeof(char*));
    printf("Input string : ");
    scanf("%s", s);
    while(strlen(s) < 1 || strlen(s) > 8){
        return -9999;
    }
    printf("%d\n", solution(s));
}
