
def rotateString(s : str, goal : str) -> bool:
    if len(s) != len(goal): #checking if length equal or nto
        return False
    for i in range(len(s)):
        if s[i:] + s[:i] == goal:
            return True

s = input()
goal = input()
print(rotateString(s, goal))
