import hgtk

MATCH_H2B_CHO = {
    u'ㄱ': [[0,0,0,1,0,0]],
    u'ㄴ': [[1,0,0,1,0,0]],
    u'ㄷ': [[0,1,0,1,0,0]],
    u'ㄹ': [[0,0,0,0,1,0]],
    u'ㅁ': [[1,0,0,0,1,0]],
    u'ㅂ': [[0,0,0,1,1,0]],
    u'ㅅ': [[0,0,0,0,0,1]],
    u'ㅇ': [[]],
    u'ㅈ': [[0,0,0,1,0,1]],
    u'ㅊ': [[0,0,0,0,1,1]],
    u'ㅋ': [[1,1,0,1,0,0]],
    u'ㅌ': [[1,1,0,0,1,0]],
    u'ㅍ': [[1,0,0,1,1,0]],
    u'ㅎ': [[0,1,0,1,1,0]],

    u'ㄲ': [[0,0,0,0,0,1], [0,0,0,1,0,0]],
    u'ㄸ': [[0,0,0,0,0,1], [0,1,0,1,0,0]],
    u'ㅃ': [[0,0,0,0,0,1], [0,0,0,1,1,0]],
    u'ㅆ': [[0,0,0,0,0,1], [0,0,0,0,0,1]],
    u'ㅉ': [[0,0,0,0,0,1], [0,0,0,1,0,1]],
}

MATCH_H2B_JOONG = {
    u'ㅏ': [[1,1,0,0,0,1]],
    u'ㅑ': [[0,0,1,1,1,0]],
    u'ㅓ': [[0,1,1,1,0,0]],
    u'ㅕ': [[1,0,0,0,1,1]],
    u'ㅗ': [[1,0,1,0,0,1]],
    u'ㅛ': [[0,0,1,1,0,1]],
    u'ㅜ': [[1,0,1,1,0,0]],
    u'ㅠ': [[1,0,0,1,0,1]],
    u'ㅡ': [[0,1,0,1,0,1]],
    u'ㅣ': [[1,0,1,0,1,0]],
    u'ㅐ': [[1,1,1,0,1,0]],
    u'ㅔ': [[1,0,1,1,1,0]],
    u'ㅒ': [[0,0,1,1,1,0], [1,1,1,0,1,0]],
    u'ㅖ': [[0,0,1,1,0,0]],
    u'ㅘ': [[1,1,1,0,0,1]],
    u'ㅙ': [[1,1,1,0,0,1], [1,1,1,0,1,0]],
    u'ㅚ': [[1,0,1,1,1,1]],
    u'ㅝ': [[1,1,1,1,0,0]],
    u'ㅞ': [[1,1,1,1,0,0], [1,1,1,0,1,0]],
    u'ㅟ': [[1,0,1,1,0,0], [1,1,1,0,1,0]],
    u'ㅢ': [[0,1,0,1,1,1]],
}

MATCH_H2B_JONG = {
    u'ㄱ': [[1,0,0,0,0,0]],
    u'ㄴ': [[0,1,0,0,1,0]],
    u'ㄷ': [[0,0,1,0,1,0]],
    u'ㄹ': [[0,1,0,0,0,0]],
    u'ㅁ': [[0,1,0,0,0,1]],
    u'ㅂ': [[1,1,0,0,0,0]],
    u'ㅅ': [[0,0,1,0,0,0]],
    u'ㅇ': [[0,1,1,0,1,1]],
    u'ㅈ': [[1,0,1,0,0,0]],
    u'ㅊ': [[0,1,1,0,0,0]],
    u'ㅋ': [[0,1,1,0,1,0]],
    u'ㅌ': [[0,1,1,0,0,1]],
    u'ㅍ': [[0,1,0,0,1,1]],
    u'ㅎ': [[0,0,1,0,1,1]],

    u'ㄲ': [[1,0,0,0,0,0], [1,0,0,0,0,0]],
    u'ㄳ': [[1,0,0,0,0,0], [0,0,1,0,0,0]],
    u'ㄵ': [[0,1,0,0,1,0], [1,0,1,0,0,0]],
    u'ㄶ': [[0,1,0,0,1,0], [0,0,1,0,1,1]],
    u'ㄺ': [[0,1,0,0,0,0], [1,0,0,0,0,0]],
    u'ㄻ': [[0,1,0,0,0,0], [0,1,0,0,0,1]],
    u'ㄼ': [[0,1,0,0,0,0], [1,1,0,0,0,0]],
    u'ㄽ': [[0,1,0,0,0,0], [0,0,1,0,0,0]],
    u'ㄾ': [[0,1,0,0,0,0], [0,1,1,0,0,1]],
    u'ㄿ': [[0,1,0,0,0,0], [0,1,0,0,1,1]],
    u'ㅀ': [[0,1,0,0,0,0], [0,0,1,0,1,1]],
    u'ㅄ': [[1,1,0,0,0,0], [0,0,1,0,0,0]],
    u'ㅆ': [[0,0,1,1,0,0]],
}

MATCH_H2B_ALPHABET = {
    'a': [[1,0,0,0,0,0]],
    'b': [[1,1,0,0,0,0]],
    'c': [[1,0,0,1,0,0]],
    'd': [[1,0,0,1,1,0]],
    'e': [[1,0,0,0,1,0]],
    'f': [[1,1,0,1,0,0]],
    'g': [[1,1,0,1,1,0]],
    'h': [[1,1,0,0,1,0]],
    'i': [[0,1,0,1,0,0]],
    'j': [[0,1,0,1,1,0]],
    'k': [[1,0,1,0,0,0]],
    'l': [[1,1,1,0,0,0]],
    'm': [[1,0,1,1,0,0]],
    'n': [[1,0,1,1,1,0]],
    'o': [[1,0,1,0,1,0]],
    'p': [[1,1,1,1,0,0]],
    'q': [[1,1,1,1,1,0]],
    'r': [[1,1,1,0,1,0]],
    's': [[0,1,1,1,0,0]],
    't': [[0,1,1,1,1,0]],
    'u': [[1,0,1,0,0,1]],
    'v': [[1,1,1,0,0,1]],
    'w': [[0,1,1,1,1,1]],
    'x': [[1,0,1,1,0,1]],
    'y': [[1,0,1,1,1,1]],
    'z': [[1,0,1,0,1,1]],

    'A': [[0,0,0,0,0,1], [1,0,0,0,0,0]],
    'B': [[0,0,0,0,0,1], [1,1,0,0,0,0]],
    'C': [[0,0,0,0,0,1], [1,0,0,1,0,0]],
    'D': [[0,0,0,0,0,1], [1,0,0,1,1,0]],
    'E': [[0,0,0,0,0,1], [1,0,0,0,1,0]],
    'F': [[0,0,0,0,0,1], [1,1,0,1,0,0]],
    'G': [[0,0,0,0,0,1], [1,1,0,1,1,0]],
    'H': [[0,0,0,0,0,1], [1,1,0,0,1,0]],
    'I': [[0,0,0,0,0,1], [0,1,0,1,0,0]],
    'J': [[0,0,0,0,0,1], [0,1,0,1,1,0]],
    'K': [[0,0,0,0,0,1], [1,0,1,0,0,0]],
    'L': [[0,0,0,0,0,1], [1,1,1,0,0,0]],
    'M': [[0,0,0,0,0,1], [1,0,1,1,0,0]],
    'N': [[0,0,0,0,0,1], [1,0,1,1,1,0]],
    'O': [[0,0,0,0,0,1], [1,0,1,0,1,0]],
    'P': [[0,0,0,0,0,1], [1,1,1,1,0,0]],
    'Q': [[0,0,0,0,0,1], [1,1,1,1,1,0]],
    'R': [[0,0,0,0,0,1], [1,1,1,0,1,0]],
    'S': [[0,0,0,0,0,1], [0,1,1,1,0,0]],
    'T': [[0,0,0,0,0,1], [0,1,1,1,1,0]],
    'U': [[0,0,0,0,0,1], [1,0,1,0,0,1]],
    'V': [[0,0,0,0,0,1], [1,1,1,0,0,1]],
    'W': [[0,0,0,0,0,1], [0,1,1,1,1,1]],
    'X': [[0,0,0,0,0,1], [1,0,1,1,0,1]],
    'Y': [[0,0,0,0,0,1], [1,0,1,1,1,1]],
    'Z': [[0,0,0,0,0,1], [1,0,1,0,1,1]],

    '1': [[0,0,1,1,1,1], [1,0,0,0,0,0]],
    '2': [[0,0,1,1,1,1], [1,1,0,0,0,0]],
    '3': [[0,0,1,1,1,1], [1,0,0,1,0,0]],
    '4': [[0,0,1,1,1,1], [1,0,0,1,1,0]],
    '5': [[0,0,1,1,1,1], [1,0,0,0,1,0]],
    '6': [[0,0,1,1,1,1], [1,1,0,1,0,0]],
    '7': [[0,0,1,1,1,1], [1,1,0,1,1,0]],
    '8': [[0,0,1,1,1,1], [1,1,0,0,1,0]],
    '9': [[0,0,1,1,1,1], [0,1,0,1,0,0]],
    '0': [[0,0,1,1,1,1], [0,1,0,1,1,0]],

    ',': [[0,1,0,0,0,0]],
    '.': [[0,1,0,0,1,1]],
    '-': [[0,1,0,0,1,0]],
    '?': [[0,1,1,0,0,1]],
    '_': [[0,0,1,0,0,1]],
    '!': [[0,1,1,0,1,0]],
}


def letter(hangul_letter):
    """
    Convert a hangul letter to 6-dot braille
    (alphabet, number, and some special chracter supported)

    :param str hangul: a hangul chracter to convert to braille
    :return: braille data (6-int list with the value 0 or 1)
    :rtype: list[str, list[int]]
    """
    result = []
    hangul_decomposed = hgtk.text.decompose(hangul_letter[0])
    hangul_decomposed = \
        hangul_decomposed.replace(hgtk.text.DEFAULT_COMPOSE_CODE, '')
    for i in range(len(hangul_decomposed)):
        hangul = hangul_decomposed[i]
        if i == 0 and hangul in MATCH_H2B_CHO:
            result.append([hangul, MATCH_H2B_CHO[hangul]])
        if i == 0 and hangul in MATCH_H2B_ALPHABET:
            result.append([hangul, MATCH_H2B_ALPHABET[hangul]])
        if i == 1 and hangul in MATCH_H2B_JOONG:
            result.append([hangul, MATCH_H2B_JOONG[hangul]])
        if i == 2 and hangul in MATCH_H2B_JONG:
            result.append([hangul, MATCH_H2B_JONG[hangul]])
            
    if result == []:
        result.append([hangul, [[0,0,0,0,0,0]]])
    return result


# +
#### 우리 음료수에 필요한 약어들 ####
# 다, 사, 카, 타 
# 온, 울, 을, 영(엉), 옹

## 필요없는 약어 ##
# 가,나 마, 바, 자, 파, 하 : (내가 사용하는 점자 번역기에서는 마와 자는 약어를 사용하지 않더라구요. 만들라고 하면 만들 순 있삼)
# 것, 억, 언, 얼, 연, 열, 옥, 운, 은, 인
# 그래서, 그러나, 그러면, 그러므로, 그런데, 그리고, 그리하여
# -

def text(hangul_sentence):
    result = []

    for hangul_letter in hangul_sentence:
        result.append([hangul_letter, letter(hangul_letter)])
        

    ##----민지 코드-----
    for i in range(len(result)): # 다사카타


        if result[i][1][0][0] == 'ㄷ'and result[i][1][1][0]=='ㅏ':
            result[i] = ['다', [['다',[[0,1,0,1,0,0]]]]]

        if result[i][1][0][0] == 'ㅅ'and result[i][1][1][0]=='ㅏ':
            result[i] = ['사', [['사',[[1,1,1,0,0,0]]]]]

        if result[i][1][0][0] == 'ㅋ'and result[i][1][1][0]=='ㅏ':
            result[i] = ['카', [['카',[[1,1,0,1,0,0]]]]]

        if result[i][1][0][0] == 'ㅌ'and result[i][1][1][0]=='ㅏ':
            result[i] = ['타', [['타',[[1,1,0,0,1,0]]]]]

    #----온울을영(엉)옹
        try :
            if result[i][1][1][0] == 'ㅗ' and result[i][1][2][0]=='ㄴ':
                result[i][1][1:] = [['온', [[1,1,1,0,1,1]]]]

            if result[i][1][1][0] == 'ㅜ' and result[i][1][2][0]=='ㄹ':
                result[i][1][1:] = [['울', [[1,1,1,1,0,1]]]]

            if result[i][1][1][0] == 'ㅡ' and result[i][1][2][0]=='ㄹ':
                result[i][1][1:] = [['을', [[0,1,1,1,0,1]]]]

            if (result[i][1][1][0]=='ㅓ' or result[i][1][1][0]=='ㅕ') and result[i][1][2][0]=='ㅇ':
                result[i][1][1:] = [['엉', [[1,1,0,1,1,1]]]]

            if result[i][1][1][0] == 'ㅗ' and result[i][1][2][0]=='ㅇ':
                result[i][1][1:] = [['옹', [[1,1,1,1,1,1]]]]
        except : 
            continue

        if result[i][1][0][0] == 'ㅇ':
            result[i][1:] = [result[i][1][1:]]
        
    return result

'''테코
result = text('레쓰비 마일드')
jum_lst = []

for i in range(len(result)):
    for j in (result[i][1]):
        #print(j[1])
        if j[1] !=1:
   
            for l in range(len(j[1])):
                jum = j[1][l]

                jum = ['○' if x==0 else '●' for x in jum]
                jum_lst.append(jum)
            
                
for i in range(len(jum_lst)):
    try:
        print(f"{jum_lst[i][0]} {jum_lst[i][3]}")
        print(f"{jum_lst[i][1]} {jum_lst[i][4]}")
        print(f"{jum_lst[i][2]} {jum_lst[i][5]}")
        print(' ')   
    except:
        continue'''


