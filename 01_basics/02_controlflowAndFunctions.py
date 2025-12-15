def classify_number(n: int) ->str:
	if n < 0:
		return "negative"
	elif n == 0:
		return "zero"
	else:
		return "positive"


def print_numbers(limit: int = 5) ->None:	#Eğer x verilmezse default olarak 5 olarak işlem yapar
	for i in range(limit):
		if i == 3:
			continue
		print(f"i = {i}, type = {classify_number(i)}")	#virgül ile de olur, f""ile de

def loop_demo() ->None:
	values = [10, 20, 30, 40, 50]
	for index, value in enumerate(values):
		if value == 30:
			break
		print(f"index={index} , value={value}")

def main () -> None:	#Bu fonksiyon çalıştıktan sonra herhangi bir şey döndürmeyecek
	print_numbers()
	print("------")
	loop_demo()

if __name__ == "__main__":
	main()





