from django.shortcuts import render # type: ignore

# Create your views here.
def employee_list(request):
    return render(request, "pages/employee_list.html")
