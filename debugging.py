# def my_function ():
#     for i in range(1,21):
#         if i==20:
#             print("You got it")
# my_function()            

# from random import randint
# dice_img=["1","2","3","4","5","6"]
# dice_num=randint(0,5)
# print(dice_img[dice_num])


pages=0
word_per_page=0
pages=int(input("Number of pages: "))
word_per_page=int(input("Number of words per page: "))
total_words= word_per_page * pages
print(total_words)