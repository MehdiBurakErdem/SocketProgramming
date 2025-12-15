from typing import List, Dict, Tuple, Iterable

def listVsTuple() -> Tuple[List[int], Tuple[int, ...]]:
	lst = [10,20,30]
	tpl = (1,2,3)
	lst.append(40)	#ancak tuple değişmez(imutable) hızlı,güvenli,az bellek

	#bence en önemlisi tuple hashlanebilir...
	htpl = {(41.01, 28.97): "Istanbul", (39.93, 32.85): "Ankara"}
	print("Hashlanan tuple aşağıda------")
	print(htpl)
	print(htpl[(41.01, 28.97)])
	print("----")

	return lst,tpl

def list_comprehension(n: int) -> List[int]:
	return [i * i for i in range(n) if i % 2 == 0]


def dict_comprehension(words: Iterable[str]) -> Dict[str, int]:
	return {w: len(w) for w in words}

def main() -> None:
	print("+---- Colllections And Comprehensions ----+")
	print("list vs tuple: ", listVsTuple())
	print("list comprehension (n=10):", list_comprehension(10))
	print("dict comprehesion", dict_comprehension(["apple","pear"]))

if __name__ == "__main__":
	main()
