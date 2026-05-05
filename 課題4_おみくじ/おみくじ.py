import tkinter as tk

def fortune():
    import random

    words = ["大吉：とても良い",
             "中吉：良い",
             "小吉：すこし良い",
             "吉：普通",
             "凶：悪い",
             "大凶：最悪"]
    n = random.randint(0, len(words)-1)

    #print("あなたの運勢は「",words[n],"」です。")
    buff.set(f"あなたの運勢は{words[n]}です")

root=tk.Tk()
root.title("おみくじ")
root.geometry("300x200")


tk.Label(root,text="あなたの運勢を占います").pack()
tk.Button(root,text="押してください",command=fortune).pack()
buff = tk.StringVar()
tk.Label(root,textvariable=buff).pack()
root.mainloop()