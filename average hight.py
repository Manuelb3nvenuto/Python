#all this were copy and paste because i made them time ago, that's why there are not that many commits
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])




total_height = 0
for height in student_heights:
  total_height += height
  number_of_students=len(student_heights)
average_height=round(total_height/number_of_students)
print(average_height)