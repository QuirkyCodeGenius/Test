print("NOTAS ESTUDIANTES")
nombreEstudiante = str(input("ingrese el nombre del estudiante: "))
firstNote = float(input("ingrese la nota del primer corte: ")) # 20% of semester
secondNote = float(input("ingrese la nota del segundo corte: ")) # 30% of semester
thirdNote = float(input("ingrese la nota del tercer corte: ")) # 50% of semester

promedio = firstNote*0.2 + secondNote*0.3 + thirdNote*0.5
print("la nota final del semestre del estduiante ", nombreEstudiante," es: ", promedio)
