from django.shortcuts import render,redirect
from django.http import HttpResponse
from Emp_Info.models import Employee

def home(request):
    return HttpResponse("This is my first Django!...")

def disp(request):
    return render(request, 'index.html')

def calculator(request):
    result = 0
    try:
        num1 = int(request.GET.get("num1"))
        num2 = int(request.GET.get("num2"))
        opr = request.GET.get("opr")

        if opr == "+":
            result = num1 + num2
        elif opr == "-":
            result = num1 - num2
        elif opr == "*":
            result = num1 * num2
        elif opr == "/":
            result = num1 / num2
        elif opr == "**":
            result = num1 ** num2
        elif opr == "%":
            result = num1 % num2
        else:
            result = "Invalid operator"

    except Exception as e:
        result = f"Error: {e}"

    return render(request, 'calculator.html', {"sum": result})


def employee(request):
    try:
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']

        e = Employee(name=name, email=email, phone=phone, address=address)
        e.save()

    except Exception as e:
        print(e)
        
    return render(request, 'employee.html')


def ems(request):
    emp = Employee.objects.all()

    data = {
        'emp':emp
    }


    return render(request, 'EMS.html',data)


def addemployee(request):
    try:
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']

        e = Employee(name=name, email=email, phone=phone, address=address)
        e.save()

        return redirect("/ems/")
    
    except Exception as e:
        print(e)



def updateEmp(request,id):
    try:
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']

        e = Employee(id=id, name=name, email=email, phone=phone, address=address)
        e.save()
        
        return redirect("/ems/")
    
    
    except Exception as e:
        print(e)
        


def delete(request,id):
    Employee.objects.filter(id=id).delete()
    
    return redirect("/ems/")