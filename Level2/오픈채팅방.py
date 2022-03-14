def solution(record):
    user = {}
    user_log = [] #유저들의 입 퇴장 정보 저장배열
    answer = []
    for i in range(len(record)):

        user_info = record[i].split()



        #유저의 상태에 따라 문구 생성
        if user_info[0] == 'Enter':
            user_log.append(user_info[1])
            answer.append('님이 들어왔습니다.' )

            # uid와 닉네임 정보를 딕셔너리에 저장
            user[user_info[1]] = user_info[2]

        elif user_info[0] == 'Leave':
            user_log.append(user_info[1])
            answer.append('님이 나갔습니다.')
        elif user_info[0] == 'Change':
            user[user_info[1]] = user_info[2]

    for i in range(len(user_log)):
        answer[i] = user[user_log[i]] + answer[i]

    return answer



case1 = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(case1))