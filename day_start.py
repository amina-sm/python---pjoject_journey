# from turtle import Turtle,Screen
# timmy=Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)

# my_screen=Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable
table= PrettyTable()
table.add_column("Family Name", ["Fatuma","Age","Tatu"])
table.add_column("Age", [12,8,4])
table.align="l"
print(table)