import turtle as t
#import random as r

def rbaum (age=100):
    """paint a recursiv tree"""
    if age < 5:
        return
    t.pd()
    t. fd(age)
    t. rt(45)
    rbaum(age/2)
    t. lt(90)
    rbaum(age/2)
    t. rt(45)
    t. pu()
    t. fd(-age)
    return

if __name__=="__main__":
    t. speed(0)
    t. home()
    t. clear()
    t. lt(90)
    t. pu()
    t. fd(-200)
    rbaum ()
