import random


students = ["გიორგი ნოზაძე","ლუკა დემეტრაშვილი","გიორგი როდონაია","ზუკა გველესიანი","სერგი ჩიხრაძე" 
,"დავით წიქრიძე","ლუკა ჩიტიძე","ლუკა ჭუმბაშვილი","ლუკა პაპაშვილი","ნიკუშა ყუბანეიშვილი"
,"გიორგი ჭედლიშვილი","ბესიკ გელხაური","ილია ირემაძე","სანრო სუხიშვილი"]


leader1 = ["ირაკლი უგულავა"]
leader2 = ["თაზო კუტალია"]
leader3 = ["გიორგი ნინიაშვილი"]
leader4 = ["ნიკოლას დვალი"]
leader5 = ["ნიკოლოზ კურტანიძე"]

leaders = [leader1,leader2,leader3,leader4,leader5]

for leader in leaders:
    while len(leader) != 4:
        if students == []:
            break
        random_student = random.choice(students)
        leader.append(random_student)
        students.remove(random_student)

print(leader1)
print(leader2)
print(leader3)
print(leader4)
print(leader5)
