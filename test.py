x = 0
a_list = ['USA', 'CA', 'FR']

while x not in a_list:
    print("Country not in list. Please enter something else.")
    x = input("Enter country acronym: ")
#    if(x=="USA"):
#        print("United States of America")
#    if(x=="CA"):
#        print("Canada")
#    if(x=="FR"):
#        print("France")
    d = {'USA':'United States of America', 'CA':'Canada','FR':'France'}
    print(x + ' is ' + d[x])