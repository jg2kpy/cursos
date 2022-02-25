import random

def main():
    name = input("Hello, What is you name?\n")
    print(f"Well, {name}, I am thinking of a integer number between 1 and 20.")
    rand = random.randint(1,20)
    entry = -1
    tries = 0
    while entry != rand:
        print("Take a guess")
        entry = int(input())
        if entry > rand:
            print("Your guess es too high")
        elif entry < rand:
            print("Your guess es too low")
        tries+=1
    
    print(f"Good job, {name}!, You guessed my number in {tries} guesses!")


if __name__ == "__main__":
    main()