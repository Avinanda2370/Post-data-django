from django.shortcuts import render
from post.models import StudentData

# Create your views here.
def hi(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        email = request.POST['email']
        try:
            StudentData.objects.create(
                name = name,
                age = age,
                email = email
            )
            return render(request,'post/index.html')
        except:

            context={
                "msg":"Input all field correctly"
            }
            if age =="":
                context={
                "msg": "Your age field is empty"
            }

            return render(request, 'post/Error.html',context)
    else:
        return render(request, 'post/index.html')

