# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.

def course_info():
    course_dict = {}
    while True:
        course_id = input("Enter the course ID (or type 'exit' to finish): ")
        if course_id.lower() == 'exit':
            break
        course_name = input("Enter the course name: ")
        course_dict[course_id] = course_name

    subject_input = input("Enter the subject to search for (e.g., 'COS'): ")

    
    matching_courses = []

    for course_id, course_name in course_dict.items():
        if course_id.startswith(subject_input):
            matching_courses.append((course_id, course_name))

    if not matching_courses:
        print("No courses found for the subject.")
    else:
        print(f"Courses for subject '{subject_input}':")
        for course_id, course_name in matching_courses:
            print(f"{course_id}: {course_name}")


course_info()
