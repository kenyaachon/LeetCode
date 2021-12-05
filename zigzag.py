from typing import Counter, List


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        strSize = len(s)
        i = 0
        answer = ""
        position = "down"
        d = 0
        dag = 0
        array = [[' ' for c in range(int(strSize))] for r in range(numRows)]
        
        
        while i < strSize:

            if position=="down" and d < numRows:
                array[d][dag] = s[i]
                d += 1
                if d == numRows and numRows > 2:
                    position = "diagonal"
                    d -= 1
                elif d== numRows and numRows <= 2:
                    d = 0
                    dag += 1
            
            elif position=="diagonal":
                d -= 1
                dag += 1
                array[d][dag] = s[i]
                if d - 1 == 0:
                    position = "down"
                    d = 0
                    dag += 1

            i += 1

        print(array)
        for i in array:
            for letter in i:
                if letter != ' ':
                    answer += letter

        return answer


def main():
    answers = Solution()
    '''
    result = answers.convert("PAYPALISHIRING", 4)
    print("Expected: PINALSIGYAHRPI")
    print(result)


    result = answers.convert("A", 1)
    print("Expected: A")
    print(result)
    '''
    result = answers.convert("ABC", 1)
    print("Expected: ABC")
    print(result)

    result = answers.convert("ADBECF", 2)
    print("Expected: ABCDEF")
    print(result)

    result = answers.convert("PAYPALISHIRING", 3)
    print("Expected: PAHNAPLSIIGYIR")
    print(result)

if __name__=="__main__":
    main()