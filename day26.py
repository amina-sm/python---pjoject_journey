# # numbers = [1, 2, 3]
# # new_list = [n+1 for n in numbers]
# # print(new_list)

# # range_list = [n*2 for n in range(1, 5)]
# # print(range_list)

# # names = ["amina", "tatu", "emmy", "fetty", "abubakar"]
# # short_names = [name for name in names if len(name) < 5]
# # print(short_names)


import random
names = ["amina", "tatu", "emmy", "fetty", "abubakar"]
# long_names = [name.upper() for name in names if len(name) < 5]
# print(long_names)
# #

student_scores = {student: random.randint(1, 100) for student in names}
print(student_scores)

passed_student = {student: score for (
    student, score) in student_scores.items()if score >= 60}
print(passed_student)
