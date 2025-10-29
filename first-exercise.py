# مرتضی کیانی تمرین اول

# گرفتن سن از کاربر
age = int(input("لطفا سن  خود را به سال وارد کنید: "))

# محاسبه بر حسب سال
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

# نمایش خروجی
print("سن شما به ساعت:", hours)
print("سن شما به دقیقه:", minutes)
print("سن شما به ثانیه:", seconds)
