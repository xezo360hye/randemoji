from random import choices as rnd
happy = "๐ฅ๐๐๐๐๐๐ช๐๐๐๐๐ค๐๐ค๐คฉ๐คช๐ค ๐ฅณ๐๐คค๐๐"
sad = "๐ญ๐๐๐ฉ๐ข๐คฆ๐คท๐ฑ๐๐คจ๐๐ฌ๐๐คฎ๐ต๐คฏ๐ง๐๐๐ค๐ก๐คฌ"

def main():
	string = input("Enter ur str here\n> ")
	use = int(input("1 - only happy\n2 - only sad\n3 - both\n> "))
	res = ""
	for i in string:
		if i == " ":
			res += rnd(happy if use == 1 else sad if use == 2 else happy + sad)[0]
		else:	res += i
	print(res)

if __name__ == "__main__":
	main()
