#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
bool solution(const char* s) {
    bool answer = true;
    int length = strlen(s);
    int counter = 0;
    if(length == 4 || length == 6) {
        for(int i = 0; i < length; i++){
            if(isdigit(s[i]) != 0) counter++;
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
//출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
