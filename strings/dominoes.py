class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        if len(dominoes) == 1:
            return dominoes
        leftDoms = []
        rightDoms = []
        for ch in dominoes:
            leftDoms.append(ch)
            rightDoms.append(ch)
        for i in reversed(range(len(dominoes))):
            if i == len(dominoes) - 1:
                continue
            elif i == 0:
                if dominoes[i] == '.':
                    if leftDoms[i+1] == 'L':
                        leftDoms[i] = 'L'

            elif dominoes[i] == '.':
                if leftDoms[i+1] == 'L':
                    if leftDoms[i-1] != 'R':
                        leftDoms[i] = 'L'

        
        for i in range(len(dominoes)):
            if i == len(dominoes) - 1:
                if dominoes[i] == '.':
                    if rightDoms[i-1] == 'R':
                        rightDoms[i] = 'R'
            elif i == 0:
                continue
            elif dominoes[i] == '.':
                if rightDoms[i-1] == 'R':
                    if i + 1 < len(dominoes):
                        if rightDoms[i + 1] != 'L':
                            rightDoms[i] = 'R'

        output = ""

        print("left", leftDoms)
        print("right", rightDoms)

        for i in range(len(dominoes)):
            if (leftDoms[i] == 'R' and rightDoms[i] == 'L') or (leftDoms[i] == 'L' and rightDoms[i] == 'R'):
                output += '.'   
            elif (leftDoms[i] == 'R' and rightDoms[i] == '.') or (leftDoms[i] == '.' and rightDoms[i] == 'R'):
                output += 'R'
            elif leftDoms[i] == 'R' and rightDoms[i] == 'R':
                output += 'R'
            elif (leftDoms[i] == 'L' and rightDoms[i] == '.') or (leftDoms[i] == '.' and rightDoms[i] == 'L'):
                output += 'L'
            elif leftDoms[i] == 'L' and rightDoms[i] == 'L':
                output += 'L'
            else:
                output += '.'



        return output


# result = Solution()
# answer = result.pushDominoes(".L.R...LR..L..")
# print("expected answer ", "LL.RR.LLRRLL..")
# print("actual answer", answer)


# result = Solution()
# answer = result.pushDominoes(".L.R.")
# print("expected answer ", "LL.RR")
# print("actual answer", answer)

# result = Solution()
# answer = result.pushDominoes("..R..")
# print("expected answer ", "..RRR")
# print("actual answer", answer)

result = Solution()
answer = result.pushDominoes("R.......L.R.........")
print("expected answer ", "RRRR.LLLL.RRRRRRRRRR")
print("actual answer", answer)