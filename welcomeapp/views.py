from django.shortcuts import render

# Create your views here.
def message(request):
    if request.GET:
        name = request.GET.get('username')
        return render(request,'result.html',{
            'username': name,
            'data': request.GET
            })
    return render(request,'index.html')