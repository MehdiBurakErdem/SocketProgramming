from typing import List

def write_file(path: str, lines: List[str]) -> None:
	with open(path, "w") as f:
		for line in lines:
			f.write(line + "\n")

def read_file(path: str) -> List[str]:
	with open(path, "r") as f:
		return [line.strip() for line in f]

def safe_read (path: str) -> None:
	try:
		content = read_file(path)
		print("Dosya icerigi: ")
		for line in content:
			print("-->",line)
	except FileNotFoundError:
        	print("❌ Dosya bulunamadı")
	except Exception as e:
        	print("❌ Beklenmeyen hata:", e)
	finally:
		print("Dosya okuma islemi tamamlandi.")

def main() -> None:
	filename = "example.txt"

	write_file(filename ,["Merhaba", "Icerik: Pyhton File I/O + ERROR Handling"])

	safe_read(filename)

if __name__ == ("__main__"):
	main()
