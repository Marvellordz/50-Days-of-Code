from time import time
start = time()

# Accepts a list of names of words and creates accroynms with them
words = ["cetral intelligence agency", "federal government",
         "new york city", "Chelsea Football club"]
for i in words:

    text = i.split()
    a = " "
    for i in text:
        # this line coverts the first letter of each word to capitals
        a = a+str(i[0]).upper()
    print(a)

end = time()
execution_time = end - start
print("Execution Time : ", execution_time)
