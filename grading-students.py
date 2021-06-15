
def gradingStudents(grades):
    after_grade = list()
    for grade in grades:
        new_grade = grade
        while(new_grade%5 !=0):
            new_grade+=1
        if (grade < 38):
            after_grade.append(grade)
        elif ((new_grade - grade) < 3):
            after_grade.append(new_grade)
        else:
            after_grade.append(grade)
    
    return after_grade



def main():
    gr = [73,67,38,33]
    after_grade = gradingStudents(gr)
    print(after_grade)

if __name__ == "__main__":
    main()

