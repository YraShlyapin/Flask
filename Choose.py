import getpass
import time

import colorama
import keyboard


class Choose():
    def __init__(self,chooses,starLen = "*"):
        colorama.init()
        self.chooses = chooses
        self.start = starLen
        self.space = " "*len(starLen)
        self.nowChoose = 0
        keyboard.add_hotkey("up",lambda: self.repaint(-1))
        keyboard.add_hotkey("down",lambda:  self.repaint(1))
        keyboard.add_hotkey("enter", lambda: self.finish())
        self.paint()
        self.isTrue = True
        while self.isTrue:
            time.sleep(0.25)
            pass


    def paint(self):
        for index,i in enumerate(self.chooses):
            if index==self.nowChoose:
                print(self.start,end=" ")
            else:
                print(self.space, end=" ")
            print(i)

    def repaint(self,plus):
        # up and clear
        print("\r"+f"\033[{len(self.chooses)-self.nowChoose}A{self.space}",end="")

        print("\r" + f"\033[{len(self.chooses) - self.nowChoose}B", end="")

        self.nowChoose+=plus

        if self.nowChoose > len(self.chooses) - 1:
            self.nowChoose=0
        if self.nowChoose<0:
            self.nowChoose = len(self.chooses)-1
        print("\r" + f"\033[{len(self.chooses) - self.nowChoose}A{self.start}", end="")

        print("\r" + f"\033[{len(self.chooses) - self.nowChoose}B", end="")
        time.sleep(0.1)

    def finish(self):
        getpass.getpass(prompt="")
        print("\033[A",end="")
        keyboard.unhook_all()
        self.isTrue = False

    def __str__(self):
        return str(self.nowChoose+1)

a = Choose(["Егор","Саня","бутерброд"],"*")
print(a)
input()