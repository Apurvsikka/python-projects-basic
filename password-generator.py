#importing modules
import secrets as sec
import string as st
import random
# initializing points
points = 0

# asking user to select range ot the number
print('-----------------------------Password Generator-----------------------------')
pwd_tpe = input("enter 1 for easy to remember password, 2 for a bit hader password, password and 3 for complex password: ")

if pwd_tpe == '1':
    x = int(input('select the number of words you want: '))
    words = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "grape", "pineapple", "strawberry", "blueberry", "raspberry", "blackberry", "watermelon", "papaya", "pear", "peach", "plum", "apricot", "avocado", "fig", "guava", "jackfruit", "lemon", "lime", "lychee", "nectarine", "olive", "pomegranate", "tangerine", "tomato", "coconut", "date", "dragonfruit", "durian", "elderberry", "grapefruit", "honeydew", "kumquat", "mangosteen", "persimmon", "quince", "rhubarb", "starfruit", "ugli fruit", "yuzu", "zucchini", "acorn squash", "butternut squash", "cucumber", "eggplant", "green bean", "jalapeno", "lettuce", "mushroom", "onion", "pea", "potato", "pumpkin", "radish", "spinach", "sweet potato", "tomato", "yam", "zucchini", "artichoke", "asparagus", "beet", "bell pepper", "broccoli", "brussels sprout", "cabbage", "carrot"]
    password = random.sample(words, x)
    #converting lisr to string
    password = '-'.join(password)

elif pwd_tpe == '2':
    # asking user to select range ot the number
    upper_limit = int(input('enter the length of password: '))
    alphabet = st.ascii_letters + st.punctuation + st.digits + st.ascii_letters  # creating alphabet1

    password = ''.join(sec.choice(alphabet) for _ in range(upper_limit))

elif pwd_tpe == '3':
   upper_limit = int(input('enter password limit: '))
# generating random number
   if upper_limit == 1:
         alphabet = st.ascii_letters
        #  numbers = st.digits 
         password = sec.choice(alphabet)
        #  password = sec.choice(alphabet) sec.choice(numbers).upper()
   else:
       password = sec.token_urlsafe(upper_limit-1)
else:
    print('invalid input')
    exit()

# print password
print('your password is: ', password)
