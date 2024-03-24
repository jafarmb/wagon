from django.http import request
from django.shortcuts import render, redirect
from todoapp.models import Task
from.forms import TodoForm


# Create your views here.
def add(request):
    pqr = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date','')
        xyz = Task(name=name, priority=priority,date=date)
        xyz.save()
    return render(request, 'home.html', {'pqr': pqr})


#     return render(request,'detail.html',)
def delete(request, taskid):
# def details(request):
#
    mno = Task.objects.get(id=taskid)
    if request.method == 'POST':
        mno.delete()
        return redirect('/')
    return render(request, 'delete.html')

def update(request,id):
    lmn=Task.objects.get(id=id)
    f=TodoForm(request.POST or None,instance=lmn)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'lmn':lmn,'f':f})

