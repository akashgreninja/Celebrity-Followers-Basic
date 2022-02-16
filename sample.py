import art
import data
import random
import art
from data import data1



print(art.logo)



score=0

def calculation(number):
    celeb_name=number["name"]
    celeb_country = number["country"]
    celeb_description = number["description"]
    celeb_count = number["follower_count"]
    return f"{celeb_name} , a {celeb_description},from{celeb_country}"

def guess_1(guess,followers_1,followers_2):

    if followers_1>followers_2:
        return guess=="a"
    else:
        return guess=="b"

number_2=random.choice(data1)
end_of_game=True
while end_of_game:


    number_1=number_2
    number_2=random.choice(data1)


    while number_2==number_1:
        number_2=random.choice(data1)
    # print(number_1)


    print(f"choice A : {calculation(number_1)}")

    print(art.vs)

    print(f"choice B : {calculation(number_2)}")



    guess = input("Select A or B").lower()
    followers_1=number_1["follower_count"]
    followers_2=number_2["follower_count"]

    check_answer=guess_1(guess,followers_1,followers_2)


    # end_of_game=False
    # while end_of_game==False:

    if check_answer==True:
        print("you are right")
        score+=1
        print(f"your score is {score}")
            # print(f"choice A : {calculation(number_1)}")
            # print(f"choice A : {calculation(number_2)}")


    else:
        print("you are wrong")
        end_of_game=False
        print(f"your final score  is {score}")