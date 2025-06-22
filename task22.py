def group_students(students: list[dict[str, str]]) -> dict[str, list[str]]:
    groups = {}

    for student in students:
        groups[student['group']] = []

    for student in students:
        groups[student['group']].append(student['name'])

    return groups

students = [
    {
        "name":"ali",
        "group":"A"
    },
    {
        "name":"vali",
        "group":"B"
    },

    {
        "name":"jon",
        "group":"A"
    },
    {
        "name":"bob",
        "group":"C"
    }
]

result = group_students(students)
print(result)