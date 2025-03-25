# Data types: string, integer, float and boolean

# String: "Hello"
# [index] it shwgvidzlia wamovigot am indeqsze mdgomi aso
# [-1] it shegvidzlia wamovigot bolo aso
print('Hello'[-1])

print('123' + '345')
# Integer: 33
print(123 + 345)
# did cifrebtan viyenebt _ qveda tires gamosayofad
print(123_456_789)

# Float: 2.3

print(3.14159)
# Boolean: True or False
# didi asoti iwyeba orive
print(True)
print(False)

# ###########
print(len("12345"))

# type() funqciit vigebt monacemta tips
print(type("dzabila"))
print(type(123))
print(type(12.4))
print(type(True))

# int() funqciit monacemebs gadavaqcevt integerad
print(int("1234"))
# float() funqciit monacemebs vxdit floats
print(float(123))
# str() funqciit monacembes vxdit strings
print(str(123))
# bool() funqciit monacemebs vxdit booleans
print(bool("d"))
# 

name_of_the_user = input("Enter your Name:")
length_of_name = len(name_of_the_user)

print('Number of letters in your name: ' + str(length_of_name))

# Mathematical operators

print(123 + 456)
print(7 -3)
print(3 * 2)
# rodesac iyeneb gayofas shedegs abrounebs floats
print(6 / 3)
# es abrunebs integerad
print(6 // 3)
# axarisxeba
print(2**3)

# ES ARIS PRIORITETEBI MOQMEDEBEBIS -- PEMDAS -> Parantheses, Exponents, Multiplication/Divisio, Addition/Subtraction --> (), **, *, /, +, -
print(3 * (3 + 3 / 3 - 3))


# 
bmi = 84 / 1.65 ** 2
print(bmi)

print(int(bmi))

# round() funqcia daamrgvalebs ricxvs
print(round(bmi))

# shegvidzlia round() funqcias meore argumentic gadavcet, romelic amrgvalebs mdzimis shemdeg amden ricxvze

print(round(bmi, 2))

# minichebis operatorebi 

score = 0 

# erti da igivea
score = score + 1
score += 1
# erti da igivea
score = score - 1
score -= 1
# erti da igivea 
score = score / 1
score /= 1

# erti da igivea 
score = score * 1
score *= 1


# f-strings 

print(f"Your score is {score}")

height = 1.8
is_wining = True 
print(f"Your score is = {score}, your height is {height}. You are winning is {is_wining}")