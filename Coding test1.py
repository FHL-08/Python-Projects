import math
a = [25, 2, 3, 57, 38, 41]

def solution(a):
    """
    Return the digits with the highest frequency within a list in ascending order.
    
    Args:
        a (list): List of integers.
    
    Returns:
        int: digits with the highest frequency within a list in ascending order.
    
    """
    answer = []

    def breakdown(a):
        """
        Breakdown the list of integers into a list of digits.

        Args:
            a (list): List of integers.
        
        Returns:
            list: List of digits.
        """
        digits = {}    
        for i in a:
            idigit = []

            if i > 9:
                a = i%10
                idigit.append(a)
                b = int((i - a)/10)
                idigit.append(b)

                for j in idigit:  
                    if j not in digits.keys():
                        digits[j] = 1
                    else:
                        digits[j] += 1
                print(digits)

            else:
                if i not in digits.keys():
                    digits[i] = 1
                else:
                    digits[i] += 1

        return digits

    digits = breakdown(a)
    max_number = max(digits.values())

    for i in digits.keys():
        if digits[i] == max_number:
            answer.append(i)
    
    return sorted(answer, reverse = False)

def main():
    print(solution(a))        

if __name__ == "__main__":
    main()