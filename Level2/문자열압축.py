import math
def solution(s):

    answer = ''

    resArr=[]
    for i in range(0,int(len(s)/2)+1):
        count = 1
        skey = ''
        sres = ''

        for j in range(0, math.ceil(len(s)/(i+1))):
            sindex = j * (i+1)
            lindex = (j + 1) * (i+1)
            if skey == '':
                skey = s[sindex:lindex]
            else:
                if s[sindex:lindex] == skey:
                    count+=1
                else:

                    if count == 1:
                        sres += skey
                    else:
                        sres += str(count) + skey
                    count = 1
                    skey = s[sindex:lindex]

            if j >= math.ceil(len(s)/(i+1))-1 and skey!='':
                if count == 1:
                    sres += skey
                else:
                    sres += str(count) + skey
        print(sres)
        resArr.append(len(sres))

    answer = min(resArr)
    return answer

text = "abcabc"
text1 = "aabbaccc"
text2 = "ababcdcdababcdcd"
text3 = "abcabcdede"
text4 = "abcabcabcabcdededededede"
text5 = "xababcdcdababcdcd"
text6 = 'a'

print(solution(text5))

#print(test1[4:9])

#for i in range(2, 10, 2):
 #   print(i)