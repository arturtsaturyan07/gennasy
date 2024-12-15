import customtkinter as ctk
import numpy as np
import matplotlib.pyplot as plt
import math
from tkinter import messagebox

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")  

root = ctk.CTk()
root.geometry("1000x800")
root.title("Genassy")

def start_page():
    delate_pages()
    start_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
    start_frame.pack(pady=20)
    
    welcome_label = ctk.CTkLabel(
        start_frame,
        text="Բարև, Բարի գալուստ, Genasy",
        font=("Bold", 35),
        text_color="black"
    )
    welcome_label.pack(pady=100)

def hide_indicators():
    home_indicate.configure(fg_color='#c3c3c3')
    info_indicate.configure(fg_color='#c3c3c3')

def delate_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()


def indicate(lb, page):
    hide_indicators()
    lb.configure(fg_color="#159aff") 
    delate_pages()
    page()

def home_page():
    delate_pages()
    home_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
    home_frame.pack(pady=20)
    
    lb = ctk.CTkLabel(
        home_frame,
        text="Գլխավոր էջ\nՆախագծային աշխատանքներ",
        font=("Bold", 35),
        text_color="black"
    )
    lb.pack(pady=100)
    
    mathnax_button = ctk.CTkButton(
        main_frame,
        text="Հանրահաշիվ",
        font=("Bold", 20),
        command=show_mathnax_info,
        hover_color="#a3a3a3",
    )
    mathnax_button.place(x=150, y=300)
    
    pythonnax_button = ctk.CTkButton(
        main_frame,
        text="Python",
        font=("Bold", 20),
        command=show_pythonnax_info,
        hover_color="#a3a3a3",
    )
    pythonnax_button.place(x=150, y=370)
    
    home_frame.pack(pady=20)

def info_page():
    delate_pages()
    info_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
    info_frame.pack(pady=20)
    
    lb = ctk.CTkLabel(
        info_frame,
        text="Տեղեկություն",
        font=("Bold", 35),
        text_color="black"
    )
    lb.pack(pady=100)

def show_graph_info():
    delate_pages()
    graph_label = ctk.CTkLabel(main_frame, text="Գրաֆիկների կառուցում", font=('Bold', 35), text_color = 'black')
    graph_label.pack(pady=100)

    def btn_delete():
        name_func.delete(0, 'end')
    
    def btn_click():
        expression = name_func.get() 
        if not expression:
            return messagebox.showerror("Error", "Please enter a function.")
        
        try:
            x = np.linspace(-10, 10, 400)  
            y = eval(expression, {"x": x, "np": np}) 
            y1 = np.linspace(-10, 10, 400)
            
            plt.figure(figsize=(8, 6))
            plt.plot(x, y, label=expression)
            plt.xlabel("x")
            plt.ylabel("y")
            plt.title("Graph of " + expression)
            plt.legend()
            plt.grid(True)

            #plt.plot(0, y1)

            plt.show()
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")


    btn1 = ctk.CTkButton(main_frame, text = 'show', fg_color = 'red', command = btn_click)
    btn1.place(relx = 0.05, rely = 0.85, relheight = 0.05, relwidth = 0.1)
    btn2 = ctk.CTkButton(main_frame, text = 'delete', fg_color = 'red', command = btn_delete)
    btn2.place(rely = 0.85, relx = 0.85,  relheight = 0.05, relwidth = 0.1)


    name_func = ctk.CTkEntry(main_frame, fg_color = 'white', text_color = 'black')
    name_func.place(rely = 0.5, relx = 0.25, relwidth = 0.45)

    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=home_page)
    back_button.place(x=780, y=750)

def show_mathnax4_info():
    delate_pages()
    graph_label = ctk.CTkLabel(main_frame, text="Հաշվարկների մաս", font=('Bold', 35), text_color = 'black')
    graph_label.pack(pady=100)

    def btn_delete():
        name_func1.delete(0, 'end')
        name_func2.delete(0, 'end')
    
    def btn_click1():
        expression1 = name_func1.get()
        expression2 = name_func2.get() 
        try:
            text_content = (
            f"Ոսկու գրավով՝ {int(expression1) * (113/100)*int(expression2)}\n",
            f"Տան գրավով՝ {int(expression1) * (115/100)*int(expression2)}\n",
            f"Սովորական գրավով՝ {int(expression1) * (119/100)*int(expression2)}")
            mathnax1_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
            mathnax1_text.place(x=50, y=400)
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")


    btn1 = ctk.CTkButton(main_frame, text = 'show', fg_color = 'red', command = btn_click1)
    btn1.place(relx = 0.05, rely = 0.85, relheight = 0.05, relwidth = 0.1)
    btn2 = ctk.CTkButton(main_frame, text = 'delete', fg_color = 'red', command = btn_delete)
    btn2.place(rely = 0.85, relx = 0.85,  relheight = 0.05, relwidth = 0.1)


    name_func1 = ctk.CTkEntry(main_frame, fg_color = 'white', text_color = 'black', placeholder_text='Տարիների քանակ')
    name_func1.place(rely = 0.4, relx = 0.05, relwidth = 0.45)
    name_func2 = ctk.CTkEntry(main_frame, fg_color = 'white', text_color = 'black', placeholder_text='Գումար')
    name_func2.place(rely = 0.4, relx = 0.53, relwidth = 0.45)

    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=home_page)
    back_button.place(x=780, y=750)

def show_mathnax_info():
    delate_pages()
    mathnax_label = ctk.CTkLabel(main_frame, text="Նախագծային աշխատանք\n       Հանրահաշվից", font=('Bold', 35), text_color = "black")
    mathnax_label.pack(pady=100)
    mathnax1_button = ctk.CTkButton(main_frame, text="Նախագծի անդամների պատասխանատվությանը", font=('Bold', 20), command=show_mathnax1_info)
    mathnax1_button.place(x=100, y=300)
    mathnax2_button = ctk.CTkButton(main_frame, text="Նախագծի Նպատակը", font=('Bold', 20), command=show_mathnax2_info)
    mathnax2_button.place(x=100, y=370)
    mathnax3_button = ctk.CTkButton(main_frame, text="Եզրակացություն", font=('Bold', 20), command=show_mathnax3_info)
    mathnax3_button.place(x=100, y=440)
    mathnax4_button = ctk.CTkButton(main_frame, text="Պրոդուկտ", font=('Bold', 20), command=show_mathnax4_info) 
    mathnax4_button.place(x=100, y=510)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=home_page)
    back_button.place(x=780, y=750)

def show_mathnax3_info():
    delate_pages()
    mathnax_label = ctk.CTkLabel(main_frame, text="Եզրակացություն", font=('Bold', 35), text_color='black')
    mathnax_label.pack(pady=100)
    text_content = (
        "       Բազմաթիվ հաշվարկներից հետո ստացանք բանաձևեր\n"
        "կապված վարկերի, ավանդների և ինֆլյացիայի հետ։")
    mathnax1_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color = 'black')
    mathnax1_text.place(x=10, y=250)
    mathnax31_button = ctk.CTkButton(main_frame, text="Ինֆլ. և ավանդ", font=('Bold', 20), command=show_mathnax31_info)
    mathnax31_button.place(x=100, y=400)
    mathnax32_button = ctk.CTkButton(main_frame, text="Ինֆլ. և վարկեր(ոսկու գրավ)", font=('Bold', 20), command=show_mathnax32_info)
    mathnax32_button.place(x=100, y=470)
    mathnax33_button = ctk.CTkButton(main_frame, text="Ինֆլ. և վարկեր(տան գրավ)", font=('Bold', 20), command=show_mathnax33_info)
    mathnax33_button.place(x=100, y=540)
    mathnax34_button = ctk.CTkButton(main_frame, text="Ինֆլ. և վարկեր(սովորական)", font=('Bold', 20), command=show_mathnax34_info)
    mathnax34_button.place(x=100, y=610)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_mathnax_info)
    back_button.place(x=780, y=750)

def show_mathnax34_info():
    delate_pages()
    mathnax_label = ctk.CTkLabel(main_frame, text="Ինֆլ. և վարկեր(սովորական)", font=('Bold', 35), text_color='black')
    mathnax_label.pack(pady=100)
    text_content = (
        "\n       4.Ինֆլ. և վարկեր։ Դիտարկենք սովորական վարկը\n"
        "որը տրվում է y=p(119/100)*xբանաձևով:Եթե վարկով\n"
        "գումար վերցնենք և դնենք գործի մեջ\n"
        "ապա այն կենթարկվիինֆլյացիայի։\n"
        "Օգուտ կտեսնենք p(114/100)^x > p(119/100)*x դեպքում,\n"
        "արդյունքը ակնառու կլինի x>=6 դեպքում՝ երբ տարիները\n"
        "6-ից մեծ են, որը իրատեսական է։")
    mathnax1_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    mathnax1_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_mathnax3_info)
    back_button.place(x=780, y=750)

def show_mathnax33_info():
    delate_pages()
    mathnax_label = ctk.CTkLabel(main_frame, text="Ինֆլ. և վարկեր(տան գրավ)", font=('Bold', 35), text_color='black')
    mathnax_label.pack(pady=100)
    text_content = (
        "\n       3.Ինֆլ. և վարկեր։ Դիտարկենք տան գրավը որը տրվում է\n"
        "y=p(115/100)*xբանաձևով:Եթե վարկով գումար վերցնենք և\n"
        "դնենք գործի մեջ ապա այն կենթարկվի ինֆլյացիայի։\n"
        "Օգուտ կտեսնենք p(114/100)^x > p(115/100)*x դեպքում,\n"
        "արդյունքը ակնառու կլինի x>=3 դեպքում՝ երբ տարիները\n"
        "3-ից մեծ են, որը շահութաբեր կլինի։։")
    mathnax1_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    mathnax1_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_mathnax3_info)
    back_button.place(x=780, y=750)

def show_mathnax32_info():
    delate_pages()
    mathnax_label = ctk.CTkLabel(main_frame, text="Ինֆլ. և վարկեր(ոսկու գրավ)", font=('Bold', 35), text_color='black')
    mathnax_label.pack(pady=100)
    text_content = (
        "\n       2.Ինֆլ. և վարկեր։ Դիտարկենք ոսկու գրավը որը տրվում է\n"
        "y=p(113/100)*xբանաձևով:Եթե վարկով գումար վերցնենք\n"
        "և դնենք գործի մեջ ապա այն կենթարկվի ինֆլյացիայի։\n"
        "Օգուտ կտեսնենք p(114/100)^x > p(113/100)*x դեպքում,\n"
        "արդյունքը ակնառու կլինի  x>=2 դեպքում՝ երբ տարիները\n"
        "2-ից մեծ են, իսկ բանկերըտրամադրում ենառավելագույնը\n"
        "2 տարով, որը այդքան էլ ձեռնտու չէ։")
    mathnax1_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    mathnax1_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_mathnax3_info)
    back_button.place(x=780, y=750)


def show_mathnax31_info():
    delate_pages()
    mathnax_label = ctk.CTkLabel(main_frame, text="Ինֆլ. և ավանդ", font=('Bold', 35), text_color='black')
    mathnax_label.pack(pady=100)
    text_content = (
        "\n       1.Ինֆլ. և ավանդ ։ Այդքան էլ արդյունավել չէ գումարը\n"
        "ավանդ դնել,բայց եթե հնարավոր չէ գումարը օգտագործել գործի\n"
        "մեջ այդ դեպքում ավելի նպատակահարմար է հենց ավանդ դնելը։ \n")
    mathnax1_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    mathnax1_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_mathnax3_info)
    back_button.place(x=780, y=750)

def show_mathnax2_info():
    delate_pages()
    mathnax_label = ctk.CTkLabel(main_frame, text="Նախագծի Նպատակը", font=('Bold', 35), text_color='black')
    mathnax_label.pack(pady=100)
    text_content = (
        "\n       Ուսումնասիրել ավանդները, վարկերը, ինֆլացիան,\n"
        "կատարել հետազոտական աշխատանք և գալ եզրահանգման\n"
        "ֆինանսական գործարքներում։")
    mathnax1_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    mathnax1_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_mathnax_info)
    back_button.place(x=780, y=750)

def show_mathnax1_info():
    delate_pages()
    mathnax_label = ctk.CTkLabel(main_frame, text=" Նախագծի անդամների\nպատասխանատվությանը", font=('Bold', 35), text_color='black')
    mathnax_label.pack(pady=100)
    text_content = (
        "\nՆազարյան Սերյոժա - Տվյալների վերլուծում,եզրակացություններ\n"
        "Պապյան Նարե - Դիզայն,պրեզենտացիայի պատրաստում\n"
        "Մակարյան Էրիկ - Դիզայն,պրեզենտացիայի պատրաստում\n"
        "Թովմասյան Սերգո - Ֆունկցիայի հետազոտում,\n"
        "                                  կապը Ֆիշերի բանաձևի հետ\n"
        "Ծատուրյան Արթուր - Ֆունկցիայի հետազոտում,\n"
        "                                   կապը Ֆիշերի բանաձևի հետ\n"
        "Վերանյան Յուրի - Տվյալների որոնում ,մշակում,փոխանցում\n"
        "Նազարյան Գագիկ - Տվյալների որոնում ,մշակում,փոխանցում")
    mathnax1_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    mathnax1_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_mathnax_info)
    back_button.place(x=780, y=750)

def show_pythonnax_info():
    delate_pages()
    python_label = ctk.CTkLabel(main_frame, text="Նախագծային աշխատանք\n           Python-ից", font=('Bold', 35), text_color='black')
    python_label.pack(pady=100)
    python_button = ctk.CTkButton(main_frame, text="Python", font=('Bold', 20), command=show_python_info)
    python_button.place(x=100, y=300)
    math_button = ctk.CTkButton(main_frame, text="Մաթեմատիկա", font=('Bold', 20), command=show_math_info)
    math_button.place(x=100, y=370)
    graph_button = ctk.CTkButton(main_frame, text="Գրաֆիկների կառուցում", font=('Bold', 20), command=show_graph_info)
    graph_button.place(x=100, y=450)
    calculator_button = ctk.CTkButton(main_frame, text="Հաշվիչ", font=('Bold', 20), command=show_calculator_info)
    calculator_button.place(x=100, y=520)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=home_page)
    back_button.place(x=780, y=750)
    
def show_python_info():
    delate_pages()
    python_label = ctk.CTkLabel(main_frame, text="Python-ը հզոր լեզու է!", font=('Bold', 35), text_color='black')
    python_label.pack(pady=100)
    show_Python_Concepts_for_Beginners_button = ctk.CTkButton(main_frame, text="Python-ի սկզբունքներ սկսնակների համար", font=('Bold', 20), command=show_Python_Concepts_for_Beginners)
    show_Python_Concepts_for_Beginners_button.place(x=150, y=240)
    show_Python_Concepts_for_Mid_Level_button = ctk.CTkButton(main_frame, text="Python-ի սկզբունքներ միջին մակարդակի համար", font=('Bold', 20), command=show_Python_Concepts_for_Mid_Level)
    show_Python_Concepts_for_Mid_Level_button.place(x=150, y=310)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_pythonnax_info)
    back_button.place(x=780, y=750)

def show_calculator_info():
    root = ctk.CTk()
    root.title("Scientific Calculator")
    root.geometry("410x500+100+200") 
    root.resizable(False, False)
    root.configure(fg_color="#171616")

    equation = ""
    label_result = ctk.CTkLabel(root, width=25, height=2, text="", font=("Arial", 30), fg_color="#171616", text_color="white") 
    label_result.pack()

    def show(value):
        nonlocal equation
        equation += str(value)
        label_result.configure(text=equation)

    def clear():
        nonlocal equation
        equation = ""
        label_result.configure(text=equation)
        
    def calculate():
        nonlocal equation
        result = ""
        if equation != "":
            try:
                equation = equation.replace("^", "**")
                result = str(eval(equation))
            except:
                result = "Error"
        equation = result
        label_result.configure(text=equation)

    def log_function():
        nonlocal equation
        try:
            value = float(equation)
            if value <= 0: 
                raise ValueError("Log undefined for non-positive values")
            result = str(math.log(value))  
            equation = result
        except:
            equation = "Error"
        label_result.config(text=equation)

    def log_base_function():
        nonlocal equation
        try:
            if ',' in equation:
                base, number = equation.split(",")
                base = float(base)
                number = float(number)
                if base <= 0 or base == 1 or number <= 0:
                    raise ValueError("Invalid input values")
                result = str(math.log(number, base))
            else:
                equation = "Error"
                result = "Error"
        except:
            result = "Error"
       
        equation = result
        label_result.configure(text=equation)

    def power_function():
        nonlocal equation
        try:
            base, exponent = equation.split(",")
            base = float(base)
            exponent = float(exponent)
            result = str(base ** exponent)  
            equation = result
        except:
            equation = "Error"
        label_result.configure(text=equation)

    def sin_function():
        nonlocal equation
        try:
            angle = float(equation)
            result = str(math.sin(math.radians(angle))) 
            equation = result
        except:
            equation = "Error"
        label_result.configure(text=equation)

    def cos_function():
        nonlocal equation
        try:
            angle = float(equation)
            result = str(math.cos(math.radians(angle)))
            equation = result
        except:
            equation = "Error"
        label_result.configure(text=equation)

    def tan_function():
        nonlocal equation
        try:
            angle = float(equation)
            result = str(math.tan(math.radians(angle))) 
            equation = result
        except:
            equation = "Error"
        label_result.configure(text=equation)
        
    button_data = [
        ("C", clear, 10, 105), ("/", lambda: show("/"), 310, 235), ("%", lambda: show("%"), 110, 105), ("*", lambda: show("*"), 310, 300),
        ("7", lambda: show("7"), 10, 235), ("8", lambda: show("8"), 110, 235), ("9", lambda: show("9"), 210, 235), ("-", lambda: show("-"), 310, 365),
        ("4", lambda: show("4"), 10, 300), ("5", lambda: show("5"), 110, 300), ("6", lambda: show("6"), 210, 300), ("+", lambda: show("+"), 310, 430),
        ("1", lambda: show("1"), 10, 365), ("2", lambda: show("2"), 110, 365), ("3", lambda: show("3"), 210, 365), ("0", lambda: show("0"), 10, 430),
        (".", lambda: show("."), 110, 430), ("=", calculate, 210, 430), ("x^y", lambda: show("^"), 310, 170),  
        ("log", log_function, 210, 105),  
        ("log(base)", lambda: show(","), 310, 105),  
        ("sin", sin_function, 10, 170),  
        ("cos", cos_function, 110, 170),  
        ("tan", tan_function, 210, 170),
    ]
    
    for (text, command, x, y) in button_data:
        if text == "=": 
            ctk.CTkButton(root, text=text, width=5, height=1, font=("Arial", 20, "bold"), border_width=1, text_color="#fff", fg_color="#FFA500", command=command).place(x=x, y=y)
        else:
            ctk.CTkButton(root, text=text, width=5, height=1, font=("Arial", 20, "bold"), border_width=1, text_color="#fff", fg_color="#2a2d36", command=command).place(x=x, y=y)

def show_math_info():
    delate_pages()
    math_label = ctk.CTkLabel(main_frame, text="Մաթեմատիկան անհրաժեշտ է \n     ծրագրավորման համար!", font=('Bold', 35), text_color='black')
    math_label.pack(pady=100)
    show_Math_10class_1Term_button = ctk.CTkButton(main_frame, text="Մաթեմատիկա 10-րդ դասարան 1-ին կիսամյակ", font=('Bold', 20), command=show_Math_10class_1Term)
    show_Math_10class_1Term_button.place(x=100, y=240)
    show_Math_10class_2Term_button = ctk.CTkButton(main_frame, text="Մաթեմատիկա 10-րդ դասարան 2-րդ կիսամյակ", font=('Bold', 20), command=show_Math_10class_2Term)
    show_Math_10class_2Term_button.place(x=100, y=310)
    show_Math_11class_1Term_button = ctk.CTkButton(main_frame, text="Մաթեմատիկա 11-րդ դասարան 1-ին կիսամյակ", font=('Bold', 20), command=show_Math_11class_1Term)
    show_Math_11class_1Term_button.place(x=100, y=380)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_pythonnax_info)
    back_button.place(x=780, y=750)

def show_Python_Concepts_for_Beginners():
    delate_pages()
    python_label = ctk.CTkLabel(main_frame, text="Python-ի սկզբունքներ\nսկսնակների համարը", font=('Bold', 35), text_color='black')
    python_label.pack(pady=100)
    Input_and_Output_button = ctk.CTkButton(main_frame, text="Մուտք և Ելք", font=('Bold', 20), command=show_Input_and_Output_info)
    Input_and_Output_button.place(x=100, y=240)
    Variables_and_Types_button = ctk.CTkButton(main_frame, text="Փոփոխականներ և Տեսակներ", font=('Bold', 20), command=show_Variables_and_Types_info)
    Variables_and_Types_button.place(x=100, y=310)
    Conditional_Operators_button = ctk.CTkButton(main_frame, text="Պայմանների Օպերատորներ", font=('Bold', 20), command=show_Conditional_Operators_info)
    Conditional_Operators_button.place(x=100, y=380)
    String_button = ctk.CTkButton(main_frame, text="Տող", font=('Bold', 20), command=show_String_info)
    String_button.place(x=100, y=450)
    Lists_button = ctk.CTkButton(main_frame, text="Ցուցակներ", font=('Bold', 20), command=show_Lists_info)
    Lists_button.place(x=100, y=520)
    Loops_button = ctk.CTkButton(main_frame, text="Ցիկլեր", font=('Bold', 20), command=show_Loops_info)
    Loops_button.place(x=100, y=590)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_python_info)
    back_button.place(x=780, y=750)
  
def show_Python_Concepts_for_Mid_Level():
    delate_pages()
    python_label = ctk.CTkLabel(main_frame, text="   Python-ի սկզբունքներ\nմիջին մակարդակի համարը", font=('Bold', 35), text_color='black')
    python_label.pack(pady=100)
    List_Comprehension_button = ctk.CTkButton(main_frame, text="List Comprehension", font=('Bold', 20), command=show_List_Comprehension_info)
    List_Comprehension_button.place(x=100, y=240)
    Nested_Loops_button = ctk.CTkButton(main_frame, text="Ներդրված ցիկլեր", font=('Bold', 20), command=show_Nested_Loops_info)
    Nested_Loops_button.place(x=100, y=310)
    Dictionaries_button = ctk.CTkButton(main_frame, text="Dict", font=('Bold', 20), command=show_Dictionaries_info)
    Dictionaries_button.place(x=100, y=380)
    Functions_button = ctk.CTkButton(main_frame, text="Ֆունկցիաներ", font=('Bold', 20), command=show_Functions_info)
    Functions_button.place(x=100, y=450)
    Recursion_button = ctk.CTkButton(main_frame, text="Ռեկուրսիա", font=('Bold', 20), command=show_Recursion_info)
    Recursion_button.place(x=100, y=520)
    Tuples_and_Sets_button = ctk.CTkButton(main_frame, text="Tuple-ներ և Set-եր", font=('Bold', 20), command=show_Tuples_and_Sets_info)
    Tuples_and_Sets_button.place(x=100, y=590)
    Lambda_Functions_button = ctk.CTkButton(main_frame, text="Լամբդա ֆունկցիաներ", font=('Bold', 20), command=show_Lambda_Functions_info)
    Lambda_Functions_button.place(x=100, y=660)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_python_info)
    back_button.place(x=780, y=750)

def show_Math_10class_1Term():
    delate_pages()
    python_label = ctk.CTkLabel(main_frame, text="Մաթեմատիկա 10-րդ դասարան \n            1-ին կիսամյակ", font=('Bold', 35), text_color='black')
    python_label.pack(pady=100)
    Real_Numbers_button = ctk.CTkButton(main_frame, text="Իրական թվեր", font=('Bold', 20), command=show_Real_Numbers)
    Real_Numbers_button.place(x=100, y=260)
    Element_of_Trigonometry_button = ctk.CTkButton(main_frame, text="Եռանկյունաչափության տարրեր", font=('Bold', 20), command=show_Element_of_Trigonometry)
    Element_of_Trigonometry_button.place(x=100, y=330)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_math_info)
    back_button.place(x=780, y=750)

def show_Math_10class_2Term():
    delate_pages()
    python_label = ctk.CTkLabel(main_frame, text="Մաթեմատիկա 10-րդ դասարան \n             2-րդ կիսամյակ", font=('Bold', 35), text_color='black')
    python_label.pack(pady=100)
    Function_button = ctk.CTkButton(main_frame, text="Ֆունկցիա", font=('Bold', 20), command=show_Function)
    Function_button.place(x=80, y=260)
    Trigonometric_Functions_and_Equations_button = ctk.CTkButton(main_frame, text="Եռանկյունաչափական ֆունկցիաներ և հավասարումներ", font=('Bold', 20), command=show_Trigonometric_Functions_and_Equations)
    Trigonometric_Functions_and_Equations_button.place(x=80, y=330)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_math_info)
    back_button.place(x=780, y=750)

def show_Math_11class_1Term():
    delate_pages()
    python_label = ctk.CTkLabel(main_frame, text="Մաթեմատիկա 11-րդ դասարան \n              1-ին կիսամյակ", font=('Bold', 35), text_color='black')
    python_label.pack(pady=100)
    Scalar_Functions_button = ctk.CTkButton(main_frame, text="Ցուցչային ֆունկցիաներ", font=('Bold', 20), command=show_Scalar_Function)
    Scalar_Functions_button.place(x=100, y=260)
    Pointar_Function_button = ctk.CTkButton(main_frame, text="Աստիճանային ֆունկցիաներ", font=('Bold', 20), command=show_Pointar_Function)
    Pointar_Function_button.place(x=100, y=330)
    Log_Function_button = ctk.CTkButton(main_frame, text="Լոգարիթմական ֆունկցիաներ", font=('Bold', 20), command=show_Log_Function)
    Log_Function_button.place(x=100, y=400)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_math_info)
    back_button.place(x=780, y=750)


def show_Real_Numbers():
    delate_pages()
    Real_Numbers = ctk.CTkLabel(main_frame, text="Իրական թվեր", font=('Bold', 35), text_color='black')
    Real_Numbers.pack(pady=100)
    Real_Numbers_Defiition_button = ctk.CTkButton(main_frame, text="Սահմանում", font=('Bold', 20), command=show_Real_Numbers_Defiition)
    Real_Numbers_Defiition_button.place(x=100, y=260)
    Real_Numbers_Types_button = ctk.CTkButton(main_frame, text="Տեսակներ", font=('Bold', 20), command=show_Real_Numbers_Types)
    Real_Numbers_Types_button.place(x=100, y=330)
    Real_Numbers_Properties_button = ctk.CTkButton(main_frame, text="Հատկություններ", font=('Bold', 20), command=show_Real_Numbers_Properties)
    Real_Numbers_Properties_button.place(x=100, y=400)
    Real_Numbers_Presentation_button = ctk.CTkButton(main_frame, text="Թվային առանցքով ներկայացումը", font=('Bold', 20), command=show_Real_Numbers_Presentation)
    Real_Numbers_Presentation_button.place(x=100, y=470)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Math_10class_1Term)
    back_button.place(x=780, y=750)

def show_Real_Numbers_Defiition():
    delate_pages()
    show_Real_Numbers_Defiition = ctk.CTkLabel(main_frame, text="Իրական թվերի սահմանումը", font=('Bold', 35), text_color='black')
    show_Real_Numbers_Defiition.pack(pady=100)
    text_content = (
        "\n       Իրական թվերը ներառում են ցանկացած արժեք, որը\n"
        "կարելի է ներկայացնել թվաբանական գծի վրա՝ բացասականից \n"
        "մինչև դրական անսահմանություն: Դրանք բաղկացած են թե՛\n"
        "ռացիոնալ թվերից (որոնք կարելի է գրել կոտորակներով), և թե՛\n"
        "իռացիոնալ թվերից (որոնք հնարավոր չէ արտահայտել ճիշտ\n"
        "կոտորակներով, օրինակ՝ π-ն կամ √2-ը):")
    real_numbers_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    real_numbers_text.place(x=10, y=200)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Real_Numbers)
    back_button.place(x=780, y=750)

def show_Real_Numbers_Types():
    delate_pages()
    show_Real_Numbers_Defiition = ctk.CTkLabel(main_frame, text="Իրական թվերի տեսակները", font=('Bold', 35), text_color='black')
    show_Real_Numbers_Defiition.pack(pady=100)
    text_content = (
        "\n       Բնական թվեր (1, 2, 3, …): դրական ամբողջ թվեր։\n"
        "Ամբողջ թվեր (0, 1, 2, 3, …): դրական թվեր և զրո։\n"
        "Համընդհանուր թվեր (…, -2, -1, 0, 1, 2, …): դրական,\n"
        "բացասական թվեր և զրո։\n"
        "Ռացիոնալ թվեր: Թվեր, որոնք կարելի է արտահայտել\n"
        "կոտորակներով (օր.՝ 1/2, 3, 0.75), \n"
        "ներառյալ վերջավոր և կրկնվող դեցիմալները։\n"
        "Իռացիոնալ թվեր: Թվեր, որոնք հնարավոր չէ արտահայտել\n"
        "կոտորակներով և ունեն անվերջ, \n"
        "չկրկնվող դեցիմալ (օր.՝ √2, π):\n\n")
    real_numbers_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    real_numbers_text.place(x=10, y=200)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command= show_Real_Numbers)
    back_button.place(x=780, y=750)

def show_Real_Numbers_Properties():
    delate_pages()
    show_Real_Numbers_Defiition = ctk.CTkLabel(main_frame, text="Իրական թվերի հատկությունները", font=('Bold', 35), text_color='black')
    show_Real_Numbers_Defiition.pack(pady=100)
    text_content = (
        "\n       Փակվածություն: Իրական թվերը փակ են գումարման,\n"
        "հանումի, բազմապատկման և բաժանման գործողությունների\n"
        "համար (բացառությամբ զրոյով բաժանման):\n"
        "Համապատասխանություն և Համակերպում: Իրական թվերը\n"
        "բավարարում են գումարման և բազմապատկման\n"
        "համապատասխանության և համակերպման հատկությունները:\n"
        "Նույնական տարրեր: 0-ը գումարման նույնականն է\n"
        "(թիվը չի փոխվում 0-ով գումարելիս), իսկ \n"
        "1-ը բազմապատկման նույնականն է:\n"
        "Հակադարձներ: Յուրաքանչյուր իրական թիվ ունի գումարման\n"
        "հակադարձ (օր.՝ -a՝ a-ի համար), և յուրաքանչյուր ոչ զրո իրական\n"
        "թիվ ունի բազմապատկման հակադարձ (1/a՝ a≠0-ի համար):\n")
    real_numbers_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    real_numbers_text.place(x=10, y=200)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Real_Numbers)
    back_button.place(x=780, y=750)

def show_Real_Numbers_Presentation():
    delate_pages()
    show_Real_Numbers_Defiition = ctk.CTkLabel(main_frame, text="Իրական թվերի ներկայացումը\n      թվային առանցքով", font=('Bold', 35), text_color='black')
    show_Real_Numbers_Defiition.pack(pady=100)
    text_content = (
        "\n       Թվային առանցքի վրա իրական թվերը ներկայացված են\n"
        "կետերով՝ անընդհատ գծով՝ առանց բացերի, ինչը նշանակում է,\n"
        "որ ցանկացած երկու տարբեր իրական թվերի միջև գոյություն\n"
        "ունի իրական թիվ։")
    real_numbers_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    real_numbers_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Real_Numbers)
    back_button.place(x=780, y=750)

def show_Element_of_Trigonometry():
    delate_pages()
    Element_of_Trigonometry = ctk.CTkLabel(main_frame, text="Եռանկյունաչափության տարրերը", font=('Bold', 35), text_color='black')
    Element_of_Trigonometry.pack(pady=100)
    Element_of_Trigonometry_Angels_button = ctk.CTkButton(main_frame, text="Անկյուններ", font=('Bold', 20), command=show_Element_of_Trigonometry_Angels)
    Element_of_Trigonometry_Angels_button.place(x=100, y=190)
    Element_of_Trigonometry_Triangle_button = ctk.CTkButton(main_frame, text="Ուղղանկյուն եռանկյան հետ կապ", font=('Bold', 20), command=show_Element_of_Trigonometry_Triangle)
    Element_of_Trigonometry_Triangle_button.place(x=100, y=260)
    Element_of_Trigonometry_Relation_button = ctk.CTkButton(main_frame, text="Հարաբերություններ", font=('Bold', 20), command=show_Element_of_Trigonometry_Relation)
    Element_of_Trigonometry_Relation_button.place(x=100, y=330)
    Element_of_Trigonometry_Circle_button = ctk.CTkButton(main_frame, text="Միավոր շրջան", font=('Bold', 20), command=show_Element_of_Trigonometry_Circle)
    Element_of_Trigonometry_Circle_button.place(x=100, y=400)
    Element_of_Trigonometry_Equation_button = ctk.CTkButton(main_frame, text="Ինքնահավասարություններ", font=('Bold', 20), command=show_Element_of_Trigonometry_Equation)
    Element_of_Trigonometry_Equation_button.place(x=100, y=470)
    Element_of_Trigonometry_Graph_button = ctk.CTkButton(main_frame, text="Ֆունկցիաների գրաֆիկներ", font=('Bold', 20), command=show_Element_of_Trigonometry_Graph)
    Element_of_Trigonometry_Graph_button.place(x=100, y=540)
    Element_of_Trigonometry_Application_button = ctk.CTkButton(main_frame, text="Կիրառություններ", font=('Bold', 20), command=show_Element_of_Trigonometry_Application)
    Element_of_Trigonometry_Application_button.place(x=100, y=610)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Math_10class_1Term)
    back_button.place(x=780, y=750)

def show_Element_of_Trigonometry_Angels():
    delate_pages()
    Element_of_Trigonometry = ctk.CTkLabel(main_frame, text="Եռանկյունաչափության տարրերը:\n              Անկյունները", font=('Bold', 35), text_color='black')
    Element_of_Trigonometry.pack(pady=100)
    text_content = (
        "\n       Եռանկյունաչափությունը հիմնականում զբաղվում է\n"
        "անկյուններով և դրանց հարաբերություններով ուղղանկյուն\n"
        "եռանկյունների կողմերի հետ։ Անկյունները կարելի է չափել\n"
        "դեգրեներով կամ ռադիաններով:\n" 
        "Դեգրեներ: Ամենամեծ շրջանով չափվում է 360°:\n"
        "Ռադիաններ: Ամենամեծ շրջանով չափվում է 2𝜋 ռադիան:\n")
    element_of_trigonometry_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    element_of_trigonometry_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Element_of_Trigonometry)
    back_button.place(x=780, y=750)

def show_Element_of_Trigonometry_Triangle():
    delate_pages()
    Element_of_Trigonometry = ctk.CTkLabel(main_frame, text="Եռանկյունաչափության տարրերը:\nՈւղղանկյուն եռանկյան հետ կապը", font=('Bold', 35), text_color='black')
    Element_of_Trigonometry.pack(pady=100)
    text_content = (
        "\n       Ուղիղանկյուն եռանկյունը կարևոր է\n"
        "եռանկյունաչափությունում։ Այն ունի մեկ 90° անկյուն, և\n"
        "անկյունների ու կողմերի հարաբերությունները կարևոր են\n"
        "եռանկյունաչափական ֆունկցիաների համար։\n"  
        "Հիպոտենուզա(ներքնաձիք): Եռանկյան ամենաերկար կողմը, որը\n"
        "գտնվում էուղիղ անկյունից դիմաց։\n"
        "Ընդհակառակը կողմ(անկյան դիմացի էջը): Կողմը, որը գտնվում է\n"
        "դիտվող անկյունից դիմաց։\n"
        "Մոտավոր կողմ(անկյան կից էջը): Կողմը, որը գտնվում է դիտվող\n"
        "անկյունիհարևանությամբ, սակայն ոչ հիպոտենուզան։\n")
    element_of_trigonometry_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    element_of_trigonometry_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Element_of_Trigonometry)
    back_button.place(x=780, y=750)

def show_Element_of_Trigonometry_Relation():
    delate_pages()
    Element_of_Trigonometry = ctk.CTkLabel(main_frame, text="Եռանկյունաչափության տարրերը:\n      Հարաբերությունները", font=('Bold', 35), text_color='black')
    Element_of_Trigonometry.pack(pady=100)
    text_content = (
        "\n       Սրանք հիմնական ֆունկցիաներն են, որոնք կապում\n"
        "են ուղղանկյուն եռանկյան անկյունները իր կողմերի\n"
        "երկարությունների հետ:\n"      
        "Սինուս (sin): Ընդհակառակի(անկյան դիմացի էջը) կողմի\n"
        "հարաբերությունը հիպոտենուզային(ներքնաձիք):\n"
        "sin(𝜃) = ընդհակառակը / հիպոտենուզա\n"   
        "Կոսինուս (cos): Մոտավոր(անկյան կից էջը) կողմի\n"
        "հարաբերությունը հիպոտենուզային(ներքնաձիք):\n"
        "cos(𝜃) = մոտավորը / հիպոտենուզա\n"     
        "Տանգենտ (tan): Ընդհակառակի(անկյան դիմացի էջը) կողմի\n"
        "հարաբերությունը մոտավոր(անկյան կից էջը) կողմին:\n"
        "tan(𝜃) = ընդհակառակը / մոտավորը\n"
        "Կոտանգես (ctg): Մոտավոր(անկյան կից էջը) կողմի\n"
        "հարաբերությունը ընդհակառակի(անկյան դիմացի էջը) կողմին:\n"
        "ctg(𝜃) = մոտավորը / ընդհակառակը")
    element_of_trigonometry_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    element_of_trigonometry_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Element_of_Trigonometry)
    back_button.place(x=780, y=750)

def show_Element_of_Trigonometry_Circle():
    delate_pages()
    Element_of_Trigonometry = ctk.CTkLabel(main_frame, text="Եռանկյունաչափության տարրերը:\n          Միավոր շրջանը", font=('Bold', 35), text_color='black')
    Element_of_Trigonometry.pack(pady=100)
    text_content = (
        "\n       Միավորային շրջանը շառավիղը 1 չափ ունեցող շրջան է,\n"
        "որը կենտրոնանում է համակարգի սկզբունքի վրա։\n"
        "Այն օգտագործվում է եռանկյունաչափական ֆունկցիաները\n"
        "սահմանելու համար բոլոր անկյունների համար,\n"
        "ներառյալ 0°-ից 90°-ը դուրս գտնվողները։\n"
        "Այնպես որ, ցանկացած θ անկյան համար,միավորային շրջանի\n"
        "վրա գտնվող կետի կոորդինատները հետևյալն են՝\n"
        "(cos(θ), sin(θ))")
    element_of_trigonometry_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    element_of_trigonometry_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Element_of_Trigonometry)
    back_button.place(x=780, y=750)

def show_Element_of_Trigonometry_Equation():
    delate_pages()
    Element_of_Trigonometry = ctk.CTkLabel(main_frame, text="Եռանկյունաչափության տարրերը:\n   Ինքնահավասարությունները", font=('Bold', 35), text_color='black')
    Element_of_Trigonometry.pack(pady=100)
    text_content = (
        "\n       Կան շատ կարևոր ինքնահավասարություններ\n"
        "Եռանկյունաչափությնում, որոնք կապված են տարբեր\n"
        "ֆունկցիաների միջև։ Ամենատարածվածներից են:\n"
        "Պյութագորասի ինքնահավասարություն:\n"
        "sin²(θ) + cos²(θ) = 1\n"
        "Անկյունների գումարի և տարբերության\n"
        "ինքնահավասարություններ:\n"
        "sin(A+B) = sin(A)cos(B) + cos(A)sin(B)\n"
        "cos(A+B) = cos(A)cos(B) - sin(A)sin(B)\n"    
        "Երկակի անկյան բանաձևեր:\n"
        "sin(2θ) = 2sin(θ)cos(θ)\n"
        "cos(2θ) = cos²(θ) - sin²(θ)\n")
    element_of_trigonometry_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    element_of_trigonometry_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Element_of_Trigonometry)
    back_button.place(x=780, y=750)

def show_Element_of_Trigonometry_Graph():
    delate_pages()
    Element_of_Trigonometry = ctk.CTkLabel(main_frame, text="Եռանկյունաչափության տարրերը:\n   Ֆունկցիաների գրաֆիկները", font=('Bold', 35), text_color='black')
    Element_of_Trigonometry.pack(pady=100)
    text_content = (
        "\n       Եռանկյունաչափական ֆունկցիաները պարբերական\n"
        "հատկություն ունեն։ Օրինակ:\n"
        "Սինուս և կոսինուս ֆունկցիաները ունեն հիմնական\n"
        "պարբերություն 2π:\n"
        "Տանգենտ և կոտանգենտ ֆունկցիաները ունեն հիմնական\n"
        "պարբերություն π:")
    element_of_trigonometry_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    element_of_trigonometry_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Element_of_Trigonometry)
    back_button.place(x=780, y=750)

def show_Element_of_Trigonometry_Application():
    delate_pages()
    Element_of_Trigonometry = ctk.CTkLabel(main_frame, text="Եռանկյունաչափության տարրերը:\n          Կիրառությունները", font=('Bold', 35), text_color='black')
    Element_of_Trigonometry.pack(pady=100)
    text_content = (
        "\n       Եռանկյունաչափությունը լայնորեն կիրառվում է տարբեր\n"
        "ոլորտներում, ներառյալ ֆիզիկա, ինժենեռություն,\n"
        "աստղաբանություն և նույնիսկ համակարգչային գրաֆիկա։\n"
        "Այն օգտագործվում է ալիքների, ոսպի պարբերականության\n"
        "և այլ երևույթների մոդելավորման համար։")
    element_of_trigonometry_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    element_of_trigonometry_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Element_of_Trigonometry)
    back_button.place(x=780, y=750)

def show_Function():
    delate_pages()
    Function = ctk.CTkLabel(main_frame, text="Ֆունկցիա", font=('Bold', 35), text_color='black')
    Function.pack(pady=100)
    Function_Bases_button = ctk.CTkButton(main_frame, text="Ֆունկցիաներ. Հիմունքներ", font=('Bold', 20), command=show_Function_Bases)
    Function_Bases_button.place(x=100, y=190)
    Function_Types_button = ctk.CTkButton(main_frame, text="Ֆունկցիաների տեսակները", font=('Bold', 20), command=show_Function_Types)
    Function_Types_button.place(x=100, y=260)
    Function_Properties_button = ctk.CTkButton(main_frame, text="Ֆունկցիաների հատկություններ", font=('Bold', 20), command=show_Function_Properties)
    Function_Properties_button.place(x=100, y=330)
    Function_Graph_button = ctk.CTkButton(main_frame, text="Ֆունկցիաների գրաֆիկներ", font=('Bold', 20), command=show_Function_Graph)
    Function_Graph_button.place(x=100, y=400)
    Function_Aplication_button = ctk.CTkButton(main_frame, text="Ֆունկցիաների կիրառություններ", font=('Bold', 20), command=show_Function_Aplication)
    Function_Aplication_button.place(x=100, y=470)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Math_10class_2Term)
    back_button.place(x=780, y=750)

def show_Function_Bases():
    delate_pages()
    Function_Bases = ctk.CTkLabel(main_frame, text="Ֆունկցիաների տեսակները", font=('Bold', 35), text_color='black')
    Function_Bases.pack(pady=100)
    Function_Bases_Defination_button = ctk.CTkButton(main_frame, text="Սահմանում", font=('Bold', 20), command=show_Function_Bases_Defination)
    Function_Bases_Defination_button.place(x=100, y=190)
    Function_Bases_Presentation_button = ctk.CTkButton(main_frame, text="Ներկայացման եղանակներ", font=('Bold', 20), command=show_Function_Bases_Presentation)
    Function_Bases_Presentation_button.place(x=100, y=260)
    Function_Bases_Termins_button = ctk.CTkButton(main_frame, text="Տերմիններ", font=('Bold', 20), command=show_Function_Bases_Termins)
    Function_Bases_Termins_button.place(x=100, y=330)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Function)
    back_button.place(x=780, y=750)

def show_Function_Types():
    delate_pages()
    Function_Types = ctk.CTkLabel(main_frame, text="Ֆունկցիաներ. Հիմունքներ", font=('Bold', 35), text_color='black')
    Function_Types.pack(pady=100)
    Function_Types_Expresion_button = ctk.CTkButton(main_frame, text="Ըստ արտահայտության", font=('Bold', 20), command=show_Function_Types_Expresion)
    Function_Types_Expresion_button.place(x=100, y=190)
    Function_Types_Relation_button = ctk.CTkButton(main_frame, text="Ըստ հարաբերության", font=('Bold', 20), command=show_Function_Types_Relation)
    Function_Types_Relation_button.place(x=100, y=260)
    Function_Types_Typic_button = ctk.CTkButton(main_frame, text="Հատուկ ֆունկցիաներ", font=('Bold', 20), command=show_Function_Types_Typic)
    Function_Types_Typic_button.place(x=100, y=330)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Function)
    back_button.place(x=780, y=750)
    
def show_Function_Bases_Defination():
    delate_pages()
    Function_Bases = ctk.CTkLabel(main_frame, text="Սահմանում", font=('Bold', 35), text_color='black')
    Function_Bases.pack(pady=100)
    text_content = (
        "\n       Ֆունկցիա կոչվում է կապը երկու հավաքածուների միջև,\n"
        "որտեղ առաջին հավաքածուի (տիրույթ) յուրաքանչյուր տարր\n"
        "համապատասխանում է երկրորդ հավաքածուի\n"
        "(արժեքների տիրույթ)միայն մեկ տարրին։\n")
    Function_Bases_Defination_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Function_Bases_Defination_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Function_Bases)
    back_button.place(x=780, y=750)

def show_Function_Bases_Presentation():
    delate_pages()
    Function_Bases = ctk.CTkLabel(main_frame, text="Ներկայացման եղանակներ", font=('Bold', 35), text_color='black')
    Function_Bases.pack(pady=100)
    text_content = (
        "\n       Բանաձևային՝ f(x) = y։\n"
        "Գրաֆիկով՝ կոորդինատային հարթակի վրա գծագրված։\n"
        "Աղյուսակային՝ տիրույթի (input) և արժեքների տիրույթի (output)\n"
        "աղյուսակով։\n"
        "Բառային նկարագրություն՝ կապը նկարագրված բառերով")
    Function_Bases_Presentation_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Function_Bases_Presentation_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Function_Bases)
    back_button.place(x=780, y=750)

def show_Function_Bases_Termins():
    delate_pages()
    Function_Bases = ctk.CTkLabel(main_frame, text="Տերմիններ", font=('Bold', 35), text_color='black')
    Function_Bases.pack(pady=100)
    text_content = (
        "\n       Տիրույթ(Domain)՝ հնարավոր բոլոր մուտքային արժեքները։\n"
        "Արժեքների տիրույթ(Range)՝ հնարավոր բոլոր ելքային արժեքները։\n"
        "Կոդոմեյն (Codomain)՝ հավաքածու, որում կարող են գտնվել\n"
        "ելքային արժեքները (կարող է ներառել ավելորդ արժեքներ)։\n")
    Function_Bases_Termins_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Function_Bases_Termins_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Function_Bases)
    back_button.place(x=780, y=750)

def show_Function_Types_Expresion():
    delate_pages()
    Function_Types = ctk.CTkLabel(main_frame, text="Ըստ արտահայտության", font=('Bold', 35), text_color='black')
    Function_Types.pack(pady=100)
    text_content = (
        "\n       Գծային ֆունկցիա՝ f(x) = mx + c։\n"
        "Գրաֆիկ․ ուղիղ գիծ։\n"
        "Օրինակ՝ f(x) = 2x + 1։\n"
        "Քառակուսի ֆունկցիա՝ f(x) = ax^2 + bx + c։\n"
        "Գրաֆիկ․ պարաբոլա։\n"
        "Օրինակ՝ f(x) = x^2 − 3x + 2։\n"
        "Բազմանդամ ֆունկցիա՝ բարձր աստիճանի ֆունկցիաներ,\n"
        "օրինակ՝ f(x) = x^3 − 2x^2 + x։\n")
    Function_Types_Expresion_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Function_Types_Expresion_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Function_Types)
    back_button.place(x=780, y=750)

def show_Function_Types_Relation():
    delate_pages()
    Function_Types = ctk.CTkLabel(main_frame, text="Ըստ հարաբերության", font=('Bold', 35), text_color='black')
    Function_Types.pack(pady=100)
    text_content = (
        "\n       Մեկից-մեկ (Injective)՝ յուրաքանչյուր մուտք ունի\n"
        "յուրահատուկ ելք։\n"
        "Շատից-մեկ (Many-to-one)՝ մի քանի մուտք կարող է ունենալ\n"
        " նույն ելքը։\n"
        "Դեպի (Onto)՝ կոդոմեյնի բոլոր տարրերը համապատասխանում են\n"
        "տիրույթի որևէ տարրին։\n"
        "Բիժեկտիվ (Bijective)՝ և՛ մեկից-մեկ, և՛ դեպի։\n")
    Function_Types_Relation_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Function_Types_Relation_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Function_Types)
    back_button.place(x=780, y=750)

def show_Function_Types_Typic():
    delate_pages()
    Function_Types = ctk.CTkLabel(main_frame, text="Հատուկ ֆունկցիաներ։", font=('Bold', 35), text_color='black')
    Function_Types.pack(pady=100)
    text_content = (
        "\n       Կայուն ֆունկցիա (Constant)՝ f(x) = c,\n"
        "որտեղ c հաստատուն է։\n"
        "Նույնական ֆունկցիա (Identity)՝ f(x) = x։\n"
        "Քայլային ֆունկցիա (Step)՝ ներառում է միջակայքեր։\n"
        "Եռանկյունաչափական ֆունկցիաներ (Trigonometric)՝\n"
        "sin(x), cos(x), tan(x), ctg(x)։\n"
        "Էքսպոնենցիալ և լոգարիթմական ֆունկցիաներ\n"
        "f(x) = a^x, log(x)։\n")
    Function_Types_Typic_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Function_Types_Typic_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Function_Types)
    back_button.place(x=780, y=750)
    
def show_Function_Properties():
    delate_pages()
    Function_Types = ctk.CTkLabel(main_frame, text="Ֆունկցիաների հատկություններ։", font=('Bold', 35), text_color='black')
    Function_Types.pack(pady=100)
    text_content = (
        "\n       Մեկից-մեկ (Injective)։\n"
        "Տիրույթի ոչ մի երկու տարր չեն համապատասխանում նույն\n"
        "արժեքների տիրույթի տարրին։\n"
        "Դեպի (Surjective)։\n"
        "Կոդոմեյնի յուրաքանչյուր տարր ունի համապատասխան\n"
        "տիրույթի տարր։\n"
        "Բիժեկտիվ (Bijective)։\n"
        "Ֆունկցիան և՛ մեկից-մեկ է, և՛ դեպի։\n"
        "Զույգ և կենտ ֆունկցիաներ (Even and Odd)։\n"
        "Զույգ՝ Սիմետրիկ y-առանցքի նկատմամբ, f(x) = f(−x)։\n"
        "Կենտ՝ Սիմետրիկ սկզբնակետի նկատմամբ, f(−x) = −f(x)։\n")
    Function_Types_Typic_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Function_Types_Typic_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Function)
    back_button.place(x=780, y=750)

def show_Function_Graph():
    delate_pages()
    Function_Types = ctk.CTkLabel(main_frame, text="Ֆունկցիաների գրաֆիկներ։", font=('Bold', 35), text_color='black')
    Function_Types.pack(pady=100)
    text_content = (
        "\n       Գծային գրաֆիկներ՝ ուղիղ գծեր, որոնք որոշվում են\n"
        "y = mx + c բանաձևով։\n"
        "Քառակուսի գրաֆիկներ՝ պարաբոլաներ, որոնցում կարևոր են\n"
        "գագաթնակետըև սիմետրիայի առանցքը։\n"
        "Կարևոր կետեր՝\n"
        "Կտրուկներ x-ի և y-ի հետ։\n"
        "Ասիմպտոտներ (տրացեր՝ ռացիոնալ ֆունկցիաների դեպքում)։\n")
    Function_Types_Typic_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Function_Types_Typic_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Function)
    back_button.place(x=780, y=750)

def show_Function_Aplication():
    delate_pages()
    Function_Types = ctk.CTkLabel(main_frame, text="Ֆունկցիաների կիրառություններ։", font=('Bold', 35), text_color='black')
    Function_Types.pack(pady=100)
    text_content = (
        "\n       Ֆիզիկա՝ շարժման բանաձևեր, ալիքների ֆունկցիաներ։\n"
        "Տնտեսագիտություն՝ ծախսերի, պահանջարկի և\n"
        "առաջարկի ֆունկցիաներ։\n"
        "Համակարգչային գիտություն՝ ալգորիթմներ և \n"
        "րագրավորման տրամաբանություն։\n"
        "Իրական կյանք՝ եղանակի կանխատեսում, բնակչության աճ։")
    Function_Types_Typic_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Function_Types_Typic_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Function)
    back_button.place(x=780, y=750)

def show_Trigonometric_Functions_and_Equations():
    delate_pages()
    Trigonometric_Functions_and_Equations = ctk.CTkLabel(main_frame, text="Եռանկյունաչափական ֆունկցիաներ \n            և հավասարումներ", font=('Bold', 35), text_color='black')
    Trigonometric_Functions_and_Equations.pack(pady=100)
    Trigonometric_Main_button = ctk.CTkButton(main_frame, text="Եռանկյունաչափության հիմնական գաղափարներ", font=('Bold', 20), command=show_Trigonometric_Main)
    Trigonometric_Main_button.place(x=60, y=260)
    Trigonometric_Relations_button = ctk.CTkButton(main_frame, text="Եռանկյունաչափական հարաբերություններ", font=('Bold', 20), command=show_Trigonometric_Relation)
    Trigonometric_Relations_button.place(x=60, y=330)
    Trigonometric_Similarity_button = ctk.CTkButton(main_frame, text="Եռանկյունաչափական նույնություններ", font=('Bold', 20), command=show_Trigonometric_Similarity)
    Trigonometric_Similarity_button.place(x=60, y=400)
    Trigonometric_Value_button = ctk.CTkButton(main_frame, text="Եռանկյունաչափական արժեքներ", font=('Bold', 20), command=show_Trigonometric_Value)
    Trigonometric_Value_button.place(x=60, y=470)
    Trigonometric_Equation_button = ctk.CTkButton(main_frame, text="Եռանկյունաչափական հավասարումներ", font=('Bold', 20), command=show_Trigonometric_Equation)
    Trigonometric_Equation_button.place(x=60, y=540)
    Trigonometric_Aplication_button = ctk.CTkButton(main_frame, text="Եռանկյունաչափության կիրառություններ", font=('Bold', 20), command=show_Trigonometric_Aplication)
    Trigonometric_Aplication_button.place(x=60, y=610)
    Trigonometric_Circle_button = ctk.CTkButton(main_frame, text="Միավոր շրջանը", font=('Bold', 20), command=show_Trigonometric_Circle)
    Trigonometric_Circle_button.place(x=60, y=680)
    back_button = ctk.CTkButton(main_frame, text="Back", font=('Bold', 15), command=show_Math_10class_2Term)
    back_button.place(x=780, y=750)
    
def show_Trigonometric_Main():
    delate_pages()
    Function_Types = ctk.CTkLabel(main_frame, text="Եռանկյունաչափության հիմնական\n               գաղափարներ։", font=('Bold', 35), text_color='black')
    Function_Types.pack(pady=100)
    text_content = (
        "\n       Սահմանում․ Եռանկյունաչափությունը մաթեմատիկայի\n"
        "ճյուղ է, որը զբաղվում է եռանկյունների կողմերի և անկյունների\n"
        "միջև կապերի ուսումնասիրությամբ։\n"
        "Ուղղանկյուն եռանկյուն․ Եռանկյունաչափության հիմքը՝\n"
        "Հիպոտենուզ․ Աղեղնաձև անկյան դիմացի կողմը,\n"
        "եռանկյան ամենաերկար կողմը։\n"
        "Ընդհակառակ կողմ․ Անկյունին ուղղակիորեն\n"
        "դիմաց գտնվող կողմը։\n"
        "Կից կողմ․ Անկյունին կից գտնվող կողմը\n"
        "(բացառությամբ հիպոտենուզի)։\n")
    Trigonometric_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Trigonometric_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Trigonometric_Functions_and_Equations)
    back_button.place(x=780, y=750)

def show_Trigonometric_Relation():
    delate_pages()
    Function_Types = ctk.CTkLabel(main_frame, text="Եռանկյունաչափական\n  հարաբերություններ։", font=('Bold', 35), text_color='black')
    Function_Types.pack(pady=100)
    text_content = (
        "\n       Ուղղանկյուն եռանկյան համար, θ անկյան դեպքում՝\n"
        "Հարաբերություն       Բանաձև\n"
        "Սինուս (sinθ)             Ընդհակառակ/Հիպոտենուզ\n"
        "Կոսինուս (cosθ)        Կից/Հիպոտենուզ\n"
        "Տանգենս (tanθ)         Ընդհակառակ/Կից\n"
        "Կոսեկանս (cscθ)       Հիպոտենուզ/Ընդհակառակ\n"
        "Սեկանս (secθ)          Հիպոտենուզ/Կից\n"
        "Կոտանգենս (cotθ)      Կից/Ընդհակառակ\n\n"
        "Փոխադարձ կապեր․\n"
        "cscθ = 1/sinθ                 Ընդհակառակ - Դիմացի էջ  \n"
        "secθ = 1/cosθ                Կից - Կից էջ  \n"
        "cotθ = 1/tanθ                 Հիպոտենուզ - Ներքնաձիք") 
    Trigonometric_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Trigonometric_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Trigonometric_Functions_and_Equations)
    back_button.place(x=780, y=750)

def show_Trigonometric_Similarity():
    delate_pages()
    Function_Types = ctk.CTkLabel(main_frame, text="Եռանկյունաչափական\n  նույնություններ։", font=('Bold', 35), text_color='black')
    Function_Types.pack(pady=100)
    text_content = (
        "\n       Սրանք հավասարումներ են, որոնք ճիշտ են բոլոր θ-ների\n"
        "համար (որտեղ սահմանված են)։\n\n"
        "Պյութագորասյան նույնություններ․\n"
        "sin²θ + cos²θ = 1\n"
        "1 + tan²θ = sec²θ\n"
        "1 + cot²θ = csc²θ\n\n"
        "Բաժանելիության նույնություններ․\n"
        "tanθ = sinθ/cosθ\n"
        "cotθ = cosθ/sinθ\n") 
    Trigonometric_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Trigonometric_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Trigonometric_Functions_and_Equations)
    back_button.place(x=780, y=750)

def show_Trigonometric_Value():
    delate_pages()
    Function_Types = ctk.CTkLabel(main_frame, text="Եռանկյունաչափական արժեքներ\n ստանդարտ անկյունների համար։", font=('Bold', 35), text_color='black')
    Function_Types.pack(pady=100)
    text_content = (
        "\n       Հիշեք հետևյալ արժեքները 0°, 30°, 45°, 60°, և 90°-ի համար․\n\n"
        "θ         sinθ          cosθ        tanθ                   cotθ\n"
        "0°        0              1             0                        Չսահմանված\n"
        "30°       1/2         √3/2          1/√3                   √3\n"
        "45°       √2/2        √2/2          1                       1\n"
        "60°       √3/2         1/2          √3                      1/√3\n"
        "90°       1              0            Չսահմանված     0  \n") 
    Trigonometric_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Trigonometric_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Trigonometric_Functions_and_Equations)
    back_button.place(x=780, y=750)

def show_Trigonometric_Equation():
    delate_pages()
    Function_Types = ctk.CTkLabel(main_frame, text="Եռանկյունաչափական\n հավասարումներ։", font=('Bold', 35), text_color='black')
    Function_Types.pack(pady=100)
    text_content = (
        "\n       Եռանկյունաչափական հավասարումը պարունակում է\n"
        "անկյան եռանկյունաչափական ֆունկցիաներ։\n"
        "Հիմնական քայլեր հավասարումներ լուծելու համար\n"
        "1․ Բացահայտեք եռանկյունաչափական ֆունկցիան։\n"
        "2․ Օգտագործեք ստանդարտ արժեքներ կամ նույնություններ՝\n"
        "հնարավոր լուծումները գտնելու համար։\n"
        "3․ Օգտագործեք ընդհանրացված լուծումների բանաձևեր։\n"
        "Ընդհանուր լուծումներ․\n\n"
        "sinθ = k՝ Եթե |k| ≤ 1, θ = sin⁻¹(k) + 2nπ կամ π - sin⁻¹(k) + 2nπ,\n"
        "որտեղ n ամբողջ թիվ է։\n"
        "cosθ = k՝ Եթե |k| ≤ 1, θ = ±cos⁻¹(k) + 2nπ։\n"
        "tanθ = k՝ θ = tan⁻¹(k) + nπ։\n") 
    Trigonometric_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Trigonometric_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Trigonometric_Functions_and_Equations)
    back_button.place(x=780, y=750)

def show_Trigonometric_Aplication():
    delate_pages()
    Function_Types = ctk.CTkLabel(main_frame, text="Եռանկյունաչափության\n կիրառություններ։", font=('Bold', 35), text_color='black')
    Function_Types.pack(pady=100)
    text_content = (
        "\n       Բարձրության և հեռավորության խնդիրներ․\n"
        "Բարձրացման անկյուն․ Հորիզոնական գծից վեր\n"
        "բարձրացող անկյունը։\n"
        "Նվազման անկյուն․ Հորիզոնական գծից ներքև\n"
        "իջնող անկյունը։\n"
        "Կիրառեք եռանկյունաչափական հարաբերություններ\n"
        "իրական կյանքում՝ բարձրություններն ու\n"
        "հեռավորությունները գտնելու համար։\n"
        "Նավիգացիա և աստղագիտություն․ Չմատչելի օբյեկտների՝\n"
        "լեռների, շենքերի կամ երկնային մարմինների\n"
        "հեռավորությունների չափում։\n") 
    Trigonometric_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Trigonometric_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Trigonometric_Functions_and_Equations)
    back_button.place(x=780, y=750)

def show_Trigonometric_Circle():
    delate_pages()
    Function_Types = ctk.CTkLabel(main_frame, text="Միավոր շրջանը։", font=('Bold', 35), text_color='black')
    Function_Types.pack(pady=100)
    text_content = (
        "\n       Միավոր շրջանը եռանկյունաչափական\n"
        "ֆունկցիաների երկրաչափական ներկայացումն է․\n"
        "Շառավիղը՝ 1, կենտրոնը՝ կոորդինատային\n"
        "սկզբնակետում։\n"
        "Շրջանի (x, y) կետերի կոորդինատները՝\n"
        "x = cosθ, y = sinθ։\n") 
    Trigonometric_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Trigonometric_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Trigonometric_Functions_and_Equations)
    back_button.place(x=780, y=750)
    
def show_Scalar_Function():
    delate_pages()
    Scalar_Function = ctk.CTkLabel(main_frame, text="Ցուցչային ֆունկցիաներ", font=('Bold', 35), text_color='black')
    Scalar_Function.pack(pady=100)
    text_content = (
        "\n       Ցուցչային ֆունկցիան մաթեմատիկական արտահայտություն\n"
        "է, որտեղ փոփոխականը գտնվում է աստիճանի դիրքում։\n"
        "Այս ֆունկցիաներն լայնորեն օգտագործվում են աճի և անկման\n"
        "խնդիրներում, ֆինանսներում և բնական երևույթներում։\n") 
    Scalar_Function_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Scalar_Function_text.place(x=10, y=250)
    Scalar_Function_Main_button = ctk.CTkButton(main_frame, text="Ընդհանուր ձև", font=('Bold', 20), command=show_Scalar_Function_Main)
    Scalar_Function_Main_button.place(x=60, y=480)
    Scalar_Function_Properties_button = ctk.CTkButton(main_frame, text="Հիմնական հատկություններ", font=('Bold', 20), command=show_Scalar_Function_Properties)
    Scalar_Function_Properties_button.place(x=60, y=550)
    Scalar_Function_Diagrame_button = ctk.CTkButton(main_frame, text="Գծապատկերային առանձնահատկություններ", font=('Bold', 20), command=show_Scalar_Function_Diagrame)
    Scalar_Function_Diagrame_button.place(x=60, y=620)
    Scalar_Function_Use_button = ctk.CTkButton(main_frame, text="Օգտագործումներ", font=('Bold', 20), command=show_Scalar_Function_Use)
    Scalar_Function_Use_button.place(x=60, y=690)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Math_11class_1Term)
    back_button.place(x=780, y=750)

def show_Scalar_Function_Use():
    delate_pages()
    Scalar_Function = ctk.CTkLabel(main_frame, text="Օգտագործումներ", font=('Bold', 35), text_color='black')
    Scalar_Function.pack(pady=100)
    text_content = (
        "\n       Կուտակային տոկոսադրույքի բանաձև:\n"
        "𝐴 = 𝑃(1 + 𝑟)^𝑡\n"
        "Բնակչության աճ:\n"
        "𝑃(𝑡) = 𝑃₀𝑒ᵏᵗ\n"
        "Ռադիոակտիվ քայքայում:\n"
        "𝑁(𝑡) = 𝑁₀𝑒⁻ᵏᵗ\n") 
    Scalar_Function_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Scalar_Function_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Scalar_Function)
    back_button.place(x=780, y=750)

def show_Scalar_Function_Diagrame():
    delate_pages()
    Scalar_Function = ctk.CTkLabel(main_frame, text="         Գծապատկերային\n    առանձնահատկություններ", font=('Bold', 35), text_color='black')
    Scalar_Function.pack(pady=100)
    text_content = (
        "\n       Աննշանապես անցնում է (0, 𝑎) կետով։\n"
        "Ասիմպտոտա՝ 𝑥-ի առանցքը (𝑦 = 0)։\n"
        "Հարթ և շարունակական կոր։\n") 
    Scalar_Function_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Scalar_Function_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Scalar_Function)
    back_button.place(x=780, y=750)
    
def show_Scalar_Function_Properties():
    delate_pages()
    Scalar_Function = ctk.CTkLabel(main_frame, text="Հիմնական հատկություններ", font=('Bold', 35), text_color='black')
    Scalar_Function.pack(pady=100)
    text_content = (
        "\n      Տարածք: 𝑅 (բոլոր իրական թվերը)։\n"
        "Նշանակումների տիրույթ:\n"
        "(0, ∞), երբ 𝑎 > 0;\n"
        "(−∞, 0), երբ 𝑎 < 0։\n"
        "Աճ/Անկում:\n"
        "Ցուցչային աճ: 𝑏 > 1։\n"
        "Ցուցչային անկում: 0 < 𝑏 < 1։\n"
        "Խաչման կետ: 𝑦-ի խաչման կետը (0, 𝑎)-ում է,\n"
        "քանի որ 𝑓(0) = 𝑎 ⋅ 𝑏^0 = 𝑎։\n") 
    Scalar_Function_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Scalar_Function_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Scalar_Function)
    back_button.place(x=780, y=750)

def show_Scalar_Function_Main():
    delate_pages()
    Scalar_Function = ctk.CTkLabel(main_frame, text="Ընդհանուր ձև", font=('Bold', 35), text_color='black')
    Scalar_Function.pack(pady=100)
    text_content = (
        "\n       𝑓(𝑥) = 𝑎 ⋅ 𝑏^𝑥\n\n"
        "𝑎: Սկզբնական արժեք կամ գործակից։\n"
        "𝑏: Հիմքը (𝑏 > 0, 𝑏 ≠ 1)։\n"
        "𝑥: Ասիճան կամ աստիճանի ցուցիչ։\n") 
    Scalar_Function_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Scalar_Function_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Scalar_Function)
    back_button.place(x=780, y=750)
   
def show_Pointar_Function():
    delate_pages()
    Pointar_Function = ctk.CTkLabel(main_frame, text="Աստիճանային ֆունկցիաներ", font=('Bold', 35), text_color='black')
    Pointar_Function.pack(pady=100)
    text_content = (
        "\n       Ցուցչային ֆունկցիան մաթեմատիկական արտահայտություն\n"
        "է, որտեղ փոփոխականը գտնվում է աստիճանի դիրքում։\n"
        "Այս ֆունկցիաներն լայնորեն օգտագործվում են աճի և անկման\n"
        "խնդիրներում, ֆինանսներում և բնական երևույթներում։\n") 
    Pointar_Function_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Pointar_Function_text.place(x=10, y=250)
    Pointar_Function_Main_button = ctk.CTkButton(main_frame, text="Ընդհանուր ձև", font=('Bold', 20), command=show_Pointar_Function_Main)
    Pointar_Function_Main_button.place(x=60, y=450)
    Pointar_Function_Properties_button = ctk.CTkButton(main_frame, text="Հիմնական հատկություններ", font=('Bold', 20), command=show_Pointar_Function_Properties)
    Pointar_Function_Properties_button.place(x=60, y=520)
    Pointar_Function_Diagrame_button = ctk.CTkButton(main_frame, text="Գծապատկերային առանձնահատկություններ", font=('Bold', 20), command=show_Pointar_Function_Diagrame)
    Pointar_Function_Diagrame_button.place(x=60, y=590)
    Pointar_Function_Case_button = ctk.CTkButton(main_frame, text="Հատուկ դեպքեր", font=('Bold', 20), command=show_Pointar_Function_Case)
    Pointar_Function_Case_button.place(x=60, y=660)
    Pointar_Function_Use_button = ctk.CTkButton(main_frame, text="Օգտագործումներ", font=('Bold', 20), command=show_Pointar_Function_Use)
    Pointar_Function_Use_button.place(x=60, y=730)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Math_11class_1Term)
    back_button.place(x=780, y=750)

def show_Pointar_Function_Use():
    delate_pages()
    Pointar_Function = ctk.CTkLabel(main_frame, text="Օգտագործումներ", font=('Bold', 35), text_color='black')
    Pointar_Function.pack(pady=100)
    text_content = (
        "\n       Ֆիզիկա (հակադարձ քառակուսի օրենք):\n"
        "𝐹 ∝ 1/𝑟²\n"
        "Երկրաչափություն (մակերես և ծավալ):\n"
        "Քառակուսի մակերես՝ 𝐴 = 𝑠² ։\n"
        "Խորանարդի ծավալ՝ 𝑉 = 𝑠³ ։\n"
        "Կշռման օրենքներ կենսաբանության\n"
        "և ճարտարագիտության մեջ։\n") 
    Pointar_Function_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Pointar_Function_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Pointar_Function)
    back_button.place(x=780, y=750)

def show_Pointar_Function_Case():
    delate_pages()
    Pointar_Function = ctk.CTkLabel(main_frame, text="Հատուկ դեպքեր", font=('Bold', 35), text_color='black')
    Pointar_Function.pack(pady=100)
    text_content = (
        "\n      𝑛 = 1: Գծային ֆունկցիա (𝑓(𝑥) = 𝑎𝑥)։\n"
        "𝑛 = −1: Հակադարձ ֆունկցիա (𝑓(𝑥) = 𝑎/𝑥)։\n"
        "𝑛 = 0.5: Քառակուսի արմատ (𝑓(𝑥) = 𝑎√𝑥)։\n") 
    Pointar_Function_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Pointar_Function_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Pointar_Function)
    back_button.place(x=780, y=750)

def show_Pointar_Function_Diagrame():
    delate_pages()
    Pointar_Function = ctk.CTkLabel(main_frame, text="         Գծապատկերային\n    առանձնահատկություններ", font=('Bold', 35), text_color='black')
    Pointar_Function.pack(pady=100)
    text_content = (
        "\n       𝑛 > 0: Կորը մեծանում է, երբ 𝑥-ն\n"
        "հեռանում է զրոյից։\n"
        "𝑛 < 0: Կորը նվազում է 𝑥 = 0-ի մոտ,\n"
        "ունի ուղղահայաց ասիմպտոտա 𝑥 = 0-ի մոտ։\n"
        "𝑎-ն որոշում է ուղղահայաց ձգվածությունը\n"
        "կամ սեղմվածությունը։\n") 
    Pointar_Function_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Pointar_Function_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Pointar_Function)
    back_button.place(x=780, y=750)
    
def show_Pointar_Function_Properties():
    delate_pages()
    Pointar_Function = ctk.CTkLabel(main_frame, text="Հիմնական հատկություններ", font=('Bold', 35), text_color='black')
    Pointar_Function.pack(pady=100)
    text_content = (
        "\n      Տարածք:\n"
        "𝑛 > 0: Բոլոր իրական թվերը։\n"
        "𝑛 < 0: Բոլոր իրական թվերը՝ բացի 𝑥 = 0-ից։\n"
        "Նշանակումների տիրույթ:\n"
        "Երբ 𝑛 զույգ է՝ տիրույթը [0, ∞), եթե 𝑎 > 0։\n"
        "Երբ 𝑛 կենտ է՝ տիրույթը 𝑅։\n"
        "Համաչափություն:\n"
        "Զույգ աստիճաններ (𝑛 զույգ): Համաչափ է 𝑦-ի\n"
        "առանցքի նկատմամբ։\n"
        "Կենտ աստիճաններ (𝑛 կենտ): Համաչափ է ծագման\n"
        "կետի նկատմամբ։\n") 
    Pointar_Function_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Pointar_Function_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Pointar_Function)
    back_button.place(x=780, y=750)

def show_Pointar_Function_Main():
    delate_pages()
    Pointar_Function = ctk.CTkLabel(main_frame, text="Ընդհանուր ձև", font=('Bold', 35), text_color='black')
    Pointar_Function.pack(pady=100)
    text_content = (
        "\n       𝑓(𝑥) = 𝑎𝑥ⁿ\n"
        "𝑎: Գործակից կամ բազմապատկիչ։\n"
        "𝑛: Ասիճան (իրական թիվ)։\n"
        "\nՀիմնական հատկություններ\n") 
    Pointar_Function_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Pointar_Function_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Pointar_Function)
    back_button.place(x=780, y=750)

def show_Log_Function():
    delate_pages()
    Log_Function = ctk.CTkLabel(main_frame, text="Լոգարիթմական ֆունկցիաներ", font=('Bold', 35), text_color='black')
    Log_Function.pack(pady=100)
    Log_Function_Main_button = ctk.CTkButton(main_frame, text="Լոգարիթմական ֆունկցիաների մուտք", font=('Bold', 20), command=show_Log_Function_Main)
    Log_Function_Main_button.place(x=60, y=200)
    Log_Function_Defination_button = ctk.CTkButton(main_frame, text="Լոգարիթմի սահմանում", font=('Bold', 20), command=show_Log_Function_Defination)
    Log_Function_Defination_button.place(x=60, y=270)
    Log_Function_Properties_button = ctk.CTkButton(main_frame, text="Լոգարիթմական հիմնական հատկությունները", font=('Bold', 20), command=show_Log_Function_Properties)
    Log_Function_Properties_button.place(x=60, y=340)
    Log_Function_Types_button = ctk.CTkButton(main_frame, text="Լոգարիթմի տեսակները", font=('Bold', 20), command=show_Log_Function_Types)
    Log_Function_Types_button.place(x=60, y=410)
    Log_Function_Graph_button = ctk.CTkButton(main_frame, text="Լոգարիթմական ֆունկցիաների գծերը", font=('Bold', 20), command=show_Log_Function_Graph)
    Log_Function_Graph_button.place(x=60, y=480)
    Log_Function_Solution_button = ctk.CTkButton(main_frame, text="Լոգարիթմական հավասարումների լուծում", font=('Bold', 20), command=show_Log_Function_Solution)
    Log_Function_Solution_button.place(x=60, y=550)
    Log_Function_Use_button = ctk.CTkButton(main_frame, text="Լոգարիթմների կիրառություններ", font=('Bold', 20), command=show_Log_Function_Use)
    Log_Function_Use_button.place(x=60, y=620)
    Log_Function_Formula_button = ctk.CTkButton(main_frame, text="Կարևոր բանաձևեր և հատկություններ", font=('Bold', 20), command=show_Log_Function_Formula)
    Log_Function_Formula_button.place(x=60, y=690)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Math_11class_1Term)
    back_button.place(x=780, y=750)

def show_Log_Function_Formula():
    delate_pages()
    Scalar_Function = ctk.CTkLabel(main_frame, text="Կարևոր բանաձևեր\n և հատկություններ", font=('Bold', 35), text_color='black')
    Scalar_Function.pack(pady=100)
    text_content = (
        "\n       Լոգարիթմական հավասարումների լուծման\n"
        "համար հաճախ օգտագործում են լոգարիթմների\n"
        "հատկությունները՝ հավասարումը պարզեցնելու կամ\n"
        "այն էքսպոնենցիալ ձևով փոխելու համար։\n"
        "Հիմնական մոտեցումները:\n"
        "Էքսպոնենցիալ ձևը: Եթե log_b 𝑥 = 𝑦, ապա bᵧ = 𝑥։\n"
        "Լոգարիթմների համախմբում: Օգտագործեք գումարման,\n"
        "բաժանման և համարըքավորման օրենքները՝ լոգարիթմները\n"
        "համախմբելու կամ բաժանելու համար։\n"
        "Լոգարիթմը մեկուսացնելը: Լոգարիթմային արտահայտությունը\n"
        "մեկուսացնելը թույլ է տալիս այն փոփոխել էքսպոնենցիալ ձևով։\n"
        "Օրինակ: Լուծեք log₂ (𝑥+1) = 3։\n"
        "Փոխարինեք էքսպոնենցիալ ձևով՝ 2³ = 𝑥 + 1\n"
        "Լուծեք՝ 8 = 𝑥 + 1, այնպես որ 𝑥 = 7") 
    Scalar_Function_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Scalar_Function_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Log_Function)
    back_button.place(x=780, y=750)

def show_Log_Function_Use():
    delate_pages()
    Scalar_Function = ctk.CTkLabel(main_frame, text="Լոգարիթմների կիրառություններ", font=('Bold', 35), text_color='black')
    Scalar_Function.pack(pady=100)
    text_content = (
        "       Լոգարիթմները լայնորեն օգտագործվում են\n"
        "տարբեր ոլորտներում:\n"
        "Գիտություն և ինժեներություն: Լոգարիթմները կիրառվում են\n"
        "էքսպոնենցիալ աճի կամ մաշկման հաշվարկներում, օրինակ՝\n"
        "բնակչության մոդելներում, ռադիոակտիվ մաշկման մեջ\n"
        "և pH քիմիայում։\n"
        "Ֆինանսներ: Լոգարիթմները կիրառվում են\n"
        "բարդ տոկոսադրույքների հաշվարկներում\n"
        "և ներդրումների աճի մոդելավորման մեջ։\n"
        "Տեղեկատվության տեսություն: Լոգարիթմները, հատկապես\n"
        "բինար լոգարիթմները, կարևոր են տվյալների սեղմման,\n"
        "գաղտնագրերի և տեղեկատվական բարդության մեջ։\n"
        "Համակարգչային գիտություն: Ալգորիթմները, ինչպիսիք են բինար\n"
        "որոնումը, դասակարգումը և որոշ տվյալների կառուցվածքները\n"
        "(օրինակ՝ հափեր և ծառեր), հաճախ կապված են լոգարիթմական\n"
        "բարդությունների հետ։") 
    Scalar_Function_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Scalar_Function_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Log_Function)
    back_button.place(x=780, y=750)

def show_Log_Function_Solution():
    delate_pages()
    Scalar_Function = ctk.CTkLabel(main_frame, text="        Լոգարիթմական\n հավասարումների լուծում", font=('Bold', 35), text_color='black')
    Scalar_Function.pack(pady=100)
    text_content = (
        "\n       Լոգարիթմական հավասարումների լուծման\n"
        "համար հաճախ օգտագործում են լոգարիթմների\n"
        "հատկությունները՝ հավասարումը պարզեցնելու կամ\n"
        "այն էքսպոնենցիալ ձևով փոխելու համար։\n"
        "Հիմնական մոտեցումները:\n"
        "Էքսպոնենցիալ ձևը: Եթե log_b 𝑥 = 𝑦, ապա bᵧ = 𝑥։\n"
        "Լոգարիթմների համախմբում: Օգտագործեք գումարման,\n"
        "բաժանման և համարըքավորման օրենքները՝ լոգարիթմները\n"
        "համախմբելու կամ բաժանելու համար։\n"
        "Լոգարիթմը մեկուսացնելը: Լոգարիթմային արտահայտությունը\n"
        "մեկուսացնելը թույլ է տալիս այն փոփոխել էքսպոնենցիալ ձևով։\n"
        "Օրինակ: Լուծեք log₂ (𝑥+1) = 3։\n"
        "Փոխարինեք էքսպոնենցիալ ձևով՝ 2³ = 𝑥 + 1\n"
        "Լուծեք՝ 8 = 𝑥 + 1, այնպես որ 𝑥 = 7") 
    Scalar_Function_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Scalar_Function_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Log_Function)
    back_button.place(x=780, y=750)

def show_Log_Function_Graph():
    delate_pages()
    Scalar_Function = ctk.CTkLabel(main_frame, text="      Լոգարիթմական\n ֆունկցիաների գծերը", font=('Bold', 35), text_color='black')
    Scalar_Function.pack(pady=100)
    text_content = (
        "\n       Լոգարիթմական ֆունկցիայի 𝑦 = log_b 𝑥\n"
        "գծի (որտեղ b > 1) հիմնական հատկությունները՝\n"
        "Գծը բարձրանում է, եթե b > 1 և իջնում է,\n"
        "եթե 0 < b < 1։\n"
        "Գծը անցնում է (1,0) կետով, որովհետև log_b 1 = 0։\n"
        "Այն ունի տպավորման եզրագիծ 𝑥 = 0\n"
        "(գծը մոտենում է, բայց երբեք չի հատում y-արևը)։\n"
        "Երբ b > 1, ֆունկցիան դանդաղ բարձրանում է մեծ 𝑥-երի համար։") 
    Scalar_Function_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Scalar_Function_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Log_Function)
    back_button.place(x=780, y=750)

def show_Log_Function_Types():
    delate_pages()
    Scalar_Function = ctk.CTkLabel(main_frame, text="Լոգարիթմի տեսակները", font=('Bold', 35), text_color='black')
    Scalar_Function.pack(pady=100)
    text_content = (
        "       Ընդհանուր լոգարիթմներ: Լոգարիթմներ հիմքով\n"
        "հիմքով 10, հաճախ գրանցվում է որպես log𝑥\n"
        "(հիմք 10-ով անուղղակի տրված)։ Դրանք օգտագործվում\n"
        "են գիտության և ինժեների մեջ։\n"
        "Օրինակ՝ log100 = 2, որովհետև 10² = 100\n"
        "Բնական լոգարիթմներ: Լոգարիթմներ հիմքով e\n"
        "(մոտավորապես 2.718), նշվում են որպես ln𝑥։\n"
        "Բնական լոգարիթմները լայնորեն կիրառվում են\n"
        "հաշվողական անալիզում, հատկապես աճի և մաշկման\n"
        "խնդիրների լուծման համար։\n"
        "Օրինակ՝ ln e³ = 3, որովհետև e³ = e³\n"
        "Բինար լոգարիթմներ: Լոգարիթմներ հիմքով 2,\n"
        "նշվում են որպես log₂ 𝑥, հիմնականում օգտագործվում\n"
        "են համակարգչային գիտության մեջ՝ ալգորիթմների և\n"
        "տվյալների կառուցվածքների մեջ։\n"
        "Օրինակ՝ log₂ 8 = 3, որովհետև 2³ = 8") 
    Scalar_Function_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Scalar_Function_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Log_Function)
    back_button.place(x=780, y=750)

def show_Log_Function_Properties():
    delate_pages()
    Scalar_Function = ctk.CTkLabel(main_frame, text="   Լոգարիթմական\n հիմնական հատկությունները", font=('Bold', 35), text_color='black')
    Scalar_Function.pack(pady=100)
    text_content = (
        "\n       Լոգարիթմական հիմնական հատկությունները\n"
        "Լոգարիթմը 1-ի դեպքում:\n"
        "log_b 1 = 0 այդ դեպքում ցանկացած հիմքով b > 0\n"
        "Սա ճիշտ է, քանի որ ցանկացած ոչ զրոյական\n"
        "հիմք բարձրացվում է 0-րդ ուժի և տալիս 1՝ b⁰ = 1\n"
        "Լոգարիթմը հիմքի դեպքում:\n"
        "log_b b = 1\n"
        "Սա ճիշտ է, որովհետև b¹ = b\n"
        "Ամփոփման օրենքը:\n"
        "log_b (𝑥𝑦) = log_b 𝑥 + log_b 𝑦\n"
        "Այս հատկությունը թույլ է տալիս լոգարիթմըարտադրանքի\n"
        "դեպքում արտահայտել որպես երկու լոգարիթմների գումար։\n") 
    Scalar_Function_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Scalar_Function_text.place(x=10, y=250)
    next_button = ctk.CTkButton(main_frame, text="Հաջորդ էջ", font=('Bold', 15), command=show_Log_Function_Properties1)
    next_button.place(x=640, y=750)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Log_Function)
    back_button.place(x=780, y=750)

def show_Log_Function_Properties1():
    delate_pages()
    Scalar_Function = ctk.CTkLabel(main_frame, text="   Լոգարիթմական\n հիմնական հատկությունները", font=('Bold', 35), text_color='black')
    Scalar_Function.pack(pady=100)
    text_content = (
        "\n       Հասարակացման օրենքը:\n"
        "log_b (𝑥/y) = log_b 𝑥 − log_b 𝑦\n"
        "Սա թույլ է տալիս լոգարիթմը մասնաբաժնի դեպքում \n"
        "արտահայտել որպես երկու լոգարիթմների տարբերություն։\n"
        "Համարականի օրենքը:\n"
        "log_b (𝑥ⁿ) = n ⋅ log_b 𝑥\n"
        "Այս հատկությունը օգտակար է, երբ լոգարիթմում\n"
        "կան աստիճաններ։\n"
        "Հիմքի փոփոխման բանաձևը:\n"
        "log_b 𝑥 = log_k 𝑥 / log_k b\n"
        "Որտեղ k-ն ցանկացած դրական հիմք է\n"
        "(առաջարկվում է 10 կամ e)։\n"
        "Սա թույլ է տալիս փոխել լոգարիթմի հիմքը՝ հաշվարկները\n"
        "հեշտացնելու համար։\n") 
    Scalar_Function_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Scalar_Function_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Log_Function_Properties)
    back_button.place(x=780, y=750)

def show_Log_Function_Defination():
    delate_pages()
    Scalar_Function = ctk.CTkLabel(main_frame, text="Լոգարիթմի սահմանում", font=('Bold', 35), text_color='black')
    Scalar_Function.pack(pady=100)
    text_content = (
        "\n       Լոգարիթմական ֆունկցիան սահմանվում է որպես:\n"
        "𝑦 = log_b 𝑥 միայն այն դեպքում, երբ b^y = x\n"
        "Որտեղ:\n"
        "𝑏 լոգարիթմի հիմքն է։\n"
        "𝑥 թիվն է, որի լոգարիթմը հաշվում ենք (ապրանքը)։\n"
        "𝑦 𝑥-ի լոգարիթմն է հիմքով 𝑏, այսինքն՝ այն ուժը, որի մեջ\n"
        "պետք է բարձրացնել հիմքը, որպեսզի ստանանք 𝑥։\n\n"
        "Օրինակ՝ log₃ 9 = 2, որովհետև 3² = 9\n") 
    Scalar_Function_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Scalar_Function_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Log_Function)
    back_button.place(x=780, y=750)
    
def show_Log_Function_Main():
    delate_pages()
    Scalar_Function = ctk.CTkLabel(main_frame, text="  Լոգարիթմական\nֆունկցիաների մուտք", font=('Bold', 35), text_color='black')
    Scalar_Function.pack(pady=100)
    text_content = (
        "\n       Լոգարիթմական ֆունկցիան էքսպոնենցիալ ֆունկցիայի\n"
        "հակառակն է։ Ընդհանուր ասած, երբ էքսպոնենցիալ ֆունկցիան\n"
        "արտահայտում է որևէ քանակի աճը (օրինակ՝ բարդագույ\n"
        "տոկոսադրույքներ կամ բնակչության աճ), ապա լոգարիթմական\n"
        "ֆունկցիան պատասխանում է հարցին՝ «Որքան ուժով պետք է\n"
        "բարձրացնել հիմքը, որպեսզի ստանանք որոշ թիվ»։\n\n"
        "Օրինակ՝\n"
        "Էքսպոնենցիալ ձևը՝ 2^3 = 8\n"
        "Լոգարիթմական ձևը՝ log₂ 8 = 3, որովհետև 2³ = 8\n") 
    Scalar_Function_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Scalar_Function_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Log_Function)
    back_button.place(x=780, y=750)

def show_Input_and_Output_info():
    delate_pages()
    Input_and_Outputn_label = ctk.CTkLabel(main_frame, text="Մուտք և Ելք", font=('Bold', 35), text_color='black')
    Input_and_Outputn_label.pack(pady=100)
    Input_and_Outputn_Input_button = ctk.CTkButton(main_frame, text="Մուտք Python-ում", font=('Bold', 20), command=show_Input_and_Outputn_Input)
    Input_and_Outputn_Input_button.place(x=100, y=260)
    Input_and_Outputn_Output_button = ctk.CTkButton(main_frame, text="Ելք Python-ում", font=('Bold', 20), command=show_Input_and_Outputn_Output)
    Input_and_Outputn_Output_button.place(x=100, y=330)
    Input_and_Outputn_File_button = ctk.CTkButton(main_frame, text="Ֆայլերի Մուտք/Ելք(Հավելյալ)", font=('Bold', 20), command=show_Input_and_Outputn_File)
    Input_and_Outputn_File_button.place(x=100, y=400)
    Input_and_Outputn_Important_button = ctk.CTkButton(main_frame, text="Կարևոր կետեր՝ հիշելու համար", font=('Bold', 20), command=show_Input_and_Outputn_Important)
    Input_and_Outputn_Important_button.place(x=100, y=470)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Python_Concepts_for_Beginners)
    back_button.place(x=780, y=750)

def show_Input_and_Outputn_Important():
    delate_pages()
    Scalar_Function = ctk.CTkLabel(main_frame, text="Կարևոր կետեր՝ հիշելու համար", font=('Bold', 35), text_color='black')
    Scalar_Function.pack(pady=100)
    text_content = (
        "\n       Մուտք:\n"
        "Օգտագործեք input() օգտատիրոջից մուտքագրում\n"
        "ստանալու համար:\n"
        "Փոխակերպեք մուտքագրումը, օրինակ՝ int() կամ\n"
        "float()-ի միջոցով:\n"
        "Ելք:\n"
        "Օգտագործեք print() տվյալներ ցուցադրելու համար:\n"
        "Օգտագործեք f-տողեր (f\"...\") կամ տողերի ձևավորում\n"
        "մաքուր և կարդացվող ելք ստանալու համար:\n"
        "Ֆայլերի Մուտք/Ելք:\n"
        "Օգտագործեք open() տարբեր ռեժիմներով (\"r\", \"w\", \"a\")՝\n"
        "կարդալու, գրելու կամ կցելու համար:\n"
        "Միշտ փակեք ֆայլերը կամ օգտագործեք with հրաման՝\n"
        "ֆայլերի անվտանգ մշակումը ապահովելու համար:") 
    Scalar_Function_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Scalar_Function_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Input_and_Output_info)
    back_button.place(x=780, y=750)

def show_Input_and_Outputn_File():
    delate_pages()
    Scalar_Function = ctk.CTkLabel(main_frame, text="Ֆայլերի Մուտք/Ելք", font=('Bold', 35), text_color='black')
    Scalar_Function.pack(pady=100)
    text_content = (
        "\n       Python-ը կարող է ֆայլերի հետ աշխատել՝\n"
        "օգտագործելով ներկառուցված ֆունկցիաներ, ինչպիսիք\n"
        "են open(), read() և write():\n\n"
        "Օրինակ:\n"
        "# Գրառում ֆայլի մեջ\n"
        "with open(\"orinak.txt\", \"w\") as file:\n"
        "    file.write(\"Բարև, Ֆայլ!\\n\")\n\n"
        "# Կարդում ֆայլից\n"
        "with open(\"orinak.txt\", \"r\") as file:\n"
        "    content = file.read()\n"
        "    print(content)") 
    Scalar_Function_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Scalar_Function_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Input_and_Output_info)
    back_button.place(x=780, y=750)

def show_Input_and_Outputn_Output():
    delate_pages()
    Scalar_Function = ctk.CTkLabel(main_frame, text="Ելք Python-ում", font=('Bold', 35), text_color='black')
    Scalar_Function.pack(pady=100)
    text_content = (
        "\n       Ելքի համար Python-ը օգտագործում է\n"
        "print() ֆունկցիան: Այն կարող է ցուցադրել տեքստ,\n"
        "փոփոխականներ և նույնիսկ "
        "ձևավորված տողեր:\n"
        "Օրինակ:\n"
        "# Պարզ ելք\n"
        "print(\"Բարև, Աշխարհ!\")\n"
        "# Ելք փոփոխականներով\n"
        "x = 10\n"
        "y = 20\n"
        "print(\"x-ի և y-ի գումարը հավասար է՝\", x + y)\n"
        "# Ձևավորված ելք (f-string)\n"
        "name = \"Անահիտ\"\n"
        "print(f\"Իմ անունն է {name}:\")") 
    Scalar_Function_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Scalar_Function_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Input_and_Output_info)
    back_button.place(x=780, y=750)
    
def show_Input_and_Outputn_Input():
    delate_pages()
    Scalar_Function = ctk.CTkLabel(main_frame, text="Մուտք Python-ում", font=('Bold', 35), text_color='black')
    Scalar_Function.pack(pady=100)
    text_content = (
        "\n       Python-ը օգտագործում է input() ֆունկցիան՝\n"
        "օգտատիրոջից մուտքագրում ստանալու համար:\n"
        "Լռելյայն input()-ը վերադարձնում է տվյալները որպես\n"
        "տեքստ (string): Անհրաժեշտության դեպքում այն կարող եք\n"
        "փոխակերպել այլ տիպերի, օրինակ՝ ամբողջ թվերի\n"
        "կամ իրական թվերի:\n"
        "Օրինակ:\n"
        "name = input(\"Մուտքագրեք ձեր անունը: \")\n"
        "age = int(input(\"Մուտքագրեք ձեր տարիքը: \"))\n"
        "print(f\"Բարև, {name}! Դուք {age} տարեկան եք:\")\n") 
    Scalar_Function_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Scalar_Function_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Input_and_Output_info)
    back_button.place(x=780, y=750)

def show_Variables_and_Types_info():
    delate_pages()
    Variables_and_Types_label = ctk.CTkLabel(main_frame, text="Փոփոխականներ և Տեսակներ", font=('Bold', 35), text_color='black')
    Variables_and_Types_label.pack(pady=100)
    Variables_and_Types1_button = ctk.CTkButton(main_frame, text="Փոփոխականների Հայտարարում", font=('Bold', 20), command=show_Variables_and_Types1)
    Variables_and_Types1_button.place(x=100, y=260)
    Variables_and_Types2_button = ctk.CTkButton(main_frame, text="Փոփոխականների Անվանման Կանոններ", font=('Bold', 20), command=show_Variables_and_Types2)
    Variables_and_Types2_button.place(x=100, y=330)
    Variables_and_Types3_button = ctk.CTkButton(main_frame, text="Տվյալների Տիպեր Python-ում", font=('Bold', 20), command=show_Variables_and_Types3)
    Variables_and_Types3_button.place(x=100, y=400)
    Variables_and_Types4_button = ctk.CTkButton(main_frame, text="Դինամիկ Տիպավորում", font=('Bold', 20), command=show_Variables_and_Types4)
    Variables_and_Types4_button.place(x=100, y=470)
    Variables_and_Types5_button = ctk.CTkButton(main_frame, text="Տիպի Ստուգում", font=('Bold', 20), command=show_Variables_and_Types5)
    Variables_and_Types5_button.place(x=100, y=540)
    Variables_and_Types6_button = ctk.CTkButton(main_frame, text="Տիպերի Փոխակերպում", font=('Bold', 20), command=show_Variables_and_Types6)
    Variables_and_Types6_button.place(x=100, y=610)
    Variables_and_Types7_button = ctk.CTkButton(main_frame, text="Կարևոր Կետեր՝ Հիշելու Համար", font=('Bold', 20), command=show_Variables_and_Types7)
    Variables_and_Types7_button.place(x=100, y=680)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Python_Concepts_for_Beginners)
    back_button.place(x=780, y=750)

def show_Variables_and_Types1():
    delate_pages()
    Scalar_Function = ctk.CTkLabel(main_frame, text="Փոփոխականների Հայտարարում", font=('Bold', 35), text_color='black')
    Scalar_Function.pack(pady=100)
    text_content = (
        "\n       Փոփոխականները ստեղծվում են =\n"
        "օպերատորի միջոցով արժեք վերագրելով։\n"
        "Օրինակ:\n"
        "x = 10         # Ամբողջ թիվ (Integer)\n"
        "name = \"Անահիտ\" # Տող (String)\n"
        "pi = 3.14      # Ուղիղ թիվ (Float)") 
    Scalar_Function_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Scalar_Function_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Variables_and_Types_info)
    back_button.place(x=780, y=750)

def show_Variables_and_Types2():
    delate_pages()
    Scalar_Function = ctk.CTkLabel(main_frame, text="   Փոփոխականների\n Անվանման Կանոններ", font=('Bold', 35), text_color='black')
    Scalar_Function.pack(pady=100)
    text_content = (
        "\n       Անունները կարող են պարունակել տառեր,\n"
        "թվեր և ստորակետեր (_), բայց չեն կարող սկսվել թվով։\n"
        "Անունները տարբերակում են մեծատառերն ու\n"
        "փոքրատառերը (name և Name տարբեր են):\n"
        "Արգելված է օգտագործել պահված (reserved)\n"
        "բառեր, ինչպիսիք են՝ for, if, while։") 
    Scalar_Function_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Scalar_Function_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Variables_and_Types_info)
    back_button.place(x=780, y=750)

def show_Variables_and_Types3():
    delate_pages()
    Scalar_Function = ctk.CTkLabel(main_frame, text="Տվյալների Տիպեր Python-ում", font=('Bold', 35), text_color='black')
    Scalar_Function.pack(pady=100)
    text_content = (
        "       Python-ն ունի մի քանի ներկառուցված տիպեր։\n"
        "Ահա ամենահաճախ օգտագործվողները.\n"
        "ա. Թվային Տիպեր\n"
        "int: Ամբողջ թվեր (օր. 5, -10)\n"
        "float: Ուղիղ թվեր (օր. 3.14, -2.5)\n"
        "complex: Կոմպլեքս թվեր (օր. 3 + 4j)\n"
        "Օրինակ:\n"
        "a = 5        # int\n"
        "b = 2.5      # float\n"
        "c = 1 + 2j   # complex\n"
        "բ. Տողային Տիպ\n"
        "str: Նիշերի հաջորդականություն՝ փակված\n"
        "մենակ կամ կրկնակի չակերտների մեջ։\n"
        "Օրինակ:\n"
        "message = \"Բարև, Աշխարհ!\"  # Տող\n"
        "multiline = '''Սա\n"
        "բազմատող տեքստ է։'''") 
    Scalar_Function_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Scalar_Function_text.place(x=10, y=240)
    next_button = ctk.CTkButton(main_frame, text="Հաջորդ էջ", font=('Bold', 15), command=show_Variables_and_Types32)
    next_button.place(x=640, y=750)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Variables_and_Types_info)
    back_button.place(x=780, y=750)

def show_Variables_and_Types32():
    delate_pages()
    Scalar_Function = ctk.CTkLabel(main_frame, text="Տվյալների Տիպեր Python-ում", font=('Bold', 35), text_color='black')
    Scalar_Function.pack(pady=100)
    text_content = (
        "       գ. Բուլյան Տիպ\n"
        "bool: Ներկայացնում է True կամ False արժեք։\n"
        "Օրինակ:\n"
        "is_active = True\n"
        "is_done = False\n"
        "դ. Հաջորդականության Տիպեր\n"
        "list: Կարգավորված, փոփոխվող հավաքածու\n"
        "(օր. [1, 2, 3])։\n"
        "tuple: Կարգավորված, անփոփոխ հավաքածու\n"
        "(օր. (1, 2, 3))։\n"
        "Օրինակ:\n"
        "numbers = [1, 2, 3]       # list\n"
        "coordinates = (4, 5)      # tuple\n") 
    Scalar_Function_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Scalar_Function_text.place(x=10, y=250)
    next_button = ctk.CTkButton(main_frame, text="Հաջորդ էջ", font=('Bold', 15), command=show_Variables_and_Types33)
    next_button.place(x=640, y=750)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Variables_and_Types3)
    back_button.place(x=780, y=750)

def show_Variables_and_Types33():
    delate_pages()
    Scalar_Function = ctk.CTkLabel(main_frame, text="Տվյալների Տիպեր Python-ում", font=('Bold', 35), text_color='black')
    Scalar_Function.pack(pady=100)
    text_content = (
        "       ե. Հատուցման Տիպ\n"
        "dict: Բանալի-արժեք զույգերի հավաքածու\n"
        "(օր. {\"name\": \"Անահիտ\", \"age\": 25})։\n"
        "Օրինակ:\n"
        "person = {\"name\": \"Անահիտ\", \"age\": 25}\n"
        "զ. None Տիպ\n"
        "None: Ներկայացնում է արժեքի բացակայությունը։\n"
        "Օրինակ:\n"
        "result = None") 
    Scalar_Function_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Scalar_Function_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Variables_and_Types32)
    back_button.place(x=780, y=750)

def show_Variables_and_Types4():
    delate_pages()
    Scalar_Function = ctk.CTkLabel(main_frame, text="Դինամիկ Տիպավորում", font=('Bold', 35), text_color='black')
    Scalar_Function.pack(pady=100)
    text_content = (
        "\n       Python-ում փոփոխականները կարող են\n"
        "փոխել իրենց տիպը կոդի կատարման ընթացքում։\n\n"
        "Օրինակ:\n"
        "x = 10       # int\n"
        "x = \"Բարև\"  # str\n"
        "x = 3.14     # float") 
    Scalar_Function_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Scalar_Function_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Variables_and_Types_info)
    back_button.place(x=780, y=750)

def show_Variables_and_Types5():
    delate_pages()
    Scalar_Function = ctk.CTkLabel(main_frame, text="Տիպի Ստուգում", font=('Bold', 35), text_color='black')
    Scalar_Function.pack(pady=100)
    text_content = (
        "\n       Տվյալ փոփոխականի տիպը կարող եք ստուգել\n"
        "type() ֆունկցիայի միջոցով։\n\n"
        "Օրինակ:\n"
        "x = 42\n"
        "print(type(x))  # Արդյունք: <class 'int'>\n\n"
        "y = \"Python\"\n"
        "print(type(y))  # Արդյունք: <class 'str'>") 
    Scalar_Function_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Scalar_Function_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Variables_and_Types_info)
    back_button.place(x=780, y=750)


def show_Variables_and_Types6():
    delate_pages()
    Scalar_Function = ctk.CTkLabel(main_frame, text="Տիպերի Փոխակերպում", font=('Bold', 35), text_color='black')
    Scalar_Function.pack(pady=100)
    text_content = (
        "\n       Տիպերի Փոխակերպում\n"
        "Կարող եք փոխակերպել տիպերը ներկառուցված\n"
        "ֆունկցիաների միջոցով, ինչպիսիք են՝\n"
        "int(), float(), str()։\n\n"
        "Օրինակ:\n"
        "x = \"123\"       # str\n"
        "y = int(x)      # Փոխակերպում է int\n"
        "z = float(y)    # Փոխակերպում է float\n"
        "print(y, z)     # Արդյունք: 123 123.0\n") 
    Scalar_Function_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Scalar_Function_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Variables_and_Types_info)
    back_button.place(x=780, y=750)

def show_Variables_and_Types7():
    delate_pages()
    Scalar_Function = ctk.CTkLabel(main_frame, text="Կարևոր Կետեր՝\n Հիշելու Համար", font=('Bold', 35), text_color='black')
    Scalar_Function.pack(pady=100)
    text_content = (
        "\n       Python-ում փոփոխականները դինամիկ\n"
        "տիպավորված են։\n"
        "Python-ն ունի մի քանի ներկառուցված տիպեր՝\n"
        "տարբեր տեսակի տվյալներ մշակելու համար։\n"
        "Օգտագործեք պարզ և իմաստալից անուններփոփոխականների\n"
        "համար՝ կոդն ավելի ընթեռնելի դարձնելու համար։\n"
        "Տեսակի վերաբերյալ կասկածների դեպքում օգտագործեք\n"
        "type() ֆունկցիան։\n") 
    Scalar_Function_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Scalar_Function_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Variables_and_Types_info)
    back_button.place(x=780, y=750)

def show_Conditional_Operators_info():
    delate_pages()
    Conditional_Operators_label = ctk.CTkLabel(main_frame, text="Պայմանների Օպերատորներ", font=('Bold', 35), text_color='black')
    Conditional_Operators_label.pack(pady=100)
    text_content = (
        "\n       Python-ում պայմանական օպերատորները\n"
        "(երբեմն անվանում են նաև համեմատական օպերատորներ)\n"
        "օգտագործվում են երկու արժեք համեմատելու համար։\n"
        "Պայմանական օպերատորի արդյունքը Boolean տիպի արժեք է՝\n"
        "`True`(ճշմարիտ) կամ `False` (կեղծ)։\n")
    Conditional_Operators_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Conditional_Operators_text.place(x=10, y=250)
    Conditional_Operators1_button = ctk.CTkButton(main_frame, text="Հիմնական պայմանական օպերատորները", font=('Bold', 20), command=show_Conditional_Operators1)
    Conditional_Operators1_button.place(x=100, y=470)
    Conditional_Operators2_button = ctk.CTkButton(main_frame, text="Համակցված արտահայտություններում", font=('Bold', 20), command=show_Conditional_Operators2)
    Conditional_Operators2_button.place(x=100, y=540)
    Conditional_Operators3_button = ctk.CTkButton(main_frame, text="Օգտագործումը պայմանական արտահայտություններում", font=('Bold', 20), command=show_Conditional_Operators3)
    Conditional_Operators3_button.place(x=100, y=610)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Python_Concepts_for_Beginners)
    back_button.place(x=780, y=750)
    
def show_Conditional_Operators1():
    delate_pages()
    Conditional_Operators1 = ctk.CTkLabel(main_frame, text="Հիմնական պայմանական\n օպերատորները", font=('Bold', 35), text_color='black')
    Conditional_Operators1.pack(pady=100)
    text_content = (
        "Օպերատոր      Նկարագրություն\n"
        "   ==                   Հավասար (ստուգում է՝ արդյոք երկու\n"
        "                          արժեք հավասար են) \n"
        "   !=                    Ոչ հավասար (ստուգում է՝ արդյոք երկու\n"
        "                          արժեք հավասար չեն)\n"
        "   >                     Ավելի մեծ\n"
        "   <                     Ավելի փոքր\n"
        "   >=                   Ավելի մեծ կամ հավասար \n"
        "   <=                   Ավելի փոքր կամ հավասար\n"
        "Օրինակ        Արդյունք\n"
        "5==5                  True\n"
        "5!=3                   True\n"
        "5>3                    True\n"
        "5<3                    False\n"
        "5>=5                  True\n"
        "5<=3                  False") 
    Conditional_Operators1_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Conditional_Operators1_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Conditional_Operators_info)
    back_button.place(x=780, y=750)

def show_Conditional_Operators2():
    delate_pages()
    Conditional_Operators1 = ctk.CTkLabel(main_frame, text="      Պայմանական օպերատորներ\nհամակցված արտահայտություններ", font=('Bold', 35), text_color='black')
    Conditional_Operators1.pack(pady=100)
    text_content = (
        "       Կարելի է համատեղել պայմանական օպերատորները՝\n"
        "օգտագործելով տրամաբանական օպերատորներ:\n"
        "and: Վերադարձնում է `True`,\n"
        "եթե երկու պայմաններն էլ ճշմարիտ են։\n"
        "or: Վերադարձնում է `True`,\n"
        "եթե գոնե մեկ պայմանն է ճշմարիտ։\n"
        "not: Հակադարձում է պայմանը։\n"
        "Օրինակ.\n"
        "x = 10\n"
        "y = 20\n"
        "# Օգտագործելով 'and'\n"
        "print(x < 15 and y > 15)  # True\n"
        "# Օգտագործելով 'or'\n"
        "print(x < 5 or y > 15)    # True\n"
        "# Օգտագործելով 'not'\n"
        "print(not(x > 5))         # False") 
    Conditional_Operators1_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Conditional_Operators1_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Conditional_Operators_info)
    back_button.place(x=780, y=750)
    
def show_Conditional_Operators3():
    delate_pages()
    Conditional_Operators1 = ctk.CTkLabel(main_frame, text="Օգտագործումը պայմանական\n    արտահայտություններում", font=('Bold', 35), text_color='black')
    Conditional_Operators1.pack(pady=100)
    text_content = (
        "       Պայմանական օպերատորները հաճախ օգտագործվում\n"
        "են if, elif և else արտահայտություններում:\n"
        "Օրինակ.\n"
        "age = 18\n"
        "if age >= 18:\n"
        "    print(\"Դուք չափահաս եք։\")\n"
        "else:\n"
        "    print(\"Դուք անչափահաս եք։\")\n\n"
        "Ցանկանու՞մ եք ավելի մանրամասն օրինակներ կամ հատուկ\n"
        "դեպքեր Python-ում պայմանական օպերատորների վերաբերյալ։\n") 
    Conditional_Operators1_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Conditional_Operators1_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Conditional_Operators_info)
    back_button.place(x=780, y=750)

def show_String_info():
    delate_pages()
    String_label = ctk.CTkLabel(main_frame, text="Տող", font=('Bold', 35), text_color='black')
    String_label.pack(pady=100)
    text_content = (
        "       Python-ում տողերը (String) հիմնական տվյալների\n"
        "տեսակ են, որոնք օգտագործվում են տեքստ ներկայացնելու և\n"
        "մշակելու համար։")
    String_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    String_text.place(x=10, y=180)
    String1_button = ctk.CTkButton(main_frame, text="Ի՞նչ է տողը", font=('Bold', 20), command=show_String1)
    String1_button.place(x=100, y=300)
    String2_button = ctk.CTkButton(main_frame, text="Տողերի ստեղծում", font=('Bold', 20), command=show_String2)
    String2_button.place(x=100, y=370)
    String3_button = ctk.CTkButton(main_frame, text="Հիմնական գործողություններ տողերի հետ", font=('Bold', 20), command=show_String3)
    String3_button.place(x=100, y=440)
    String4_button = ctk.CTkButton(main_frame, text="Տողի մեթոդներ", font=('Bold', 20), command=show_String4)
    String4_button.place(x=100, y=510)
    String5_button = ctk.CTkButton(main_frame, text="Տողի ձևաչափում", font=('Bold', 20), command=show_String5)
    String5_button.place(x=100, y=580)
    String6_button = ctk.CTkButton(main_frame, text="Փախուստի սիմվոլներ", font=('Bold', 20), command=show_String6)
    String6_button.place(x=100, y=650)
    String7_button = ctk.CTkButton(main_frame, text="Տողի հատկությունների ստուգում", font=('Bold', 20), command=show_String7)
    String7_button.place(x=100, y=730)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Python_Concepts_for_Beginners)
    back_button.place(x=780, y=750)

def show_String7():
    delate_pages()
    Conditional_Operators1 = ctk.CTkLabel(main_frame, text="Տողի հատկությունների\n   ստուգում", font=('Bold', 35), text_color='black')
    Conditional_Operators1.pack(pady=100)
    text_content = (
        "       isalpha(): Ստուգում է՝ արդյո՞ք տողը\n"
        "միայն տառերից է բաղկացած։\n"
        "isdigit(): Ստուգում է՝ արդյո՞ք տողը\n"
        "միայն թվերից է։\n"
        "isalnum(): Ստուգում է՝ արդյո՞ք տողը\n"
        "միայն տառերից և թվերից է։\n"
        "isspace(): Ստուգում է՝ արդյո՞ք տողը\n"
        "միայն բացատներից է։\n"
        "text = \"Hello123\"\n"
        "print(text.isalpha())  # False\n"
        "print(text.isalnum())  # True\n") 
    Conditional_Operators1_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Conditional_Operators1_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_String_info)
    back_button.place(x=780, y=750)

def show_String6():
    delate_pages()
    Conditional_Operators1 = ctk.CTkLabel(main_frame, text="Փախուստի սիմվոլներ", font=('Bold', 35), text_color='black')
    Conditional_Operators1.pack(pady=100)
    text_content = (
        "       \\': Մեկ չակերտ։\n"
        "\\\": Կրկնակի չակերտ։\n"
        "\\\\: Հակակող։\n"
        "\\n: Նոր տող։\n"
        "\\t: Տաբուլյացիա։\n"
        "print(\"Բարև\\nԱշխարհ\")  # Արդյունքը՝\n"
        "# Բարև\n"
        "# Աշխարհ\n") 
    Conditional_Operators1_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Conditional_Operators1_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_String_info)
    back_button.place(x=780, y=750)

def show_String5():
    delate_pages()
    Conditional_Operators1 = ctk.CTkLabel(main_frame, text="Տողի ձևաչափում", font=('Bold', 35), text_color='black')
    Conditional_Operators1.pack(pady=100)
    text_content = (
        "       Python-ը տրամադրում է տողերի ձևաչափման\n"
        "մի քանի եղանակ.\n"
        "1. f-Strings (Առաջարկվում է Python 3.6+ համար)\n"
        "name = \"Աննա\"\n"
        "age = 30\n"
        "print(f\"Իմ անունն է {name}, և ես {age} տարեկան եմ։\")\n"
        "2. format() մեթոդ\n"
        "print(\"Իմ անունն է {} և ես {} տարեկան եմ։\".format(name, age))\n"
        "3. % Օպերատոր (Հին ձևաչափ)\n"
        "print(\"Իմ անունն է %s և ես %d տարեկան եմ։\" % (name, age))\n") 
    Conditional_Operators1_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Conditional_Operators1_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_String_info)
    back_button.place(x=780, y=750)

def show_String4():
    delate_pages()
    Conditional_Operators1 = ctk.CTkLabel(main_frame, text="Տողի մեթոդներ", font=('Bold', 35), text_color='black')
    Conditional_Operators1.pack(pady=100)
    text_content = (
        "       Python-ում տողերը ունեն բազմաթիվ\n"
        "ներկառուցված մեթոդներ.\n"
        "1. Տառերի մեծացման փոփոխում\n"
        "lower(): Փոքրատառերի փոխակերպում։\n"
        "upper(): Մեծատառերի փոխակերպում։\n"
        "capitalize(): Միայն առաջին տառի մեծացում։\n"
        "title(): Յուրաքանչյուր բառի առաջին տառի մեծացում։\n"
        "text = \"բարև ԱՇԽԱՐՀ\"\n"
        "print(text.lower())    # 'բարև աշխարհ'\n"
        "print(text.upper())    # 'ԲԱՐԵՎ ԱՇԽԱՐՀ'\n"
        "print(text.capitalize())  # 'Բարև աշխարհ'\n"
        "print(text.title())    # 'Բարև Աշխարհ'\n") 
    Conditional_Operators1_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Conditional_Operators1_text.place(x=10, y=250)
    next_button = ctk.CTkButton(main_frame, text="Հաջորդ էջ", font=('Bold', 15), command=show_String42)
    next_button.place(x=640, y=750)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_String_info)
    back_button.place(x=780, y=750)

def show_String42():
    delate_pages()
    Conditional_Operators1 = ctk.CTkLabel(main_frame, text="Տողի մեթոդներ", font=('Bold', 35), text_color='black')
    Conditional_Operators1.pack(pady=100)
    text_content = (
        "       2. Դատարկության հեռացում\n"
        "strip(): Հեռացնում է տողի սկզբից և\n"
        "վերջից դատարկությունները։\n"
        "lstrip(): Հեռացնում է միայն սկզբից։\n"
        "rstrip(): Հեռացնում է միայն վերջից։\n"
        "text = \"   Բարև Աշխարհ   \"\n"
        "print(text.strip())   # 'Բարև Աշխարհ'") 
    Conditional_Operators1_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Conditional_Operators1_text.place(x=10, y=250)
    next_button = ctk.CTkButton(main_frame, text="Հաջորդ էջ", font=('Bold', 15), command=show_String43)
    next_button.place(x=640, y=750)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_String4)
    back_button.place(x=780, y=750)

def show_String43():
    delate_pages()
    Conditional_Operators1 = ctk.CTkLabel(main_frame, text="Տողի մեթոդներ", font=('Bold', 35), text_color='black')
    Conditional_Operators1.pack(pady=100)
    text_content = (
        "       3. Որոնում և փոխարինում\n"
        "find(substring): Վերադարձնում է ենթատողի\n"
        "առաջին հանդիպման դիրքը (-1՝ եթե չկա)։\n"
        "replace(old, new): Փոխարինում է բոլոր հանդիպումները։\n"
        "text = \"Python-ը զվարճալի է\"\n"
        "print(text.find(\"զվարճալի\"))  # 7\n"
        "print(text.replace(\"զվարճալի\", \"հրաշալի\")) \n"
        "# 'Python-ը հրաշալի է'\n") 
    Conditional_Operators1_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Conditional_Operators1_text.place(x=10, y=250)
    next_button = ctk.CTkButton(main_frame, text="Հաջորդ էջ", font=('Bold', 15), command=show_String44)
    next_button.place(x=640, y=750)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_String42)
    back_button.place(x=780, y=750)

def show_String44():
    delate_pages()
    Conditional_Operators1 = ctk.CTkLabel(main_frame, text="Տողի մեթոդներ", font=('Bold', 35), text_color='black')
    Conditional_Operators1.pack(pady=100)
    text_content = (
        "       4. Տողի բաժանում և միացում\n"
        "split(delimiter): Բաժանում է տողը ցուցակի։\n"
        "join(iterable): Միացնում է ցուցակի տարրերը\n"
        "մեկ տողի մեջ։\n"
        "text = \"խնձոր,բանան,կեռաս\"\n"
        "print(text.split(\",\"))\n"
        "# ['խնձոր', 'բանան', 'կեռաս']\n"
        "words = [\"Միացրու\", \"այս\", \"բառերը\"]\n"
        "print(\" \".join(words))\n"
        "# 'Միացրու այս բառերը'\n"
        "Տողի ձևաչափում\n"
        "Python-ը տրամադրում է տողերի ձևաչափման\n"
        "մի քանի եղանակ.\n") 
    Conditional_Operators1_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Conditional_Operators1_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_String43)
    back_button.place(x=780, y=750)

def show_String3():
    delate_pages()
    Conditional_Operators1 = ctk.CTkLabel(main_frame, text="Հիմնական գործողություններ\n         տողերի հետ", font=('Bold', 35), text_color='black')
    Conditional_Operators1.pack(pady=100)
    text_content = (
        "       1. Միացում\n"
        "Տողերի միացումը կատարվում է + օպերատորով։\n"
        "greeting = \"Բարև\" + \" \" + \"Աշխարհ\"\n"
        "2. Կրկնություն\n"
        "Տողը կրկնվում է * օպերատորով։\n"
        "repeated = \"Բարև\" * 3  # Արդյունքը՝ \"ԲարևԲարևԲարև\"\n"
        "3. Ինդեքսավորում\n"
        "Տողի առանձին սիմվոլներին հասնում ենք ինդեքսով։\n"
        "text = \"Python\"\n"
        "first_char = text[0]  # 'P'\n"
        "last_char = text[-1]  # 'n'\n"
        "4. Կտրում (Slicing)\n"
        "Տողի մասերի ստացումը կատարվում է կտրման միջոցով։\n"
        "text = \"Python\"\n"
        "substring = text[1:4]  # 'yth'") 
    Conditional_Operators1_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Conditional_Operators1_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_String_info)
    back_button.place(x=780, y=750)

def show_String2():
    delate_pages()
    Conditional_Operators1 = ctk.CTkLabel(main_frame, text="Տողերի ստեղծում", font=('Bold', 35), text_color='black')
    Conditional_Operators1.pack(pady=100)
    text_content = (
        "       Մեկ և կրկնակի չակերտներ\n"
        "string1 = 'Բարև'\n"
        "string2 = \"Աշխարհ\"\n"
        "Բազմատող տեքստ\n"
        "multi_line = '''Սա\n"
        "բազմատող տեքստ է։'''\n") 
    Conditional_Operators1_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Conditional_Operators1_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_String_info)
    back_button.place(x=780, y=750)

def show_String1():
    delate_pages()
    Conditional_Operators1 = ctk.CTkLabel(main_frame, text="Ի՞նչ է տողը", font=('Bold', 35), text_color='black')
    Conditional_Operators1.pack(pady=100)
    text_content = (
        "       Տողը սիմվոլների հաջորդականություն է,\n"
        "որը սահմանվում է հետևյալով՝\n"
        "Մեկնարկող չակերտներ՝ 'hello'\n"
        "Կրկնակի չակերտներ՝ \"hello\"\n"
        "Եռակի չակերտներ (օգտագործվում են բազմատող\n"
        "տեքստերի համար)՝ '''hello''' կամ \"\"\"hello\"\"\"\n"
        "Տողերը անփոփոխելի են (immutable), այսինքն՝\n"
        "ստեղծվելուց հետո դրանք չեն կարող փոփոխվել։") 
    Conditional_Operators1_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Conditional_Operators1_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_String_info)
    back_button.place(x=780, y=750)

def show_Lists_info():
    delate_pages()
    Lists_label = ctk.CTkLabel(main_frame, text="Ցուցակներ", font=('Bold', 35), text_color='black')
    Lists_label.pack(pady=100)
    Lists1_button = ctk.CTkButton(main_frame, text="Ի՞նչ է ցուցակը", font=('Bold', 20), command=show_List1)
    Lists1_button.place(x=80, y=170)
    Lists2_button = ctk.CTkButton(main_frame, text="Ցուցակի ստեղծում", font=('Bold', 20), command=show_List2)
    Lists2_button.place(x=80, y=240)
    Lists3_button = ctk.CTkButton(main_frame, text="Տարրերին մուտք գործել", font=('Bold', 20), command=show_List3)
    Lists3_button.place(x=80, y=310)
    Lists4_button = ctk.CTkButton(main_frame, text="Ցուցակի Փոփոխություն", font=('Bold', 20), command=show_List4)
    Lists4_button.place(x=80, y=380)
    Lists5_button = ctk.CTkButton(main_frame, text="Հաճախ կիրառվող գործողություններ ցուցակների համար", font=('Bold', 20), command=show_List5)
    Lists5_button.place(x=80, y=450)
    Lists6_button = ctk.CTkButton(main_frame, text="Ցիկլ ցուցակի վրա", font=('Bold', 20), command=show_List6)
    Lists6_button.place(x=80, y=520)
    Lists7_button = ctk.CTkButton(main_frame, text="Կտորում (Slicing)", font=('Bold', 20), command=show_List7)
    Lists7_button.place(x=80, y=590)
    Lists8_button = ctk.CTkButton(main_frame, text="Ցուցակի մեթոդներ", font=('Bold', 20), command=show_List8)
    Lists8_button.place(x=80, y=660)
    Lists9_button = ctk.CTkButton(main_frame, text="Հիմնական հատկություններ", font=('Bold', 20), command=show_List9)
    Lists9_button.place(x=80, y=730)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Python_Concepts_for_Beginners)
    back_button.place(x=780, y=750) 

def show_List9():
    delate_pages()
    List1 = ctk.CTkLabel(main_frame, text="Հիմնական հատկություններ", font=('Bold', 35), text_color='black')
    List1.pack(pady=100)
    text_content = (
        "\n       Դինամիկություն․ Ցուցակները կարող\n"
        "են ընդարձակվել կամ փոքրանալ։\n"
        "Նույնական Ցուցակներ (Nested Lists)․ Ցուցակները\n"
        "կարող են պարունակել այլ Ցուցակներ։\n"
        "matrix = [[1, 2, 3], [4, 5, 6]]\n") 
    List1_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    List1_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Lists_info)
    back_button.place(x=780, y=750)

def show_List8():
    delate_pages()
    List1 = ctk.CTkLabel(main_frame, text="Ցուցակի մեթոդներ", font=('Bold', 35), text_color='black')
    List1.pack(pady=100)
    text_content = (
        "\nՄեթոդ\t\tՆկարագրություն\n"
        "append(x)\tԱվելացնում է տարր x վերջում։\n"
        "extend(iterable)\tԱվելացնում է բոլոր տարրերը իտերատիվից։\n"
        "insert(i, x)\t\tՏեղադրում է x-ը i ինդեքսում։\n"
        "remove(x)\t\tՀեռացնում է x-ի առաջին հանդիպումը։\n"
        "pop([i])\t\tՀեռացնում և վերադարձնում է\n"
        "        \t\ti ինդեքսի տարրը։\n"
        "clear()\t\tՀեռացնում է բոլոր տարրերը։\n"
        "index(x)\t\tՎերադարձնում է x-ի առաջին\n"
        "        \t\tհանդիպման ինդեքսը։\n"
        "count(x)\t\tՀաշվում է x-ի հանդիպումների քանակը։\n"
        "sort()\t\tԴասավորում է Ցուցակը աճման կարգով։\n"
        "reverse()\t\tՓոխում է Ցուցակի հերթականությունը։\n"
        "copy()\t\tՎերադարձնում է Ցուցակի պատճենը։\n") 
    List1_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    List1_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Lists_info)
    back_button.place(x=780, y=750)

def show_List7():
    delate_pages()
    List1 = ctk.CTkLabel(main_frame, text="Կտորում (Slicing)", font=('Bold', 35), text_color='black')
    List1.pack(pady=100)
    text_content = (
        "\n       Ցուցակի որոշակի հատված ստանալու համար։\n"
        "sub_list = numbers[1:4]  # Տարրերը 1-ից մինչև 3-րդ ինդեքս\n") 
    List1_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    List1_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Lists_info)
    back_button.place(x=780, y=750)

def show_List6():
    delate_pages()
    List1 = ctk.CTkLabel(main_frame, text="Ցիկլ ցուցակի վրա", font=('Bold', 35), text_color='black')
    List1.pack(pady=100)
    text_content = (
        "\nfor number in numbers:\n"
        "    print(number)\n\n"
        "# Օգտագործելով ինդեքս\n"
        "for i in range(len(numbers)):\n"
        "    print(numbers[i])\n") 
    List1_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    List1_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Lists_info)
    back_button.place(x=780, y=750)

def show_List5():
    delate_pages()
    List1 = ctk.CTkLabel(main_frame, text="Հաճախ կիրառվող գործողություններ\n           ցուցակների համար", font=('Bold', 35), text_color='black')
    List1.pack(pady=100)
    text_content = (
        "\n       Ավելացում (Append)․ Ավելացնում է տարրը վերջում։\n"
        "numbers.append(50)\n"
        "Ներմուծում (Insert)․ Ավելացնում է տարրը նշված դիրքում։\n"
        "numbers.insert(2, 35)  # Ավելացնում է 35-ը 2-րդ ինդեքսում\n"
        "Հեռացում (Remove)․ Հեռացնում է նշված տարրը։\n"
        "numbers.remove(25)  # Հեռացնում է առաջին հանդիպումը 25-ի\n"
        "Հեռացում և վերադարձ (Pop)․ Հեռացնում և վերադարձնում\n"
        "է նշված ինդեքսի տարրը\n"
        "(լռելյայն՝ վերջինը)։\n"
        "last_element = numbers.pop()\n"
        "Մաքրել (Clear)․ Հեռացնում է բոլոր տարրերը։\n"
        "numbers.clear()\n") 
    List1_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    List1_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Lists_info)
    back_button.place(x=780, y=750)

def show_List4():
    delate_pages()
    List1 = ctk.CTkLabel(main_frame, text="Ցուցակի Փոփոխություն", font=('Bold', 35), text_color='black')
    List1.pack(pady=100)
    text_content = (
        "\n       Ցուցակները փոփոխելի են, ուստի\n"
        "հնարավոր է փոփոխել տարրերը։\n"
        "numbers = [10, 20, 30, 40]\n"
        "print(numbers)  # Արդյունք՝ [10, 20, 30, 40]\n"
        "numbers[1] = 25\n"
        "print(numbers)  # Արդյունք՝ [10, 25, 30, 40]\n") 
    List1_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    List1_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Lists_info)
    back_button.place(x=780, y=750)

def show_List3():
    delate_pages()
    List1 = ctk.CTkLabel(main_frame, text="Տարրերին մուտք Գործել", font=('Bold', 35), text_color='black')
    List1.pack(pady=100)
    text_content = (
        "\n       Ինդեքսավորում․ Տարրերին մուտք գործեք\n"
        "ըստ նրանց ինդեքսի (սկսում է 0-ից)։\n"
        "Բացասական ինդեքսավորում․ Բացասական ինդեքսով\n"
        "կարելի է մուտք գործել Ցուցակի վերջից։\n"
        "numbers = [10, 20, 30, 40]\n"
        "print(numbers[0])  # Արդյունք՝ 10\n"
        "print(numbers[-1])  # Արդյունք՝ 40\n") 
    List1_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    List1_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Lists_info)
    back_button.place(x=780, y=750)

def show_List1():
    delate_pages()
    List1 = ctk.CTkLabel(main_frame, text="Ի՞նչ է ցուցակը", font=('Bold', 35), text_color='black')
    List1.pack(pady=100)
    text_content = (
        "\n       Ցուցակը Python-ում տվյալների կառույց է,\n"
        "որը պարունակում է տարրեր (էլեմենտներ),\n"
        "ունի կարգավորված և փոփոխվող (mutable) կառուցվածք։\n"
        "Ցուցակները թույլ են տալիս կրկնվող տարրեր։\n"
        "Դրանք սահմանվում են քառակուսի փակագծերով՝ []։") 
    List1_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    List1_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Lists_info)
    back_button.place(x=780, y=750)

def show_List2():
    delate_pages()
    List1 = ctk.CTkLabel(main_frame, text="Ցուցակի ստեղծում", font=('Bold', 35), text_color='black')
    List1.pack(pady=100)
    text_content = (
        "\n# Դատարկ Ցուցակ\n"
        "my_list = []\n\n"
        "# Ցուցակ տարրերով\n"
        "numbers = [1, 2, 3, 4, 5]\n\n"
        "# Տարբեր տիպի տվյալներով Ցուցակ\n"
        "mixed_list = [1, \"hello\", 3.5, True]\n") 
    List1_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    List1_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Lists_info)
    back_button.place(x=780, y=750)

def show_Loops_info():
    delate_pages()
    Loops_label = ctk.CTkLabel(main_frame, text="Ցիկլեր", font=('Bold', 35), text_color='black')
    Loops_label.pack(pady=100)
    Loops1_button = ctk.CTkButton(main_frame, text="for ցիկլ", font=('Bold', 20), command=show_Loops1)
    Loops1_button.place(x=100, y=200)
    Loops2_button = ctk.CTkButton(main_frame, text="while ցիկլ", font=('Bold', 20), command=show_Loops2)
    Loops2_button.place(x=100, y=270)
    Loops3_button = ctk.CTkButton(main_frame, text="Ցիկլերի կառավարման հրամաններ", font=('Bold', 20), command=show_Loops3)
    Loops3_button.place(x=100, y=340)
    Loops4_button = ctk.CTkButton(main_frame, text="Ներդրված(Nested) ցիկլեր", font=('Bold', 20), command=show_Loops4)
    Loops4_button.place(x=100, y=410)
    Loops5_button = ctk.CTkButton(main_frame, text="Անվերջ ցիկլեր", font=('Bold', 20), command=show_Loops5)
    Loops5_button.place(x=100, y=480)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Python_Concepts_for_Beginners)
    back_button.place(x=780, y=750)

def show_Loops1():
    delate_pages()
    List1 = ctk.CTkLabel(main_frame, text="for ցիկլ", font=('Bold', 35), text_color='black')
    List1.pack(pady=100)
    text_content = (
        "       Կիրառվում է տվյալների շարքի (օրինակ՝ ցուցակ, տող\n"
        "կամ զանգված) կամ այլ իտրերի կազմի վրայով անցնելու համար։\n"
        "Կառուցվածքը:\n"
        "for փոփոխական իտրերիում:\n"
        "    # Կոդի բլոկ\n"
        "Օրինակներ:\n"
        "Ցուցակի միջոցով անցնելիս:\n"
        "պտուղներ = [\"խնձոր\", \"բանան\", \"բալ\"]\n"
        "for պտուղ in պտուղներ:\n"
        "    print(պտուղ)\n"
        "range()-ի օգտագործմամբ:\n"
        "for i in range(5):  # Աշխատում է 0-ից մինչև 4\n"
        "    print(i)\n"
        "Տողի միջոցով անցնելիս:\n"
        "for նշան in \"բարև\":\n"
        "    print(նշան)") 
    List1_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    List1_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Loops_info)
    back_button.place(x=780, y=750)

def show_Loops2():
    delate_pages()
    List1 = ctk.CTkLabel(main_frame, text="while ցիկլ", font=('Bold', 35), text_color='black')
    List1.pack(pady=100)
    text_content = (
        "       Կոդի հատվածը կկատարվի այնքան ժամանակ,\n"
        "որքան պայմանը True է։\n"
        "Կառուցվածքը:\n"
        "while պայման:\n"
        "    # Կոդի բլոկ\n"
        "Օրինակներ:\n"
        "Հաշվիչի օգտագործմամբ:\n"
        "sum = 0\n"
        "while հաշվիչ < 5:\n"
        "    print(sum)\n"
        "    sum += 1\n"
        "Մուտք օգտվողից:\n"
        "enter = \"\"\n"
        "while մուտք != \"ելք\":\n"
        "    enter = input(\"Գրեք 'ելք'՝ դադարեցնելու համար: \")\n") 
    List1_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    List1_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Loops_info)
    back_button.place(x=780, y=750)

def show_Loops3():
    delate_pages()
    List1 = ctk.CTkLabel(main_frame, text="Ցիկլերի կառավարման\n       հրամաններ", font=('Bold', 35), text_color='black')
    List1.pack(pady=100)
    text_content = (
        "       Կառավարման հատուկ հրամանները թույլ են\n"
        "տալիս փոխել ցիկլի վարքագիծը։\n"
        "break: Դադարեցնում է ցիկլը։\n"
        "for i in range(5):\n"
        "    if i == 3:\n"
        "        break\n"
        "    print(i)  # Արդյունք: 0, 1, 2\n"
        "continue:Անում է հաջորդ իտերացիա,\n"
        "առանց ընթացիկը ավարտելու։\n"
        "for i in range(5):\n"
        "    if i == 3:\n"
        "        continue\n"
        "    print(i)  # Արդյունք: 0, 1, 2, 4\n"
        "else ցիկլերում: Կատարվում է միայն այն դեպքում,\n"
        "երբ ցիկլը ավարտվում է բնականոն ձևով։\n"
        "for i in range(5):print(i)\n"
        "else:print(\"Ցիկլն ավարտվեց!\")#Կկատարվի,եթե break չլինի") 
    List1_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    List1_text.place(x=10, y=230)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Loops_info)
    back_button.place(x=780, y=750)

def show_Loops4():
    delate_pages()
    List1 = ctk.CTkLabel(main_frame, text="Ներդրված ցիկլեր", font=('Bold', 35), text_color='black')
    List1.pack(pady=100)
    text_content = (
        "       Ցիկլ կարելի է տեղադրել մեկ այլ ցիկլի մեջ։\n"
        "Օրինակ:\n"
        "for i in range(3):\n"
        "    for j in range(2):\n"
        "        print(f\"i: {i}, j: {j}\")") 
    List1_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    List1_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Loops_info)
    back_button.place(x=780, y=750)

def show_Loops5():
    delate_pages()
    List1 = ctk.CTkLabel(main_frame, text="Անվերջ ցիկլեր", font=('Bold', 35), text_color='black')
    List1.pack(pady=100)
    text_content = (
        "       while ցիկլերը կարող են դառնալ անվերջ,\n"
        "եթե պայմանը միշտ True է մնում։\n"
        "Օրինակ:\n"
        "while True:\n"
        "    print(\"Անվերջ ցիկլ!\")") 
    List1_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    List1_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Loops_info)
    back_button.place(x=780, y=750)

def show_List_Comprehension_info():
    delate_pages()
    List_Comprehensions_label = ctk.CTkLabel(main_frame, text="List Comprehension", font=('Bold', 35), text_color='black')
    List_Comprehensions_label.pack(pady=100)
    text_content = (
        "\n       List Comprehension-ը կարճ և հարմարավետ\n"
        "միջոց է ցուցակներ (lists) ստեղծելու համար Python-ում։\n"
        "Այն թույլ է տալիս նոր ցուցակ\n"
        "ստեղծել՝ կիրառելով արտահայտություն (expression)՝ տվյալ\n"
        "iterable-ի յուրաքանչյուր տարրի նկատմամբ՝ ցանկության\n"
        "դեպքում ավելացնելով\n"
        "պայման։ List comprehension-ն ավելի կարդացվող և կարճ է, \n"
        "ան համարժեք ցիկլերը։") 
    List_Comprihation_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    List_Comprihation_text.place(x=10, y=250)
    List_Comprehension1_button = ctk.CTkButton(main_frame, text="Սինտաքս", font=('Bold', 20), command=show_List_Comprehension1)
    List_Comprehension1_button.place(x=100, y=580)
    List_Comprehension1_button = ctk.CTkButton(main_frame, text="Օրինակներ", font=('Bold', 20), command=show_List_Comprehension2)
    List_Comprehension1_button.place(x=100, y=650)
    List_Comprehension1_button = ctk.CTkButton(main_frame, text="Կարևոր Դետալներ", font=('Bold', 20), command=show_List_Comprehension3)
    List_Comprehension1_button.place(x=100, y=720)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Python_Concepts_for_Mid_Level)
    back_button.place(x=780, y=750)

def show_List_Comprehension3():
    delate_pages()
    List_Comprehensions_label = ctk.CTkLabel(main_frame, text="Կարևոր Դետալներ", font=('Bold', 35), text_color='black')
    List_Comprehensions_label.pack(pady=100)
    text_content = (
        "\n       Կարդացվողություն: Չնայած list\n"
        "comprehension-ը կարճ է, այն կարող է դժվար\n"
        "ընթեռնելի դառնալ, եթե չափազանց բարդ է։\n"
        "Արդյունավետություն: List comprehension-ը սովորաբար\n"
        "ավելի արագ է ցուցակներ ստեղծելու համար,\n"
        "քան համարժեք ցիկլերը։\n"
        "Պայմաններ: Կարելի է ներառել ինչպես if,\n"
        "այնպես էլ if-else պայմաններ։ Օրինակ՝\n"
        "result = [x if x % 2 == 0 else -x for x in range(1, 6)]\n"
        "print(result)  # Արդյունք: [-1, 2, -3, 4, -5]\n"
        "List comprehension-ը հզոր գործիք է Python-ում մաքուր և\n"
        "արդյունավետ կոդ գրելու համար։ Օգտագործեք այն, երբ այն\n"
        "պարզեցնում է ձեր տրամաբանությունը և\n"
        "բարելավում ընթեռնելիությունը։") 
    List_Comprihation_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    List_Comprihation_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_List_Comprehension_info)
    back_button.place(x=780, y=750)

def show_List_Comprehension2():
    delate_pages()
    List_Comprehensions_label = ctk.CTkLabel(main_frame, text="Օրինակներ", font=('Bold', 35), text_color='black')
    List_Comprehensions_label.pack(pady=100)
    text_content = (
        "\n       Հիմնական List Comprehension\n"
        "Ստեղծեք 1-ից 5 թվերի քառակուսիների ցուցակ՝\n"
        "squares = [x**2 for x in range(1, 6)]\n"
        "print(squares)  # Արդյունք: [1, 4, 9, 16, 25]\n"
        "Պայմանով List Comprehension\n"
        "Ստեղծեք 1-ից 10 զույգ թվերի ցուցակ՝\n"
        "evens = [x for x in range(1, 11) if x % 2 == 0]\n"
        "print(evens)  # Արդյունք: [2, 4, 6, 8, 10]\n"
        "Տվյալների Փոխակերպում\n"
        "Փոխակերպեք տողերի ցուցակը մեծատառի՝\n"
        "words = [\"hello\", \"world\", \"python\"]\n"
        "uppercase_words = [word.upper() for word in words]\n"
        "print(uppercase_words)  # Արդյունք:\n"
        "['HELLO', 'WORLD', 'PYTHON']") 
    List_Comprihation_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    List_Comprihation_text.place(x=10, y=250)
    next_button = ctk.CTkButton(main_frame, text="Հաջորդ էջ", font=('Bold', 15), command=show_List_Comprehension22)
    next_button.place(x=640, y=750)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_List_Comprehension_info)
    back_button.place(x=780, y=750)

def show_List_Comprehension22():
    delate_pages()
    List_Comprehensions_label = ctk.CTkLabel(main_frame, text="Օրինակներ", font=('Bold', 35), text_color='black')
    List_Comprehensions_label.pack(pady=100)
    text_content = (
        "\n       Ներդրված Ցիկլեր List Comprehension-ում\n"
        "Ստեղծեք երկու ցուցակների տարրերի\n"
        "բոլոր համակցությունների ցուցակ՝\n"
        "combinations = [(x, y) for x in [1, 2]\n"
        "for y in ['a', 'b']]\n"
        "print(combinations)  # Արդյունք:\n"
        "[(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]\n"
        "Ֆունկցիայի Կոչում\n"
        "Կիրառեք ֆունկցիա ցուցակի յուրաքանչյուր տարրի վրա՝\n"
        "def square(n):\n"
        "    return n**2\n"
        "numbers = [1, 2, 3, 4]\n"
        "squared_numbers = [square(x) for x in numbers]") 
    List_Comprihation_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    List_Comprihation_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_List_Comprehension2)
    back_button.place(x=780, y=750)

    
def show_List_Comprehension1():
    delate_pages()
    List_Comprehensions_label = ctk.CTkLabel(main_frame, text="Սինտաքս", font=('Bold', 35), text_color='black')
    List_Comprehensions_label.pack(pady=100)
    text_content = (
        "\n       List comprehension-ի ընդհանուր կառուցվածքն է՝\n"
        "[արտահայտություն տարրի համար iterable-ում եթե պայման]\n"
        "արտահայտություն: Արժեքը կամ փոփոխությունը,\n"
        "որը կիրառվում է յուրաքանչյուր տարրի նկատմամբ։\n"
        "տարր: Iterable-ի ընթացիկ տարրը։\n"
        "iterable: Հերթական կամ հավաքածու, որի վրա\n"
        "կատարվում է կրկնություն։\n"
        "պայման (ըստ ցանկության): Ֆիլտր, որը ներառում է\n"
        "միայն որոշակի տարրեր։\n") 
    List_Comprihation_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    List_Comprihation_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_List_Comprehension_info)
    back_button.place(x=780, y=750)

def show_Nested_Loops_info():
    delate_pages()
    Nested_Loops_label = ctk.CTkLabel(main_frame, text="Ներդրված ցիկլեր", font=('Bold', 35), text_color='black')
    Nested_Loops_label.pack(pady=100)
    Nested_Loops1_button = ctk.CTkButton(main_frame, text="Սինտաքս", font=('Bold', 20), command=show_Nested_Loops1)
    Nested_Loops1_button.place(x=100, y=200)
    Nested_Loops2_button = ctk.CTkButton(main_frame, text="Հաճախակի կիրառություններ", font=('Bold', 20), command=show_Nested_Loops2)
    Nested_Loops2_button.place(x=100, y=270)
    Nested_Loops3_button = ctk.CTkButton(main_frame, text="Օրինակներ", font=('Bold', 20), command=show_Nested_Loops3)
    Nested_Loops3_button.place(x=100, y=340)
    Nested_Loops4_button = ctk.CTkButton(main_frame, text="Ներդրված ցիկլերի համար խորհուրդներ", font=('Bold', 20), command=show_Nested_Loops4)
    Nested_Loops4_button.place(x=100, y=410)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Python_Concepts_for_Mid_Level)
    back_button.place(x=780, y=750)

def show_Nested_Loops4():
    delate_pages()
    List_Comprehensions_label = ctk.CTkLabel(main_frame, text="Ներդրված ցիկլերի\n  համար խորհուրդներ", font=('Bold', 35), text_color='black')
    List_Comprehensions_label.pack(pady=100)
    text_content = (
        "\n       Խուսափեք չափազանց ներմուծված ցիկլերից:\n"
        "Շատ մակարդակների ներմուծումը կարող է բարդացնել կոդի\n"
        "ընթերցումը և պահպանումը:\n"
        "Եթե հնարավոր է, օգտագործեք ֆունկցիաներ\n"
        "կամ ամփոփումներ:\n"
        "Break և Continue:\n"
        "Օգտագործեք break՝ ցիկլից դուրս գալու համար:\n"
        "Օգտագործեք continue՝ ցիկլի մարմնի մնացած մասից\n"
        "խուսափելու համար ընթացիկ դարձնումով:\n"
        "Else հետ ցիկլերի:\n"
        "Ինչպես for այնպես էլ while ցիկլերը կարող են ունենալ else բլոկ,\n"
        "որն իրականացվում է, եթե ցիկլը ավարտվում է առանց break-ի:") 
    List_Comprihation_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    List_Comprihation_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Nested_Loops_info)
    back_button.place(x=780, y=750)

def show_Nested_Loops3():
    delate_pages()
    List_Comprehensions_label = ctk.CTkLabel(main_frame, text="Օրինակներ", font=('Bold', 35), text_color='black')
    List_Comprehensions_label.pack(pady=100)
    text_content = (
        "\n       1. Ներդրված for ցիկլ ցուցակների ցուցակի հետ\n"
        "matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]\n"
        "for row in matrix:\n"
        "    for element in row:\n"
        "        print(element, end=' ')\n"
        "Արդյունք: 1 2 3 4 5 6 7 8 9\n") 
    List_Comprihation_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    List_Comprihation_text.place(x=10, y=250)
    next_button = ctk.CTkButton(main_frame, text="Հաջորդ էջ", font=('Bold', 15), command=show_Nested_Loops32)
    next_button.place(x=640, y=750)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Nested_Loops_info)
    back_button.place(x=780, y=750)

def show_Nested_Loops32():
    delate_pages()
    List_Comprehensions_label = ctk.CTkLabel(main_frame, text="Օրինակներ", font=('Bold', 35), text_color='black')
    List_Comprehensions_label.pack(pady=100)
    text_content = (
        "\n       2. Զույգեր ստեղծելը\n"
        "list1 = [1, 2, 3]\n"
        "list2 = ['A', 'B', 'C']\n"
        "\n"
        "for num in list1:\n"
        "    for char in list2:\n"
        "        print(f\"{num}{char}\", end=' ')\n"
        "Արդյունք: 1A 1B 1C 2A 2B 2C 3A 3B 3C\n") 
    List_Comprihation_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    List_Comprihation_text.place(x=10, y=250)
    next_button = ctk.CTkButton(main_frame, text="Հաջորդ էջ", font=('Bold', 15), command=show_Nested_Loops33)
    next_button.place(x=640, y=750)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Nested_Loops3)
    back_button.place(x=780, y=750)

def show_Nested_Loops33():
    delate_pages()
    List_Comprehensions_label = ctk.CTkLabel(main_frame, text="Օրինակներ", font=('Bold', 35), text_color='black')
    List_Comprehensions_label.pack(pady=100)
    text_content = (
        "\n       3. Ներդրված while ցիկլ\n"
        "i = 1\n"
        "while i <= 3:\n"
        "    j = 1\n"
        "    while j <= 3:\n"
        "        print(f\"i={i}, j={j}\")\n"
        "        j += 1\n"
        "    i += 1\n"
        "Արդյունք:\n"
        "css\n"
        "Copy code\n"
        "i=1, j=1\n"
        "i=1, j=2\n"
        "i=1, j=3\n"
        "...") 
    List_Comprihation_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    List_Comprihation_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Nested_Loops32)
    back_button.place(x=780, y=750)

def show_Nested_Loops2():
    delate_pages()
    List_Comprehensions_label = ctk.CTkLabel(main_frame, text="Հաճախակի կիրառություններ", font=('Bold', 35), text_color='black')
    List_Comprehensions_label.pack(pady=100)
    text_content = (
        "\n       Բազմադիմensional տվյալներով աշխատել:\n"
        "Ներդրված ցուցակներ, մատրիցներ կամ ցանցեր:\n"
        "Խաչաձև տեսանելիությանiterations:\n"
        "Երկու ցուցակներից տարրերի համադրություններ\n"
        "կամ փոխակերպումներ:\n"
        "Complex պայմաններ:\n"
        "Գործողություններ կատարել արժեքների զույգերով:\n") 
    List_Comprihation_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    List_Comprihation_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Nested_Loops_info)
    back_button.place(x=780, y=750)

def show_Nested_Loops1():
    delate_pages()
    List_Comprehensions_label = ctk.CTkLabel(main_frame, text="Սինտաքս", font=('Bold', 35), text_color='black')
    List_Comprehensions_label.pack(pady=100)
    text_content = (
        "\nfor outer_variable in outer_iterable:\n"
        "    for inner_variable in inner_iterable:\n"
        "        # Կոդի բլոկ, որը կատարվում է\n"
        "          յուրաքանչյուր համադրության համար") 
    List_Comprihation_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    List_Comprihation_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Nested_Loops_info)
    back_button.place(x=780, y=750)
    
def show_Dictionaries_info():
    delate_pages()
    Dictionaries_label = ctk.CTkLabel(main_frame, text="Dict", font=('Bold', 35), text_color='black')
    Dictionaries_label.pack(pady=100)
    text_content = (
        "\n       Python-ում Dictionary-ը\n"
        "հավաքածու է, որը բաղկացած է\n"
        "բանալի-գործողություն զույգերից։ Յուրաքանչյուր\n"
        "բանալի-գործողություն զույգը բաժանվում է կոլոնով (:),\n"
        "իսկ զույգերը բաժանվում են դաշտերով։ Dictionary-ը\n"
        "փակվում է աղեղավոր փակագծերի մեջ {}։"
    ) 
    Dictionaries_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    Dictionaries_text.place(x=10, y=250)
    Dictionaries1_button = ctk.CTkButton(main_frame, text="Հիմնական հատկանիշները", font=('Bold', 20), command=show_Dictionaries1)
    Dictionaries1_button.place(x=100, y=500)
    Dictionaries2_button = ctk.CTkButton(main_frame, text="Սինտաքսը", font=('Bold', 20), command=show_Dictionaries2)
    Dictionaries2_button.place(x=100, y=570)
    Dictionaries3_button = ctk.CTkButton(main_frame, text="Գործողությունները", font=('Bold', 20), command=show_Dictionaries3)
    Dictionaries3_button.place(x=100, y=640)
    Dictionaries4_button = ctk.CTkButton(main_frame, text="Կազմությունը (Comprehension)", font=('Bold', 20), command=show_Dictionaries4)
    Dictionaries4_button.place(x=100, y=720)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Python_Concepts_for_Mid_Level)
    back_button.place(x=780, y=750)

def show_Dictionaries4():
    delate_pages()
    List_Comprehensions_label = ctk.CTkLabel(main_frame, text="Կազմությունը (Comprehension)", font=('Bold', 35), text_color='black')
    List_Comprehensions_label.pack(pady=100)
    text_content = (
        "\n       Կարող եք օգտագործել Dictionary-ի կազմությունը՝\n"
        "ստեղծելու Dictionary-ներ ավելի կարճ ձևով:\n"
        "squares = {x: x**2 for x in range(5)}\n"
        "# Արդյունք՝ {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}\n"
        "Եթե ցանկանում եք ավելի մանրամասն օրինակներ կամ\n"
        "բացատրություններ, խնդրում եմ, տեղեկացրեք ինձ:")
    List_Comprihation_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    List_Comprihation_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Dictionaries_info)
    back_button.place(x=780, y=750)

def show_Dictionaries3():
    delate_pages()
    List_Comprehensions_label = ctk.CTkLabel(main_frame, text="Գործողությունները", font=('Bold', 35), text_color='black')
    List_Comprehensions_label.pack(pady=100)
    text_content = (
        "\n       1. Գործողությունների մուտք:\n"
        "Դուք կարող եք մուտք գործել արժեքները՝ նշելով\n"
        "դրանց բանալին։\n"
        "print(my_dict['name'])  # Արդյունք՝ John\n"
        "2. Ավելացնել կամ թարմացնել տարրեր:\n"
        "Դուք կարող եք ավելացնել կամ թարմացնել տարրը՝\n"
        "նշանակելով արժեք բանալիի համար։\n"
        "my_dict['age'] = 31  # Թարմացնում ենք 'age'-ի արժեքը\n"
        "my_dict['job'] = 'Engineer'  # Ավելացնում ենք\n"
        "նոր բանալի-գործողություն զույգ\n"
        "3. Տարրերի ջնջում:\n"
        "del կարելի է օգտագործել՝ բանալիով ջնջելու համար։\n"
        "del my_dict['city']\n"
        "# Ջնջում ենք 'city' բանալի-գործողություն զույգը") 
    List_Comprihation_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    List_Comprihation_text.place(x=10, y=200)
    next_button = ctk.CTkButton(main_frame, text="Հաջորդ էջ", font=('Bold', 15), command=show_Dictionaries32)
    next_button.place(x=640, y=750)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Dictionaries_info)
    back_button.place(x=780, y=750)

def show_Dictionaries32():
    delate_pages()
    List_Comprehensions_label = ctk.CTkLabel(main_frame, text="Գործողությունները", font=('Bold', 35), text_color='black')
    List_Comprehensions_label.pack(pady=100)
    text_content = (
        "\n       4. Մեթոդներ:\n"
        "my_dict.keys() – Հետևում է Dictionary-ում բոլոր\n"
        "բանալիների ցուցակը։\n"
        "my_dict.values() – Հետևում է Dictionary-ում բոլոր\n"
        "արժեքների ցուցակը։\n"
        "my_dict.items() – Հետևում է Dictionary-ում բոլոր\n"
        "բանալի-գործողություն զույգերի ցուցակը։\n"
        "my_dict.get(key) – Հետադարձում է տվյալ բանալիի արժեքը\n"
        "(վերադարձնում է None, եթե բանալին չի գտնվել)։\n"
        "my_dict.pop(key) – Ջնջում և վերադարձնում է տվյալ\n"
        "բանալիի արժեքը։\n"
        "my_dict.update(other_dict) – Թարմացնում է Dictionary-ն՝\n"
        "ավելացնելով մյուս Dictionary-ի տարրերը։\n") 
    List_Comprihation_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    List_Comprihation_text.place(x=10, y=200)
    next_button = ctk.CTkButton(main_frame, text="Հաջորդ էջ", font=('Bold', 15), command=show_Dictionaries33)
    next_button.place(x=640, y=750)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Dictionaries3)
    back_button.place(x=780, y=750)

def show_Dictionaries33():
    delate_pages()
    List_Comprehensions_label = ctk.CTkLabel(main_frame, text="Գործողությունները", font=('Bold', 35), text_color='black')
    List_Comprehensions_label.pack(pady=100)
    text_content = (
        "\n       Ստեղծում ենք **Dictionary**\n"
        "my_dict = {\n"
        "    'name': 'Alice',\n"
        "    'age': 25,\n"
        "    'city': 'Paris'\n"
        "}\n"
        "# Գործողությունների մուտք\n"
        "print(my_dict['name'])  # Արդյունք՝ Alice\n"
        "# Նոր բանալի-գործողություն զույգ ավելացնել\n"
        "my_dict['job'] = 'Engineer'\n"
        "# Ջնջում ենք բանալի-գործողություն զույգ\n"
        "my_dict.pop('city')\n"
        "# get մեթոդի օգտագործում\n"
        "print(my_dict.get('age'))  # Արդյունք՝ 25\n"
        "# Թարմացնում ենք **Dictionary**-ը\n"
        "my_dict.update({'age': 26, 'country': 'France'})") 
    List_Comprihation_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    List_Comprihation_text.place(x=10, y=200)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Dictionaries32)
    back_button.place(x=780, y=750)

def show_Dictionaries2():
    delate_pages()
    List_Comprehensions_label = ctk.CTkLabel(main_frame, text="Սինտաքսը", font=('Bold', 35), text_color='black')
    List_Comprehensions_label.pack(pady=100)
    text_content = (
        "\n        Ստեղծում ենք Dictionary\n"
        "my_dict = {\n"
        "    'name': 'John',\n"
        "    'age': 30,\n"
        "    'city': 'New York'\n"
        "}\n") 
    List_Comprihation_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    List_Comprihation_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Dictionaries_info)
    back_button.place(x=780, y=750)    

def show_Dictionaries1():
    delate_pages()
    List_Comprehensions_label = ctk.CTkLabel(main_frame, text="Հիմնական հատկանիշները", font=('Bold', 35), text_color='black')
    List_Comprehensions_label.pack(pady=100)
    text_content = (
        "\n       1. Բանալի և Գործողություն:\n"
        "Բանալի: Գործողության միավորող ճանաչիչ\n"
        "(կարող է լինել ցանկացած անփոփոխ տեսակ, ինչպես\n"
        "օրինակ՝ տողեր, թվեր կամ թվարկներ)։\n"
        "Գործողություն: Գործողությունը, որը կապված է տվյալ\n"
        "բանալիի հետ (կարող է լինել ցանկացած տվյալների տեսակ՝\n"
        "ներառյալ ցուցակներ, այլ Dictionary-ներ և այլն)։\n"
        "2. Անարդար (Unordered): Python-ում Dictionary-ները չեն\n"
        "պահպանում տարրերի կարգը (չնայած սկսած Python 3.7-ից,\n"
        "դրանք պահպանում են ներմուծման կարգը)։\n"
        "3. Փոփոխվող: Դուք կարող եք փոփոխել, ավելացնել կամ\n"
        "ջնջել տարրեր Dictionary-ում։\n"
        "4. Բանալիի կրկնություն չի կարող լինել: Յուրաքանչյուր\n"
        "բանալի Dictionary-ում պետք է լինի եզակի։") 
    List_Comprihation_text = ctk.CTkLabel(main_frame, text=text_content, font=('Bold', 20), text_color='black')
    List_Comprihation_text.place(x=10, y=250)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Dictionaries_info)
    back_button.place(x=780, y=750)

def show_Functions_info():
    delate_pages()
    Functions_label = ctk.CTkLabel(main_frame, text="Ֆունկցիաներ", font=('Bold', 35), text_color='black')
    Functions_label.pack(pady=100)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Python_Concepts_for_Mid_Level)
    back_button.place(x=780, y=750)

def show_Recursion_info():
    delate_pages()
    Recursion_label = ctk.CTkLabel(main_frame, text="Ռեկուրսիա", font=('Bold', 35), text_color='black')
    Recursion_label.pack(pady=100)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Python_Concepts_for_Mid_Level)
    back_button.place(x=780, y=750)

def show_Tuples_and_Sets_info():
    delate_pages()
    Tuples_and_Sets_label = ctk.CTkLabel(main_frame, text="Tuple-ներ և Set-եր", font=('Bold', 35), text_color='black')
    Tuples_and_Sets_label.pack(pady=100)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Python_Concepts_for_Mid_Level)
    back_button.place(x=780, y=750)

def show_Lambda_Functions_info():
    delate_pages()
    Lambda_Functions_label = ctk.CTkLabel(main_frame, text="Լամբդա ֆունկցիաներ", font=('Bold', 35), text_color='black')
    Lambda_Functions_label.pack(pady=100)
    back_button = ctk.CTkButton(main_frame, text="Հետ", font=('Bold', 15), command=show_Python_Concepts_for_Mid_Level)
    back_button.place(x=780, y=750)





options_frame = ctk.CTkFrame(root, fg_color="#c3c3c3", width=150, height=1000)
options_frame.pack(side="left", fill="y")

home_btn = ctk.CTkButton(
    options_frame, text="Home", font=("Arial Bold", 15), text_color="#158aff",
    fg_color="#c3c3c3", hover_color="#a3a3a3", command=lambda: indicate(home_indicate, home_page)
)
home_btn.place(x=10, y=50)

home_indicate = ctk.CTkLabel(options_frame, text="", fg_color="#c3c3c3", width=5, height=40)
home_indicate.place(x=3, y=50)

info_btn = ctk.CTkButton(
    options_frame, text="Info", font=("Arial Bold", 15), text_color="#158aff",
    fg_color="#c3c3c3", hover_color="#a3a3a3", command=lambda: indicate(info_indicate, info_page)
)
info_btn.place(x=10, y=100)

info_indicate = ctk.CTkLabel(options_frame, text="", fg_color="#c3c3c3", width=5, height=40)
info_indicate.place(x=3, y=100)

main_frame = ctk.CTkFrame(
    root, fg_color="white", corner_radius=10, border_width=2, border_color="black",
    width=850, height=1000
)
main_frame.pack(side="left", fill="both", expand=True)
start_page()
root.mainloop()
