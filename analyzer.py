
total=0
numbers=[]
the_2=0
the_1=0
numb_of_numbers=0
words=[]
countted_letters=[]
countted_letters_grob_2=[]
min_number=0
max_numb=0
while True:
    message_box=input("(write 'END' to stop)\nwrite massage):")
    if message_box=="END":
        break

    if message_box.isdigit():
        numb_of_numbers+=1
        if numb_of_numbers==1:
            max_numb=int(message_box)
            min_number=int(message_box)
        else:
            if int(message_box)>max_numb:
                max_numb=int(message_box)
            if int(message_box)<min_number:
                min_number=int(message_box)
        total+=int(message_box)
        numbers +=message_box

        if int(message_box)%2==0:
            the_2+=1
        if int(message_box)%2!=0:
            the_1+=1
    if any (ch.isalpha() for ch in message_box):
        words+=message_box.split()
        for ch in message_box:
            countted_letters.append(ch)
for n in countted_letters:
    if n not in countted_letters_grob_2:
        countted_letters_grob_2+=n
        count=countted_letters.count(n)
        print(f"{n}:{count}")

print(f"مجموه الارقام ={total}")
print(f"عدد الارقام ={numb_of_numbers}")
print(f"عدد الارقام الزوجية ={the_2}")
print(f"عدد الارقام الفردية ={the_1}")
print(f"اصغر رقم ={min_number}")
print(f"اكبر رقم ={max_numb}")
print(f"عدد الكلمات ={len(words)}")
print(f"عدد الحروف={len(countted_letters)}")
