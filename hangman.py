Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> home = "アメリカ"
>>> if home == "アメリカ":
	print("Hello, America!")

	
Hello, America!
>>> else:
	
SyntaxError: invalid syntax
>>> home = "アメリカ"
>>> if home == "アメリカ":
	print("Hello, America!")
	else:
		
SyntaxError: invalid syntax
>>> home = "アメリカ"
>>> if home == "アメリカ":
	print("Hello, America!")
else:
	print("Hello, World!")

	
Hello, America!
>>> def hangman(word):
	wrong = 0
	stages = ["",
		  "__________          ",
		  "|                   ",
		  "|          |        ",
		  "|          o        ",
		  "|         /|\       ",
		  "|         / \       ",
		  "|                   "
		  ]
	rletters = list(word)
	board = ["_"] * len(word)
	win = False
	print("ハングマンへようこそ！")
	while wrong < len(stages) - 1:
		print("\n")
		msg = "１文字を予想してね"
		char = input(msg)
		if char in rletters:
			cind = rletters.index(char)
			board[cind] = char
			rletters[cind] = $
			
SyntaxError: invalid syntax
>>> def hangman(word):
	wrong = 0
	stages = ["",
		  "__________          ",
		  "|                   ",
		  "|          |        ",
		  "|          o        ",
		  "|         /|\       ",
		  "|         / \       ",
		  "|                   "
		  ]
	rletters = list(word)
	board = ["_"] * len(word)
	win = False
	print("ハングマンへようこそ！")
	while wrong < len(stages) - 1:
		print("\n")
		msg = "１文字を予想してね"
		char = input(msg)
		if char in rletters:
			cind = rletters.index(char)
			board[cind] = char
			rletters[cind] = '$'
		else:
			wrong += 1
		print(" ".join(board))
		e = wrong + 1
		print("\n".join(stages[0:e]))
		if "_" not in board:
			print("あなたの勝ち！")
			print(" ".join(board))
			win = True
			break
		if not win:
			print("\n".join(stages[0:wrong +1]))
			print("あなたの負け！正解は {}."format(word))
			
SyntaxError: invalid syntax
>>> print("あなたの負け！正解は{}.".format(word))
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    print("あなたの負け！正解は{}.".format(word))
NameError: name 'word' is not defined
>>> 
