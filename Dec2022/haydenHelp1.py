color1 = input("Enter a color: ")
color2 = input("Enter a second color: ")

def colors(color1, color2):
    # if user enters blue and red, then print purple
    if (color1 == "red" and color2 == "blue") or (color1 == "blue" and color2 == "red"):
        print("When you mix red and blue, you get purple.")
    # if user enters red and yellow, then print orange
    elif (color1 == "red" and color2 == "yellow") or (color1 == "yellow" and color2 == "red"):
        print("When you mix red and yellow, you get orange.")
    # if user enters blue and yellow, then print green
    elif (color1 == "blue" and color2 == "yellow") or (color1 == "yellow" and color2 == "blue"):
        print("When you mix blue and yellow, you get green.")
    # if user enters any other combination, then print error
    else:
        print("Error: Invalid color(s) entered.")
        
colors(color1, color2)
    