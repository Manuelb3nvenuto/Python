#all this were copy and paste because i made them time ago, that's why there are not that many commits

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)


high_score = student_scores[0]
for current_score in student_scores:
  if current_score> high_score:
    high_score = current_score

print(f"The highest score in the class is: {high_score}")