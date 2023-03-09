#Adebiyi Abass
#CS-175L-02
#Average

def calc_average(score1, score2, score3, score4, score5):
    average = (score1 + score2 + score3 + score4 + score5)
    print ('Average')

def determine_grade(score):
    if score>= 90:
        print('A')
    elif score>= 80:
        print('B')
    elif score>= 70:
        print('C')
    elif score>= 60:
        print('D')
    else:
        print('F')

score1 = int(input("Enter score 1: "))
score2 = int(input("Enter score 2: "))
score3 = int(input("Enter score 3: "))
score4 = int(input("Enter score 4: "))
score5 = int(input("Enter score 5: "))

avg = calc_average(score1, score2, score3, score4, score5)

print("Score 1: {} Grade: {}". format(score1, determine_grade(score1)))
print("Score 2: {} Grade: {}". format(score2, determine_grade(score2)))
print("Score 3: {} Grade: {}". format(score3, determine_grade(score3)))
print("Score 4: {} Grade: {}". format(score4, determine_grade(score4)))
print("Score 5: {} Grade: {}". format(score5, determine_grade(score5)))

