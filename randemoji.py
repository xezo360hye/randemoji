from random import choices as rnd
happy = "🔥😂😊😁🙏😎💪😋😇🎉🙌🤘👍🤑🤩🤪🤠🥳😌🤤😍😀"
sad = "😭😔😒😩😢🤦🤷😱👎🤨😑😬🙄🤮😵🤯🧐😕😟😤😡🤬"

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
