def solution(x, n):
    answer = []
    temp = x
    for i in range(1, n + 1):
      answer.append(temp)
      temp += x
    return answer