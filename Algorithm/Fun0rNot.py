def funnyString(s):
    rev_s = s[::-1]  # Reverse the string

    # Calculate ASCII differences for both original and reversed strings
    diff_s = [abs(ord(s[i]) - ord(s[i - 1])) for i in range(1, len(s))]
    diff_rev_s = [abs(ord(rev_s[i]) - ord(rev_s[i - 1])) for i in range(1, len(rev_s))]

    return "Funny" if diff_s == diff_rev_s else "Not Funny"

if __name__ == '__main__':

    q = int(input().strip())  # Number of test cases

    for _ in range(q):
        s = input().strip()  # Read input string
        result = funnyString(s)  # Call function
        print(result)