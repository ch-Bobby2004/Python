# True Love Calculator

name1 = input("Enter your name: ").lower()
name2 = input("Enter their name: ").lower()

combined_names = name1 + name2


t = combined_names.count('t')
r = combined_names.count('r')
u = combined_names.count('u')
e = combined_names.count('e')

l = combined_names.count('l')
o = combined_names.count('o')
v = combined_names.count('v')
e2 = combined_names.count('e')  # 'e' counts again for LOVE


true_score = t + r + u + e
love_score = l + o + v + e2
final_score = int(f"{true_score}{love_score}")  # concatenate like 10 + 8 -> 108


if final_score < 10 or final_score > 90:
    print(f"Your True Love score is {final_score}%. A perfect match!")
elif 40 <= final_score <= 50:
    print(f"Your True Love score is {final_score}%. There's potential!")
else:
    print(f"Your True Love score is {final_score}%. Keep the love growing!")