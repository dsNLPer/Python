import tkinter as tk
import random

def check_guess():
    try:
        guess = int(entry.get())
        if guess < target:
            result_label.config(text="それより大きいです！", fg="blue")
        elif guess > target:
            result_label.config(text="それより小さいです！", fg="red")
        else:
            result_label.config(text="当たり！おめでとう！", fg="green")
            new_game_button.pack(pady=10)
            guess_button.config(state=tk.DISABLED)
    except ValueError:
        result_label.config(text="数字を入力してください！", fg="orange")
    entry.delete(0, tk.END)

def new_game():
    global target
    target = random.randint(1, 1000)
    result_label.config(text="新しいゲームを開始します！", fg="black")
    new_game_button.pack_forget()
    guess_button.config(state=tk.NORMAL)


root = tk.Tk()
root.title("M25W0149") 
root.geometry("500x300")
root.configure(bg="#f0f0f0")

target = random.randint(1, 100)

title_label = tk.Label(
    root, 
    text="数当てゲーム high & low",
    font=("Arial", 16, "bold"),
    bg="#f0f0f0",
    fg="#333"
)
title_label.pack(pady=10)

desc_label = tk.Label(
    root, 
    text="ヒントを見て、ボクの数を当ててね。1から100の間だよ",
    font=("Arial", 12),
    bg="#f0f0f0"
)
desc_label.pack(pady=5)

input_frame = tk.Frame(root, bg="#f0f0f0")
input_frame.pack(pady=15)

entry = tk.Entry(
    input_frame, 
    font=("Arial", 14), 
    width=10,
    justify="center"
)
entry.pack(side=tk.LEFT, padx=5)

guess_button = tk.Button(
    input_frame, 
    text="数を入れたら。押してください", 
    command=check_guess,
    font=("Arial", 12),
    bg="#4CAF50",
    fg="white",
    padx=10
)
guess_button.pack(side=tk.LEFT)

result_label = tk.Label(
    root, 
    text="ヒント：数を入れて",
    font=("Arial", 12),
    bg="#f0f0f0",
    height=2
)
result_label.pack(pady=15)

new_game_button = tk.Button(
    root,
    text="新しいゲームを始める",
    command=new_game,
    font=("Arial", 10),
    bg="#FF9800",
    fg="white"
)

root.mainloop()
