student_score=input("enter student scores:")

scores=[int (score) for score in student_score.split(",") ]

grades=["A" if score >=90 else
        "B" if score >=80 else
        "c" if score >=70 else
        "D" if score >=60 else
        "E" if score >=50 else
        "F"
        for score in scores   
        ]

passing_students=[score for score in scores if score>50]
failing_students=[score for score in scores if score<50]

print("---students grade---")

for i,(score,grade)in enumerate (zip(scores,grades),start=1):
    print(f"students {i}: score={score},grade={grade}")

print("------Passing and Failing students----")
print("passing students:",passing_students)
print("failing students:",failing_students)