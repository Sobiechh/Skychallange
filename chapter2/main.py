def getSudo(left, right):
    count = 0 #result

    for number in range(left, right+1):
        number = str(number)
        if sorted(number) == list(number):
            a = zip(number, number[1:])
            if len(set([elem for elem in a if elem[0] == elem[1]])) > 1:
                count += 1

    return count

if __name__ == "__main__":
    left = 372**2
    right = 809**2

    count = getSudo(left, right)
    print(f'{count} meets all three criteria')