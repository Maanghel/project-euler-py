"""
A palindromic number reads the same both ways. The largest palindrome 
made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers. 
"""

def largest_palindrome_three_digit():
    """returns the largest palindrome made from the product of two 3-digit numbers"""
    max_palindrome = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            if str(product) == str(product)[::-1]:
                max_palindrome = max(max_palindrome, product)
    return max_palindrome

#########################   Main    ################################

if __name__ == "__main__":
    print(largest_palindrome_three_digit())
