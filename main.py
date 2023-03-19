def increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))

if __name__ == "__main__":
    res = input("Please enter a string: ")
    print(increment_string(res))
