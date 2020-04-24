def main():
    with open('test.txt', 'r', encoding='UTF-8') as fd:
        number = 0
        for line in fd:
            words = line.split()
            number += len(words)
    print("Number of words in a file: ", number)
            
if __name__ == '__main__':
    main()
