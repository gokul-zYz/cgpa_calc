tcp=0
tgp=0
S=10
A=9
B=8
C=7
D=6
E=5
F=4
def first(grade_point1,grade_point2,grade_point3,grade_point4,grade_point5,grade_point6,
    grade_pointlab1,grade_pointlab2,grade_pointlab3):
    global tcp
    global tgp
    tcp+=30
    current=((grade_point1*4+grade_point2*4+grade_point3*4+grade_point4*4
        +grade_point5*4+grade_point6*4+grade_pointlab1*2+grade_pointlab2*2
        +grade_pointlab3*2))
    tgp+=current
    print(current/30)
        
def second(grade_point1,grade_point2,grade_point3,grade_point4,grade_point5,grade_point6,
    grade_pointlab1,grade_pointlab2,grade_pointlab3):
    global tcp
    global tgp
    tcp+=30
    current=((grade_point1*4+grade_point2*4+grade_point3*4+grade_point4*4
        +grade_point5*4+grade_point6*4+grade_pointlab1*2+grade_pointlab2*2
        +grade_pointlab3*2))
    tgp+=current
    print(current/30)
def third(grade_point1,grade_point2,grade_point3,grade_point4,grade_point5,grade_point6,
    grade_pointlab1,grade_pointlab2,grade_pointlab3):
    global tcp
    global tgp
    tcp+=30
    current=((grade_point1*4+grade_point2*4+grade_point3*4+grade_point4*4
        +grade_point5*4+grade_point6*4+grade_pointlab1*2+grade_pointlab2*2
        +grade_pointlab3*2))
    tgp+=current
    print(current/30)
def fourth(grade_point1,grade_point2,grade_point3,grade_point4,grade_point5,grade_point6,
    grade_pointlab1,grade_pointlab2,grade_pointlab3):
    global tcp
    global tgp
    tcp+=30
    current=((grade_point1*4+grade_point2*4+grade_point3*4+grade_point4*4
        +grade_point5*4+grade_point6*4+grade_pointlab1*2+grade_pointlab2*2
        +grade_pointlab3*2))
    tgp+=current
    print(current/30)
def fifth(grade_point1,grade_point2,grade_point3,grade_point4,grade_point5,grade_point6,
    grade_pointlab1,grade_pointlab2,grade_pointlab3,grade_pointlab4):
    global tcp
    global tgp
    tcp+=31
    current=((grade_point1*4+grade_point2*4+grade_point3*4+grade_point4*4
        +grade_point5*4+grade_point6*4+grade_pointlab1*2+grade_pointlab2*2
        +grade_pointlab3*2+grade_pointlab4))
    tgp+=current
    print(current/31)
def sixth(grade_point1,grade_point2,grade_point3,grade_point4,grade_point5,grade_point6,
    grade_pointlab1,grade_pointlab2,grade_pointlab3,grade_pointlab4):
    global tcp
    global tgp
    tcp+=31
    current=((grade_point1*4+grade_point2*4+grade_point3*4+grade_point4*4
        +grade_point5*4+grade_point6*4+grade_pointlab1*2+grade_pointlab2*2
        +grade_pointlab3*2+grade_pointlab4))
    tgp+=current
    print(current/31)
def overall():
    ans=tgp/tcp
    print(ans)

    

first(A,A,A,A,A,A,A,A,A)

overall()
