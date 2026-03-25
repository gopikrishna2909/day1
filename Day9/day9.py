student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
print(max(student_scores, key=student_scores.get))

# student_grades = {}
# for key in student_scores:
#     if 91<student_scores[key]<100:
#         student_grades[key]="Outstanding"
#     elif 81<student_scores[key]<90:
#         student_grades[key]="Exceeds Expectations"
#     elif 71<student_scores[key]<80:
#         student_grades[key]="Acceptable"
#     else:
#         student_grades[key]="Fail"
# #print(student_grades)
#
#
# travel_log ={
#     "France": ["Paris","Lille","Digino"],
#     "Andhra": {
#         "college": "Andhra University",
#         "degree": "Btech",
#         "branch":["ece","cse","mech","eee"]
#
#     }
# }
# print(travel_log["Andhra"]["branch"][0])
