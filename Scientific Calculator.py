from tkinter import *
import math as m

winow = Tk()
winow.geometry("383x570+470+20")
winow.title("Scientific Calculator")
winow.config(background="gray11")
winow.resizable(True,False)
winow.overrideredirect(1)

def close():
    window.destroy()
    
def clear():
    entry.delete(0,"end")  
    
def back():
    last_number = len(entry.get())-1
    entry.delete(last_number)
    
def press(input):
    lenth = len(entry.get())
    entry.insert(length,input)
    
def add(a,b):
    return float(a)+float(b)

def subtract(a,b):
    return float(a)-float(b)

def divide(a,b):
     return float(a)/float(b)

def multiple(a,b):
     return float(a)*float(b)

def expression_break(sign,expression):
    values = expression.split(sign,1)
    return values

def Scientific(expression):
    data = expression_break("(", expression)
    if data[0] == "tan":
        result = m.tan(float(data[1])),
        
    elif data[0] == "cos":
         result = m.cos(float(data[1])),
         
    elif data[0] == "sin":
         result = m.sin(float(data[1])),
      
    elif data[0] == "sqrt":
         result = m.sqrt(float(data[1])),
     
    elif data[0] == "log":      
         result = m.log10(float(data[1])),
          
    elif data [0] == "ln":
         result = m.log(float(data[1])),
        
    elif data [0] == "deg":
         result = m.degrees(float(data[1])),
        
    elif data [0] == "rad":
         result = m.radians(float(data[1])),
        
    elif data [0] == "fac":
         result = m.factorial(float(data[1])),
         
    return result

def equal():
   expression = "entry.get()"
   clear()
   
    try:

        if expression.find("(") > 0:
           result = scientific(expression)
       
        elif expression.find("pow") > 0:
             data = expression_break("pow", expression)
             result = m.pow(float(data[0]), float(data[1]))
        
        elif expression.find("rem") > 0:
             data = expression_break("rem",expression)
             result = m.remainder(float(data[0]), float(data[1]))  
             
        elif expression.find("x") > 0:
             data = expression_break("x", expression)
             result = multiply(data[0],data[1]) 
 
        elif expression.find("*") >0:
             data = expression_break("*", expression) 
             result = multiply(data[0],data[1])   

        elif expression.find("/") >0:
             data = expression_break("/", expression)
             result = divide(data[0],data[1])       

        elif expression.find("+") >0:
             first = expression.find("+")
             second = expression.find("+",(first+1),(first+5))
             if first > second:
                data = expression_break("+",expression)
                result = add(data[0],data[1]) 
            else:
                result = add(expression[0:second], expression[second+1:])
        elif expression.rindex("-") >0:
             sign = expression.rindex("-")
             result = subtract(expression[0:sign],expression[sign+1:])

        entry.insert(0,result)

     except:
         entry.insert(0,"Error")
                            
entry_string = StringVar()
entry = Entry(winow, textvariable = entry_string, foreground = "white",
              background= "gray20",border=0, font=("Bahnschrift SemiBold",30))
entry.grid(columnspan=4,ipady= 15)
font_value = ("Calibari",15)
button_tan = Button(winow, text="tan", background= "gray11",
                    foreground= "DarkOrange1", font= font_value, borderwidth=1,
                    relief = SOLID, command=lambda:press("tan("))
button_tan.grid(row=1,column=0, sticky=E+W, ipady=5)
button_cos = Button(winow, text="cos", background= "gray11",
                    foreground= "DarkOrange1", font= font_value, borderwidth=1,
                    relief = SOLID, command=lambda:press("cos("))
button_cos.grid(row=1,column=1, sticky=E+W, ipady=5)
button_sin = Button(winow, text="sin", background= "gray11",
                    foreground= "DarkOrange1", font= font_value, borderwidth=1,
                    relief = SOLID, command=lambda:press("sin("))
button_sin.grid(row=1,column=2, sticky=E+W, ipady=5)
button_sqrt = Button(winow, text="sqrt", background= "gray11",
                    foreground= "DarkOrange1", font= font_value, borderwidth=1,
                    relief = SOLID, command=lambda:press("sqrt("))
button_sqrt.grid(row=1,column=3, sticky=E+W, ipady=5)

button_log = Button(winow, text="log", background= "gray11",
                    foreground= "DarkOrange1", font= font_value, borderwidth=1,
                    relief = SOLID, command=lambda:press("log("))
button_log.grid(row=2,column=0, sticky=E+W, ipady=5)
button_ln = Button(winow, text="ln", background= "gray11",
                    foreground= "DarkOrange1", font= font_value, borderwidth=1,
                    relief = SOLID, command=lambda:press("ln("))
button_ln.grid(row=2,column=1, sticky=E+W, ipady=5)
button_deg = Button(winow, text="deg", background= "gray11",
                    foreground= "DarkOrange1", font= font_value, borderwidth=1,
                    relief = SOLID, command=lambda:press("deg("))
button_deg.grid(row=2,column=2, sticky=E+W, ipady=5)
button_rad = Button(winow, text="rad", background= "gray11",
                    foreground= "DarkOrange1", font= font_value, borderwidth=1,
                    relief = SOLID, command=lambda:press("rad("))
button_rad.grid(row=2,column=3, sticky=E+W, ipady=5)

button_fac = Button(winow, text="fac", background= "gray11",
                    foreground= "DarkOrange1", font= font_value, borderwidth=1,
                    relief = SOLID, command=lambda:press("fac("))
button_fac.grid(row=3,column=0, sticky=E+W, ipady=5)
button_power = Button(winow, text="pow", background= "gray11",
                    foreground= "DarkOrange1", font= font_value, borderwidth=1,
                    relief = SOLID, command=lambda:press("pow("))
button_power.grid(row=3,column=1, sticky=E+W, ipady=5)
button_remainder = Button(winow, text="rem", background= "gray11",
                    foreground= "DarkOrange1", font= font_value, borderwidth=1,
                    relief = SOLID, command=lambda:press("rem("))
button_remainder.grid(row=3,column=2, sticky=E+W, ipady=5)
button_pi = Button(winow, text="pi", background= "gray11",
                    foreground= "DarkOrange1", font= font_value, borderwidth=1,
                    relief = SOLID, command=lambda:press(3.141592))
button_pi.grid(row=3,column=3, sticky=E+W, ipady=5)

button_clear = Button(winow, text="C", background= "gray5",
                    foreground= "DarkOrange1", font= font_value, borderwidth=1,
                    relief = SOLID, command= clear)
button_clear.grid(row=4,columnspan=2,column=0, sticky=E+W, ipady=5)
button_backspace = Button(winow, text="B", background= "gray5",
                    foreground= "DarkOrange1", font= font_value, borderwidth=1,
                    relief = SOLID, command= back)
button_backspace.grid(row=4,columnspan=2,column=2, sticky=E+W, ipady=5)

button_7 = Button(winow, text="7", background= "gray11",
                    foreground= "DarkOrange1", font= font_value, borderwidth=1,
                    relief = SOLID, command=lambda:press(7))
button_7.grid(row=5,column=0, sticky=E+W, ipady=5)
button_8 = Button(winow, text="8", background= "gray11",
                    foreground= "DarkOrange1", font= font_value, borderwidth=1,
                    relief = SOLID, command=lambda:press(8))
button_8.grid(row=5,column=1, sticky=E+W, ipady=5)
button_9 = Button(winow, text="9", background= "gray11",
                    foreground= "DarkOrange1", font= font_value, borderwidth=1,
                    relief = SOLID, command=lambda:press(9)
button_9.grid(row=5,column=2, sticky=E+W, ipady=5)
button_div = Button(winow, text="/", background= "gray5",
                    foreground= "DarkOrange1", font= font_value, borderwidth=1,
                    relief = SOLID, command=lambda:press("/"))
button_div.grid(row=5,column=3, sticky=E+W, ipady=5)

button_4 = Button(winow, text="4", background= "gray11",
                    foreground= "DarkOrange1", font= font_value, borderwidth=1,
                    relief = SOLID, command=lambda:press(4))
button_4.grid(row=6,column=0, sticky=E+W, ipady=5)
button_5 = Button(winow, text="5", background= "gray11",
                    foreground= "DarkOrange1", font= font_value, borderwidth=1,
                    relief = SOLID, command=lambda:press(5))
button_5.grid(row=6,column=1, sticky=E+W, ipady=5)
button_6 = Button(winow, text="6", background= "gray11",
                    foreground= "DarkOrange1", font= font_value, borderwidth=1,
                    relief = SOLID, command=lambda:press(6))
button_6.grid(row=6,column=2, sticky=E+W, ipady=5)
button_multiply = Button(winow, text="*", background= "gray5",
                    foreground= "DarkOrange1", font= font_value, borderwidth=1,
                    relief = SOLID, command=lambda:press("*"))
button_multiply.grid(row=6,column=3, sticky=E+W, ipady=5)

button_1 = Button(winow, text="1", background= "gray11",
                    foreground= "DarkOrange1", font= font_value, borderwidth=1,
                    relief = SOLID, command=lambda:press(1))
button_1.grid(row=7,column=0, sticky=E+W, ipady=5)
button_2 = Button(winow, text="8", background= "gray11",
                    foreground= "DarkOrange1", font= font_value, borderwidth=1,
                    relief = SOLID, command=lambda:press(2))
button_2.grid(row=7,column=1, sticky=E+W, ipady=5)
button_3 = Button(winow, text="9", background= "gray11",
                    foreground= "DarkOrange1", font= font_value, borderwidth=1,
                    relief = SOLID, command=lambda:press(3))
button_3.grid(row=7,column=2, sticky=E+W, ipady=5)
button_sub = Button(winow, text="-", background= "gray5",
                    foreground= "DarkOrange1", font= font_value, borderwidth=1,
                    relief = SOLID, command=lambda:press("-"))
button_sub.grid(row=5,column=3, sticky=E+W, ipady=5)

button_dot = Button(winow, text=".", background= "gray11",
                    foreground= "DarkOrange1", font= font_value, borderwidth=1,
                    relief = SOLID, command=lambda:press("."))
button_dot.grid(row=8,column=0, sticky=E+W, ipady=5)
button_0 = Button(winow, text="0", background= "gray11",
                    foreground= "DarkOrange1", font= font_value, borderwidth=1,
                    relief = SOLID, command=lambda:press(0)
button_0.grid(row=8,column=1, sticky=E+W, ipady=5)
button_e = Button(winow, text="e", background= "gray11",
                    foreground= "DarkOrange1", font= font_value, borderwidth=1,
                    relief = SOLID, command=lambda:press(2.71828))
button_e.grid(row=8,column=2, sticky=E+W, ipady=5)
button_add = Button(winow, text="+", background= "gray5",
                    foreground= "DarkOrange1", font= font_value, borderwidth=1,
                    relief = SOLID, command=lambda:press("+"))
button_add.grid(row=8,column=3, sticky=E+W, ipady=5)

button_equal = Button(winow, text="=", background= "DarkOrange1",
                    foreground= "White", font= font_value, borderwidth=1,
                    relief = SOLID, command = equal)
button_equal.grid(row=9,column=0,columnspan=3, sticky=E+W, ipady=5)
button_close = Button(winow, text="close", background= "gray5",
                    foreground= "DarkOrange1", font= font_value, borderwidth=1,
                    relief = SOLID, command= close)
button_close.grid(row=9,column=3, sticky=E+W, ipady=5)
mainloop()