# مرتضی کیانی تمرین دوم
print("سن شما به ساعت:", hours)
print("سن شما به دقیقه:", minutes)
print("سن شما به ثانیه:", seconds)
print("سن شما به ثانیه:", seconds)



# دریافت عدد دو رقمی
num = int(input("یک عدد دو رقمی وارد کنید: "))

# جدا کردن دهگان و یکان
tens = num // 10
ones = num % 10

# ساخت عدد معکوس
reverse_num = ones * 10 + tens

#  نتیجه
print("مقلوب عدد =", reverse_num)