students=[
    {"name": "Sanskriti", "clique": "Nerd"},
    {"name": "Samyak", "clique": "Coder"},
    {"name": "Preetansh", "clique": "Idiot"}
]

#def f(person):
#    return person["clique"]

students.sort(key=lambda person: person["clique"])

print(students)