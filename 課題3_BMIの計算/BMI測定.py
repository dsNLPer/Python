import tkinter as tk

def calculate():
    try:
        w = float(w_entry.get())
        h = float(h_entry.get()) / 100
        bmi = w / (h * h)
        
        if bmi < 18.5: 
            s = "低体重(痩せ型)"
        elif bmi < 25: 
            s = "標準体重"
        elif bmi < 30: 
            s = "肥満(1度)"
        elif bmi < 35: 
            s = "肥満(2度)"
        elif bmi < 40: 
            s = "肥満(3度)"
        else: 
            s = "肥満(4度)"
            
        result.set(f"あなたの肥満度は{bmi:.2f}で{s}です")
    except:
        result.set("エラー: 正しい数値を入力してください")

root = tk.Tk()
root.title("BMI測定")
root.geometry("300x200")

tk.Label(root, text="あなたの肥満度を計算します").pack(pady=5)

tk.Label(root, text="体重をkgで入力：").pack()
w_entry = tk.Entry(root)
w_entry.pack()

tk.Label(root, text="身長をcmで入力：").pack()
h_entry = tk.Entry(root)
h_entry.pack()

tk.Button(root, text="BMIを計算します、押してください", command=calculate).pack(pady=10)

result = tk.StringVar()
tk.Label(root, textvariable=result).pack()

root.mainloop()