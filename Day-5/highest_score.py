student_scores = [180, 124, 165, 173, 189, 169, 146]
total_score = sum(student_scores)
# for score in student_scores:
#     total_score += score

# print(f"The total score is {total_score}")
# print(f"The highest score is {max(student_scores)}")

highest_score = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score

print(highest_score)
