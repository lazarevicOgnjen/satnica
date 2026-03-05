def writeToMD(s):
	with open ("subjects.md", "w", encoding="utf-8") as f:
		f.write(s)

def appendToMD(s):
	with open ("subjects.md", "a", encoding="utf-8") as f:
		f.write(s)	
	
