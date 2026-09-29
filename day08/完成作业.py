# def is_palindrome():
#     wr=input('请输入文本')
#     if wr==wr[::-1]:
#         print('是回文')
#     else:
#         print('不是回文')
# is_palindrome()
#
# def count_words():
#     eng=input('请输入你的文本')
#     eng=eng.split()
#     print(len(eng))
# count_words()
#
#
#
# def calc_average():
#     grade=input('输入班级分数')
#     grade=grade.split()
#     num=int(input('班级数量'))
#     total=0
#     for s in grade:
#         total=total+int(s)
#         average_grade=total/len(grade)
#     return(average_grade)
# average_grade=calc_average()
# print(average_grade)
#
# def get_grade(score):
#     if score>=90:
#         return 'A'
#     elif score>=80:
#         return 'B'
#     elif score>=70:
#         return 'C'
#     elif score>=60:
#         return 'D'
#     else:
#         return 'F'
# # get_grade(90)
# print(get_grade(80))

def analyze_class():
    grades = input('请输入班级里面的成绩')
    grades=grades.split()
    grades=list(zip(grades[::2],grades[1::2]))
    total=0

    all_grades = []
    for i in grades:
        nums=i[1]
        all_grades.append(nums)
        total=total+int(nums)
        average_grade=total/len(all_grades)
        if int(nums)>=60:
            # print(nums)
            true=nums
            nums_true=len(all_grades)/len(true)
            print('合格率:',nums_true)

    print('平均分:',average_grade)
    return all_grades
s=analyze_class()
print('最大的值:',max(s))
print('最小的值',min(s))
average_grade=analyze_class()
print(analyze_class())






    