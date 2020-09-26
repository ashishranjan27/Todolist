from django.shortcuts import render,HttpResponse
from home.models import Task
# Create your views here.
def home(request):
    # return HttpResponse('works')
    context={'success':False , 'name':'ASHISH'}
    if request.method=="POST":
        title=request.POST['title']
        desc=request.POST['desc']
        print(title,desc)
        ins=Task(taskTitle=title,taskDesc=desc)
        ins.save()
        context={'success':True, 'name':'Ashish'}

    return render(request, 'index.html',context)

def tasks(request):
    # In below one task is from model or database and fetch all detail from there only
    alltask= Task.objects.all()  
    # print(alltask)
    # for item in alltask:
    #     print(item.taskTitle)
    #     print(item.taskDesc)
       
    context={'tasks':alltask}
    return render(request,'tasks.html',context)

