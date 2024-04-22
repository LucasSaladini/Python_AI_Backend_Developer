linguagens = ["python", "js", "c", "java", "csharp"]
s1 = linguagens.sort()
print(s1)

linguagens = ["python", "js", "c", "java", "csharp"]
s2 = linguagens.sort(reverse=True)
print(s2)

linguagens = ["python", "js", "c", "java", "csharp"]
s3 = linguagens.sort(key=lambda x: len(x))
print(s3)

linguagens = ["python", "js", "c", "java", "csharp"]
s4 = linguagens.sort(key=lambda x: len(x), reverse=True)
print(s4)
