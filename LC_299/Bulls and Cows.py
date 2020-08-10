"""
    You are playing the following Bulls and Cows game with your friend: You
    write down a number and ask your friend to guess what the number is. Each
    time your friend makes a guess, you provide a hint that indicates how many
    digits in said guess match your secret number exactly in both digit and
    position (called "bulls") and how many digits match the secret number but
    locate in the wrong position (called "cows"). Your friend will use
    successive guesses and hints to eventually derive the secret number.
    
    Write a function to return a hint according to the secret number and
    friend's guess, use A to indicate the bulls and B to indicate the cows.
"""


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        num_bulls = num_cows = 0
        numbers = [0]*10
        for i in range(len(secret)):
            s, g = int(secret[i]), int(guess[i])
            if s == g:  # bulls found
                num_bulls += 1
            else:
                if numbers[s] < 0:
                    num_cows += 1
                if numbers[g] > 0:
                    num_cows += 1
                numbers[s] += 1
                numbers[g] -= 1
        return f"{num_bulls}B{num_cows}C"


def main():
    line = input("Enter the number of digits: ")
    digit_len = int(line)
    import random
    rand_num = random.randint(0, 10**digit_len - 1)
    secret = f"{rand_num:0{digit_len}}"
    print(f"A random {digit_len}-digit number is generated. Now take a guess")

    sol = Solution()
    
    while True:
        line = input()
        guess = str(line)
        ret = sol.getHint(secret, guess)
        if ret == "4B0C":
            break
        print(ret)
    print("You guessed it!")


if __name__ == '__main__':
    main()
