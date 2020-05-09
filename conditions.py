phone = input("phone: ")
digits_mapping = {
"1": "uno",
"2": "dos" , 
"3": "tres",
"4": "cuatro"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
    print(output)


