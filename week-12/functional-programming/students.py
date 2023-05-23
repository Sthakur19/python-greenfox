# Students
# Given a list of students with the following fields: name, age, gender and grades.

# Create a new list that only includes the boys
# Create a new list that only includes who's name starts with the letter J
# Create a new list that only includes the girls
# Create a new list that only includes who's grade average is above 4
# Create a new list that only includes the boys who's name starts with the letter J
# Create a new list that only includes the girls who's grade average is above 4
# Create a new list that only includes who's at least two 5s
# Create a new list that only includes who's grade average is above 4 and at at least got two 5s

students = [
{'name': 'John', 'age': 16, 'gender': 'male', 'grades': [5,5,4,2]},
{'name': 'Jane', 'age': 15, 'gender': 'female', 'grades': [4,3,4,4,5]},
{'name': 'Bob', 'age': 17, 'gender': 'male', 'grades': [2,2,3,1]}
]

list_only_boys = [student for student in students if student['gender'] == 'male']
print(list_only_boys)

name_start_with_j = [student for student in students if student['name'][0] == 'J']
print(name_start_with_j)

list_only_girls = [student for student in students if student['gender'] == 'female']
print(list_only_girls)

list_grade_avg_above_4 = [student for student in students if sum(student['grades'])/len(student['grades']) > 4]
print(list_grade_avg_above_4)

list_boy_name_start_j = [student for student in students if student['gender'] == 'male' and student['name'][0] == 'J']
print(list_boy_name_start_j)

list_girl_grade_above_4 = [student for student in students if student['gender'] == 'female' and 
sum(student['grades'])/len(student['grades']) > 4]
print(list_grade_avg_above_4)

list_include_two_5 = [student for student in students if student['grades'].count(5) >= 2]
print(list_include_two_5)

list_include_two_5_avg_above_4 = [student for student in students if student['grades'].count(5) >= 2 and 
sum(student['grades'])/len(student['grades']) >= 4 ] 
print(list_include_two_5_avg_above_4)


# for student in students:
#     print(sum(student['grades'])/len(student['grades']))