n = int(input())
student_marks = dict()

for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

chosen_student = str(input())

test = student_marks.get(chosen_student)
result = sum(test) / len(test)
print(f'{result:.2f}')
