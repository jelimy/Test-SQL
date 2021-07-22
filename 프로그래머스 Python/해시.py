# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

# 코딩테스트 연습 > 해시 > 전화번호 목록 (level2)
# 사용언어 Python3

# 1차 답안 >> 오답 (효율성 테스트 시간초과)
def solution(phone_book):
    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if i != j and phone_book[i] == phone_book[j][:len(phone_book[i])]:
                return False
    return True
# for문과 if문이 중첩되어 시간 복잡도가 증가

# 2차 답안 >> 정답
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    return True
# 시도 : 문자열이라는 특성을 이용해 sort()로 앞, 뒤의 값만 비교할 수 있도록 했다. 이를 통해 for문의 중첩을 막을 수 있었다.


