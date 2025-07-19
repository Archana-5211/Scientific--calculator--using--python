import math
def basic_calculator():
    x = float(input("Enter first number: "))
    optr = input("Enter operator (+, -, *, /, %, ^): ")
    y = float(input("Enter second number: "))

    if optr =='+':
        return x+y
    elif optr =='-':
        return x-y
    elif optr =='*':
        return x*y
    elif optr =='^':
        return x**y
    elif optr =='%':
        return x%y
    elif optr =='/':
        if y!=0:
          return x/y
        else:
            return "Error:division by zero"
    else:
        print("Invalid operator")
def scientific_calculator():
    def power(a, b):
        return math.pow(a, b) 
    def sqrt(a):
        return math.sqrt(a) 
    def log10(a):
        return math.log10(a)
        return math.log10(a) 
    def log(a):
        return math.log(a)
    def sin(a):
        return math.sin(math.radians(a))
    def cos(a):
        return math.cos(math.radians(a))
    def tan(a):
        return math.tan(math.radians(a))
    def sec(a):
        s=math.cos(math.radians(a))
        if s==0:
            return "Undefined(cos=0)"
        else:
            return 1/s
    def cosec(a):
        c=math.sin(math.radians(a))
        if c==0:
            return "Undefined(sin=0)"
        else:
            return 1/c
    def cot(a):
        t=math.tan(math.radians(a))
        if t==0:
            return "Undefined(tan=0)"
        else:
            return 1/t
    def exponential(a):
        return math.exp(a)
    print("\n---Scientific Calculator---")
    print("1.Power\n2.sqrt\n3.log10\n4.log\n5.sin\n6.cos\n7.tan\n8.sec\n9.cosec\n10.cot\n11.exponential")
    choice=input("Choose option (1-11):")
    if choice=='1':
        a=float(input("Enter base:"))
        b=float(input("Enter exponent:"))
        print("Result:",power(a,b))
    elif choice=='2':
        a=float(input("Enter number:"))
        print("Result:",sqrt(a))
    elif choice=='3':
        a=float(input("Enter number:"))
        print("Log:",log10(a))
    elif choice=='4':
        a=float(input("Enter number:"))
        print("Log:",log(a))
    elif choice=='5':
        a=float(input("Enter angle in degree:"))
        print("Sine",sin(a))
    elif choice=='6':
        a=float(input("Enter angle in degree:"))
        print("Cosine",cos(a))
    elif choice=='7':
        a=float(input("Enter angle in degree:"))
        print("Tangent",tan(a))
    elif choice=='8':
        a=float(input("Enter angle in degree:"))
        print("Secant",sec(a))
    elif choice=='9':
        a=float(input("Enter angle in degree:"))
        print("Cosecant",cosec(a))
    elif choice=='10':
        a=float(input("Enter angle in degree:"))
        print("Cotangent",cot(a))
    elif choice=='11':
        a=float(input("Enter number:"))
        print(f"e^{a}=",exponential(a))
    else:
        print("Invalid choice")

def unit_converter():
    def cm_to_inch(cm): return cm / 2.54
    def inch_to_cm(inch): return inch * 2.54
    def kg_to_g(kg): return kg * 1000.0
    def g_to_kg(g): return g / 1000.0
    def c_to_f(c): return (c * 9/5) + 32
    def f_to_c(f): return (f - 32) * 5/9
    def k_to_c(k):return(k - 273.15)
    def c_to_k(c):return(c + 273.15)

    print("\n--- Unit Converter ---")
    print("1. CM to INCH\n2. INCH to CM\n3. KG to gram\n4.gram to KG\n5. °C to °F\n6. °F to °C\n7.K to °C\n8.°C to K" )
    choice = input("Choose option (1-8): ")
    value = float(input("Enter value: "))

    if choice == '1':
        print("Inches:", cm_to_inch(value))
    elif choice == '2':
        print("CM:", inch_to_cm(value))
    elif choice == '3':
        print("Pounds:", kg_to_g(value))
    elif choice == '4':
        print("Kilograms:", g_to_kg(value))
    elif choice == '5':
        print("Fahrenheit:", c_to_f(value))
    elif choice == '6':
        print("Celsius:", f_to_c(value))
    elif choice == '7':
        print("Celsius:", k_to_c(value))
    elif choice == '8':
        print("Kelvin:", c_to_k(value))

    else:
        print("Invalid Choice")

def main():
    print("Welcome to the Calculator!")
    print("1. Basic Calculator")
    print("2. Scientific Calculator")
    print("3.Unit Converter")

    choice = input("Choose option (1 or 2 or 3): ")
    if choice == '1':
        
        print("Result:", basic_calculator())
    elif choice == '2':
        scientific_calculator()
    elif choice=='3':
        unit_converter()
    else:
        print("Invalid choice!")
main()