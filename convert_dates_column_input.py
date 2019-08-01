# USER INPUT REQUEST

def main():
    print("Dieses Programm hilft dir bei der Umwandlung von europäischen Datumsangaben \n in ein maschinenlesbares Format. \n Bitte gebe deine Liste mit Daten im Format TT.MM.JJJJ ein. \n Nutze dabei eine neue Zeile zur Trennung der Daten und bestätige die Eingabe mit einem beliebigen Buchstaben.")

# USER DATA READ

    ddmmyyyy=[]
    while input:
        line = input()
        ddmmyyyy.append(line)

        if len(line) < 2:
            print ("Danke für die Eingabe!")
            break
            
# INVERSION OF STRINGS

    output_list = []
    for i in ddmmyyyy:
        output_list.append(i[6:] + "-" + i[3:5] + "-" + i[:2])
    del output_list[-1]    

# OUTPUT DATA IN TWO DIFFERENT FORMATS AS ROWS AND COLUMNS
        
    print("Hier sind deine Daten im neuen Format als Spalte: \n \n", '\n'.join(output_list), "\n  \n") 

    print("Hier sind deine Daten im neuen Format als Zeile: \n \n", '\t'.join(output_list), "\n  \n")

# REPEAT OR EXIT

while True:
    main()
    if input("Programm wiederholen? (J/N)").strip().upper() != 'J':
        print("\n \n Viel Erfolg und bis zum nächsten Mal!")
        break

    




  
