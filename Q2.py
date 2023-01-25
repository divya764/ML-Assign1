dog = {'name':'Tommy','color':'white','breed':'husky','legs':'4','age':'2'}
print ("Dog Dictionary Created:",dog)
student = {'first_name':'Srujana','last_name':'Makutam','Gender':'Female','age':'22','marital_status':'si ngle',
'skills':'dancer','Country':'India','City':'Hyderabad','Address':'1/180'}
print ("Student Dictionary Created:",student)
skills = {'dancer':'1','singer':'2','coder':'3'}
print ("Skills Dictionary Created:",skills)
print ("Length of student:", len(student))
print ("Datatype fo skills:",type(skills))
print ("Values of skills:",skills.values())
skills['artist'] = 4
print ("New skill added:",skills)
print ("Dog keys:",dog.keys())
print ("Student values:",student.values())