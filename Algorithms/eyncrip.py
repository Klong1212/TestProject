import string

def caesarCipher(s, k):
    Upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for i in range(len(s)):
        if s[i].isupper():
            result += Upper[(Upper.index(s[i]) + k) % 26]
        elif s[i].islower():
            result += lower[(lower.index(s[i]) + k) % 26]
        else:
            result += s[i]  # ถ้าไม่ใช่ตัวอักษร ให้ใส่ค่าตามเดิม
    return result

