# γραμμή 6: ο χρήστης εισάγει το μήκος της πρώτης κάθετης πλευράς (δεκαδικός αριθμός) του ορθογωνίου τριγώνου και ορίζει τη μεταβλητή x
# γραμμή 7: ο χρήστης εισάγει το μήκος της δεύτερης κάθετης πλευράς (δεκαδικός αριθμός) του ορθογωνίου τριγώνου και ορίζει τη μεταβλητή y
# γραμμή 8: οι δύο μεταβλητές πολ/ζονται μεταξύ τους, διαιρούνται δια 2 και το αποτέλεσμα ορίζει τη μεταβλητή z  
# γραμμή 9: εμφανίζεται κείμενο και η μεταβλητή z (ως κείμενο)

x = float(input ("Εισάγετε το μήκος της πρώτης κάθετης πλευράς:"))
y = float(input ("Εισάγετε το μήκος της δεύτερης κάθετης πλευράς:"))
z = float((x * y) / 2)
print ("το εμβαδόν του τριγώνου είναι: "  + str(z))
