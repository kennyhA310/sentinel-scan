from core.engine import Scanner
if __name__ == "__main__":
    target = input ("Enter target IP: ")
    scanner = Scanner(target)
    scanner.run()