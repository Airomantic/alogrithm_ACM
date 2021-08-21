import re


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if not s:
            return None
        s=re.sub('[^a-zA-Z0-9]','',s)
        s=s.lower()
        n=len(s)
        stack=[]
        for i in range(n):
            if s[i] in stack:
                continue
            else:

                while stack and stack[-1]>s[i] and stack[-1] in s[i+1:]:
                    stack.pop()
                stack.append(s[i])

        return "".join(stack)


def stringToString(input):
    return input[:].encode('utf-8').decode('utf-8')


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            s = stringToString(line);

            ret = Solution().removeDuplicateLetters(s)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()