first_number = (int(input("Give me the lower number: ")))
last_number = (int(input("Give me the bigger number: ")))

palin = 0
trans = 0
lyc = 0
Numbers=[]

for i in range (first_number,last_number+1):
    Numbers.append(i)

for i in Numbers:
    each_value = str(i)
    reverse = each_value[::-1]
    if  each_value == reverse:
        palin += 1
    else:
        counter = 0
        while each_value != reverse and counter != 30:
            each_value = int(each_value)
            reverse = int(reverse)

            each_value = each_value + reverse

            each_value = str(each_value)
            reverse = each_value[::-1]

            if each_value == reverse:
                trans += 1
            counter += 1

        if each_value != reverse and counter >= 30:
            print ("The number", i ,"is Lychrel")
            lyc += 1

print ("Natural palindromes: ", palin)
print ("Become palindromes: ", trans)
print ("Lychrel candidates: ", lyc)
