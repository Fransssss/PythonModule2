# author: Fransiskus Agapa
# module
import hello as hl
import greet as g
import smalltalk as st
import goodbye as gb

print("\n== Module Menu ==")
print("1. Hello module")
print("2. Greet module")
print("3. Small talk module")
print('4. Good bye module')
print("E. Exit")
choice = input("choice: ")

while choice != 'e' and choice != 'E':
    if choice == '1':
        print("\n[ Hello module ]")
        hl.hello()
    elif choice == '2':
        print("\n[ Greet module ]")
        g.greet()
    elif choice == '3':
        print("\n[ Small talk module ]")
        st.smalltlk()
    elif choice == '4':
        print("\n[ Good bye module ]")
        gb.goodby()
    else:
        print("\n[ Invalid choice ]")

    print("\n== Module Menu ==")
    print("1. Hello module")
    print("2. Greet module")
    print("3. Small talk module")
    print('4. Good bye module')
    print("E. Exit")
    choice = input("choice: ")

if choice == 'e' or choice == 'E':
    print("\nExit Program")