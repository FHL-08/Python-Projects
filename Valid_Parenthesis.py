def main():
    pattern = input("please input a string of parenthesis characters: ")
    if (verify_pattern(pattern)):
        print("True")
    else:
        print("False")

def verify_pattern(pattern):
    valid = []
    length = len(pattern)
    if (length%2 == 0):
        for i in range(length):
            if (i < length - 1):
                if (pattern[i] == "("):
                    if (pattern[i+1] == ")" or (pattern[-i-1] == ")" and (i + 1) < length/2)):
                        valid.append("true")
                    else:
                        continue

                elif (pattern[i] == "["):
                    if (pattern[i+1] == "]" or (pattern[-i-1] == "]" and (i + 1) < length/2)):
                        valid.append("true")
                    else:
                        continue

                elif (pattern[i] == "{"):
                    if (pattern[i+1] == "}" or (pattern[-i-1] == "}" and (i + 1) < length/2)):
                        valid.append("true")
                    else:
                        continue
        if (len(valid) == length/2):
            return True
    else:
        return False

main()

