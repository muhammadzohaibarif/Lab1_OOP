from course import Course, InvalidMarksError,load_course

c = Course("Programming for AI")
c.add_student("Ali", 88)
c.add_student("Sara", 92)
c.add_student("Omar", 75)

try:
    c.add_student("Bilal", 100)
except InvalidMarksError as e:
    print("Error:", e)

print(c)

course = load_course("Programming for AI", "marks.txt")
print(course)
print("Top student:", course.top_student())

c = Course("X");  
c.add_student("Ali", 88)
c.remove_student("Ali")
print(len(c))

try:
    c.remove_student("Zara")
except KeyError as e:
    print("keyError:", e)
