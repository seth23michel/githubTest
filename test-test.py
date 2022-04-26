import easygui

if __name__ == '__main__':
   con = easygui.ynbox("Should I continue", 'Yes or No', ('Yes', 'No'))

   if con:
      easygui.msgbox(f'Hello World', title="Tester test")
   else:
      choice = easygui.buttonbox('Click on your favorite flavor.', 'Favorite Flavor', ('Chocolate', 'Vanilla', 'Strawberry'))
      print(choice)
