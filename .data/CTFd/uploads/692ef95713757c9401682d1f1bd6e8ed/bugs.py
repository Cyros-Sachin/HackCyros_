import tkinter as t
import time
from tkinter import messagebox
import json, base64, secrets
import urllib.request

VERIFY_URL = "https://rootaccess.pythonanywhere.com/verify"

window = t.Tk()
cw, ch = 600, 450
can = t.Canvas(window, width=cw, height=ch, bg="white")
can.pack()

b = [["3" for x in range(3)] for y in range(3)]
p = []
imp = []
ok = []

human_moves = []
game_over = False


def send_proof_and_show_flag():
    payload = {
        "v": 1,
        "nonce": secrets.token_hex(8),
        "human": human_moves,
    }
    proof = base64.urlsafe_b64encode(json.dumps(payload).encode()).decode()

    req_body = json.dumps({"proof": proof}).encode("utf-8")
    req = urllib.request.Request(
        VERIFY_URL,
        data=req_body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        messagebox.showerror("Verifier error", f"Could not contact verifier:\n{e}")
        return

    if data.get("ok") and data.get("flag"):
        messagebox.showinfo("FLAG", "cyros{"+data["flag"].split("{")[1])
    else:
        messagebox.showinfo("Verifier", f"Result: {data.get('result')}\n(No flag)")


def end_game(msg):
    global game_over
    if game_over:
        return
    game_over = True
    messagebox.showinfo("Winner", msg)
    send_proof_and_show_flag()
    try:
        window.destroy()
    except Exception:
        pass

def click(event):
     global b, p, imp, ok
     if game_over:
        return
     x, y = event.x // 200, event.y // 150
     if len(human_moves) < 5:
         human_moves.append({"x": int(x), "y": int(y)})

     can.create_line(x * 200, y * 150, (x + 1) * 200, (y + 1) * 150, fill="red", width=3)
     can.create_line(x * 200, (y + 1) * 150, (x + 1) * 200, y * 150, fill="red", width=3)

     if event.x > 400:
         if event.y > 300:
             b[2][2] = 0
         elif (event.y < 300) and (event.y > 150):
             b[2][1] = 0
         else:
             b[2][0] = 0
     elif (event.x < 400) & (event.x > 200):
         if event.y > 300:
             b[1][2] = 0
         elif (event.y < 300) and (event.y > 150):
             b[1][1] = 0
         else:
             b[1][0] = 0
     else:
         if event.y > 300:
             b[0][2] = 0
         elif (event.y < 300) and (event.y > 150):
             b[0][1] = 0
         else:
             b[0][0] = 0
     ok=[]
     bruh=[]
     for i in range(0,3):
         for j in range(0,3):
             if b[i][j]==1:
                 ok.append([i,j])
             elif b[i][j]==0:
                 bruh.append([i,j])
     imp=[]
     for i in range(0,3):
         for j in range(0,3):
             if j+2<3:
                 if (b[i][j]==0 and b[i][j+1]==0 and b[i][j+2]!=1):
                     imp.append([i,j+2])
                 if (b[i][j+1]==0 and b[i][j+2]==0 and b[i][j]!=1):
                     imp.append([i,j])
                 if (b[i][j]==0 and b[i][j+2]==0 and b[i][j+1]!=1):
                     imp.append([i,j+1])
                 if (b[j][i]==0 and b[j+1][i]==0 and b[j+2][i]!=1):
                     imp.append([j+2,i])
                 if (b[j+1][i]==0 and b[j+2][i]==0 and b[j][i]!=1):
                     imp.append([j,i])
                 if (b[j][i]==0 and b[j+2][i]==0 and b[j+1][i]!=1):
                     imp.append([j+1,i])
                 if (b[0][0]==0 and b[1][1]==0 and b[2][2]!=1):
                     imp.append([2,2])
                 if (b[1][1]==0 and b[2][2]==0 and b[0][0]!=1):
                     imp.append([0,0])
                 if(b[0][0]==0 and b[2][2]==0 and b[1][1]!=1):
                     imp.append([1,1])
                 if (b[0][2]==0 and b[1][1]==0 and b[2][0]!=1):
                     imp.append([2,0])
                 if (b[1][1]==0 and b[2][0]==0 and b[0][2]!=1):
                     imp.append([0,2])
                 if(b[0][2]==0 and b[2][0]==0 and b[1][1]!=1):
                     imp.append([1,1])
     p=[]
     for i in range(0,3):
         for j in range(0,3):
             if b[i][j] == '3' and b[i][j] not in imp:
                 p.append([i,j])
     if p == [] and imp == []:
         time.sleep(1)
         end_game("Tie Game")
         return
     if [0,0] in ok and [0,1] in ok and b[0][2]=='3':
         time.sleep(1)
         end_game("Computer")
         return
     if [0,1] in ok and [0,2] in ok and b[0][0]=='3':
         time.sleep(1)
         end_game("Computer")
         return
     if [0,0] in ok and [0,2] in ok and b[0][1]=='3':
         time.sleep(1)
         end_game("Computer")
         return
     if [1,0] in ok and [1,1] in ok and b[1][2]=='3':
         time.sleep(1)
         end_game("Computer")
         return
     if [1,0] in ok and [1,2] in ok and b[1][1]=='3':
         time.sleep(1)
         end_game("Computer")
         return
     if [1,1] in ok and [1,2] in ok and b[1][0]=='3':
         time.sleep(1)
         end_game("Computer")
         return
     if [2,0] in ok and [2,1] in ok and b[2][2]=='3':
         time.sleep(1)
         end_game("Computer")
         return
     if [2,1] in ok and [2,2] in ok and b[2][0]=='3':
         time.sleep(1)
         end_game("Computer")
         return
     if [2,0] in ok and [2,2] in ok and b[2][1]=='3':
         time.sleep(1)
         end_game("Computer")
         return
     if [0,0] in ok and [1,0] in ok and b[2][0]=='3':
         time.sleep(1)
         end_game("Computer")
         return
     if [0,0] in ok and [2,0] in ok and b[1][0]=='3':
         time.sleep(1)
         end_game("Computer")
         return
     if [1,0] in ok and [2,0] in ok and b[0][0]=='3':
         time.sleep(1)
         end_game("Computer")
         return
     if [0,1] in ok and [1,1] in ok and b[2][1]=='3':
         time.sleep(1)
         end_game("Computer")
         return
     if [0,1] in ok and [2,1] in ok and b[1][1]=='3':
         time.sleep(1)
         end_game("Computer")
         return
     if [1,1] in ok and [2,1] in ok and b[0][1]=='3':
         time.sleep(1)
         end_game("Computer")
         return
     if [0,2] in ok and [1,2] in ok and b[2][2]=='3':
         time.sleep(1)
         end_game("Computer")
         return
     if [0,2] in ok and [2,2] in ok and b[1][2]=='3':
         time.sleep(1)
         end_game("Computer")
         return
     if [1,2] in ok and [2,2] in ok and b[0][2]=='3':
         time.sleep(1)
         end_game("Computer")
         return
     if [1,1] in ok and [2,2] in ok and b[0][0]=='3':
         time.sleep(1)
         end_game("Computer")
         return
     if [0,0] in ok and [2,2] in ok and b[1][1]=='3':
         time.sleep(1)
         end_game("Computer")
         return
     if [1,1] in ok and [0,0] in ok and b[2][2]=='3':
         time.sleep(1)
         end_game("Computer")
         return
     if [2,0] in ok and [1,1] in ok and b[0][2]=='3':
         time.sleep(1)
         end_game("Computer")
         return
     if [0,2] in ok and [1,1] in ok and b[2][0]=='3':
         time.sleep(1)
         end_game("Computer")
         return
     if [2,0] in ok and [0,2] in ok and b[1][1]=='3':
         time.sleep(1)
         end_game("Computer")
         return
     if [0,0] in bruh and [0,1] in bruh and b[0][2]==0:
         time.sleep(1)
         end_game("Player")
         return
     if [0,1] in bruh and [0,2] in bruh and b[0][0]==0:
         time.sleep(1)
         end_game("Player")
         return
     if [0,0] in bruh and [0,2] in bruh and b[0][1]==0:
         time.sleep(1)
         end_game("Player")
         return
     if [1,0] in bruh and [1,1] in bruh and b[1][2]==0:
         time.sleep(1)
         end_game("Player")
         return
     if [1,0] in bruh and [1,2] in bruh and b[1][1]==0:
         time.sleep(1)
         end_game("Player")
         return
     if [1,1] in bruh and [1,2] in bruh and b[1][0]==0:
         time.sleep(1)
         end_game("Player")
         return
     if [2,0] in bruh and [2,1] in bruh and b[2][2]==0:
         time.sleep(1)
         end_game("Player")
         return
     if [2,1] in bruh and [2,2] in bruh and b[2][0]==0:
         time.sleep(1)
         end_game("Player")
         return
     if [2,0] in bruh and [2,2] in bruh and b[2][1]==0:
         time.sleep(1)
         end_game("Player")
         return
     if [0,0] in bruh and [1,0] in bruh and b[2][0]==0:
         time.sleep(1)
         end_game("Player")
         return
     if [0,0] in bruh and [2,0] in bruh and b[1][0]==0:
         time.sleep(1)
         end_game("Player")
         return
     if [1,0] in bruh and [2,0] in bruh and b[0][0]==0:
         time.sleep(1)
         end_game("Player")
         return
     if [0,1] in bruh and [1,1] in bruh and b[2][1]==0:
         time.sleep(1)
         end_game("Player")
         return
     if [0,1] in bruh and [2,1] in bruh and b[1][1]==0:
         time.sleep(1)
         end_game("Player")
         return
     if [1,1] in bruh and [2,1] in bruh and b[0][1]==0:
         time.sleep(1)
         end_game("Player")
         return
     if [0,2] in bruh and [1,2] in bruh and b[2][2]==0:
         time.sleep(1)
         end_game("Player")
         return
     if [0,2] in bruh and [2,2] in bruh and b[1][2]==0:
         time.sleep(1)
         end_game("Player")
         return
     if [1,2] in bruh and [2,2] in bruh and b[0][2]==0:
         time.sleep(1)
         end_game("Player")
         return
     if [1,1] in bruh and [2,2] in bruh and b[0][0]==0:
         time.sleep(1)
         end_game("Player")
         return
     if [0,0] in bruh and [2,2] in bruh and b[1][1]==0:
         time.sleep(1)
         end_game("Player")
         return
     if [1,1] in bruh and [0,0] in bruh and b[2][2]==0:
         time.sleep(1)
         end_game("Player")
         return
     if [2,0] in bruh and [1,1] in bruh and b[0][2]==0:
         time.sleep(1)
         end_game("Player")
         return
     if [0,2] in bruh and [1,1] in bruh and b[2][0]==0:
         time.sleep(1)
         end_game("Player")
         return
     if [2,0] in bruh and [0,2] in bruh and b[1][1]==0:
         time.sleep(1)
         end_game("Player")
         return
     elif [1,1] in imp:
         can.create_oval(200,150,400,300,outline="black",width=3)
         b[1][1]=1
     elif [0,0] in imp:
         can.create_oval(0,0,200,150,outline="black",width=3)
         b[0][0]=1
     elif [1,0] in imp:
         can.create_oval(200,0,400,150,outline="black",width=3)
         b[1][0]=1
     elif [2,0] in imp:
         can.create_oval(400,0,600,150,outline="black",width=3)
         b[2][0]=1
     elif [1,2] in imp:
         can.create_oval(200,300,400,450,outline="black",width=3)
         b[1][2]=1
     elif [2,2] in imp:
         can.create_oval(400,300,600,450,outline="black",width=3)
         b[2][2]=1
     elif [0,1] in imp:
         can.create_oval(0,150,200,300,outline="black",width=3)
         b[0][1]=1
     elif [0,2] in imp:
         can.create_oval(0,300,200,450,outline="black",width=3)
         b[0][2]=1
     elif [2,1] in imp:
         can.create_oval(400,150,600,300,outline="black",width=3)
         b[2][1]=1
     elif [1,1] in p:
         can.create_oval(200,150,400,300,outline="black",width=3)
         b[1][1]=1
     elif [0,0] in p:
         can.create_oval(0,0,200,150,outline="black",width=3)
         b[0][0]=1
     elif [1,0] in p:
         can.create_oval(200,0,400,150,outline="black",width=3)
         b[1][0]=1
     elif [2,0] in p:
         can.create_oval(400,0,600,150,outline="black",width=3)
         b[2][0]=1
     elif [1,2] in p:
         can.create_oval(200,300,400,450,outline="black",width=3)
         b[1][2]=1
     elif [2,2] in p:
         can.create_oval(400,300,600,450,outline="black",width=3)
         b[2][2]=1
     elif [0,1] in p:
         can.create_oval(0,150,200,300,outline="black",width=3)
         b[0][1]=1
     elif [0,2] in p:
         can.create_oval(0,300,200,450,outline="black",width=3)
         b[0][2]=1
     elif [2,1] in p:
         can.create_oval(400,150,600,300,outline="black",width=3)
         b[2][1]=1
     
            
            
          
b1=can.create_line(200,0,200,450)
b2=can.create_line(400,0,400,450)
b3=can.create_line(0,150,600,150)
b4=can.create_line(0,300,600,300)


qb=t.Button(window, text="Quit", bg="red", fg="white", command=window.quit)
qb.pack(side=t.LEFT, padx=10)


can.bind("<Button-1>", click)
window.mainloop()