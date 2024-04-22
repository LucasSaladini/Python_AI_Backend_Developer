linguagens = ["python", "js", "c", "java", "csharp"]

s1 = sorted(linguagens, key=lambda x: len(x))
print(s1)

s2 = sorted(linguagens, key=lambda x:len(x), reverse=True)
print(s2)