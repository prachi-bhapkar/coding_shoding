dict={"mon":3,"tue":5,"thu":9}
print("given dictionary is ",dict)
check_key=input("enter key=")
check_val=input("enter value=")
if check_key in dict:
    print(check_key,"is present")
    dict.pop(check_key)
    dict[check_key]=check_key
else:
    print (check_key,"not present")
    dict[check_key]=check_val
    print("uppdated dictionary:",dict)