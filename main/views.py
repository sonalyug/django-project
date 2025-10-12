from django.shortcuts import render, redirect
from .forms import ContactForm, CalculatorForm

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def courses(request):
    return render(request, 'main/courses.html')

def contact(request):
    submitted = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            submitted = True
            form = ContactForm()  # Reset form
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {"form": form, "submitted": submitted})

def calculator(request):
    result = None
    error = ""
    if request.method == "POST":
        form = CalculatorForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            op = form.cleaned_data['operation']
            try:
                if op == 'add':
                    result = num1 + num2
                elif op == 'sub':
                    result = num1 - num2
                elif op == 'mul':
                    result = num1 * num2
                elif op == 'div':
                    if num2 != 0:
                        result = num1 / num2
                    else:
                        error = "Cannot divide by zero"
            except Exception as exc:
                error = str(exc)
        else:
            error = "Invalid input"
    else:
        form = CalculatorForm()
    return render(request, 'main/calculator.html', {"form": form, "result": result, "error": error})
