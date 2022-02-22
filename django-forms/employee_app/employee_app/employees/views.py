from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django import forms

# Create your views here.
from employee_app.employees.models import Employee


def demo_view(request):
    ctx = {
        'employee_form': EmployeeForm()
    }
    # needs to be injected into context
    return render(request, 'demo.html', ctx)


def validate_positive(value):
    if value < 0:
        raise ValidationError('Value must be positive')


# definition of django bound form
class EmployeeForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=40)
    age = forms.IntegerField(
        required=False,
        widget=forms.TextInput(attrs={
            'type': 'range'
        }, ),
        validators=(
            # adding custom validation
            validate_positive,
        )
    )
    egn = forms.CharField(max_length=10)
    job_title = forms.ChoiceField(
        choices=((1, 'Software Developer'),
                 (2, 'QA Engineer'),
                 (3, 'DevOps Specialist'),
                 )
    )
    company = forms.ChoiceField(
        choices=((c, c) for c in Employee.COMPANIES))

    # we get more information in the request when we submit the form!


# model forms
class EmployeeFormTwo(forms.ModelForm):
    # second way of dealing with bots
    bot_catcher = forms.CharField(widget=forms.HiddenInput, required=False, )

    # only bot will fill hidden field
    def clean_bot_catcher(self):
        bot_catcher = self.cleaned_data['bot_catcher']
        if len(bot_catcher) > 0:
            raise ValidationError('Gotcha Bot!')
        return bot_catcher

    class Meta:
        model = Employee
        # fields=('first_name','last_name')
        fields = '__all__'
        # rewriting fields is done directly in meta
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control'}
            )
        }


def create_employee(request):
    # creates a form from data of the post request allowing us to validate
    # employee_form = EmployeeForm(request.POST)
    # if employee_form.is_valid():
    #     print('Valid')
    # else:
    #     print('Invalid')
    # standard get/post view

    # if request.method == 'GET':
    #     # get/show form
    #     context = {
    #         'employee_form': EmployeeForm()
    #     }
    #     return render(request, 'create.html', context)
    # else:
    #     # save info
    #     employee_form = EmployeeForm(request.POST)
    #     # isvalid divides data into cleaned and errors within the request object
    #     if employee_form.is_valid():
    #         return redirect('demo')
    #     context = {
    #         'employee_form': employee_form
    #     }
    #     # if an error occurs data remains and the errors are displayed as ul
    #     return render(request, 'create.html', context)
    # same as above but shorter
    if request.method == 'POST':
        employee_form = EmployeeFormTwo(request.POST,request.FILES)
        if employee_form.is_valid():
            # save to database
            # emp = Employee(
            #     first_name=employee_form.cleaned_data['first_name'],
            #     last_name=employee_form.cleaned_data['last_name'],
            #     job_title=employee_form.cleaned_data['job_title'],
            #     egn=employee_form.cleaned_data['egn'],
            #     company=employee_form.cleaned_data['company'],
            # )

            # with model forms this next line is redundant all you need to do is save
            emp = Employee(
                **employee_form.cleaned_data,
                department_id=1
            )
            emp.save()
            return redirect('demo')
    else:
        employee_form = EmployeeFormTwo()
    employee_order_form = EmployeeOrderForm(request.GET)
    employee_order_form.is_valid()
    order_by = employee_order_form.cleaned_data.get('order_by', 'first_name')
    context = {
        'employee_form': employee_form,
        'employees': Employee.objects.order_by(order_by).all(),
        'employee_order_form': employee_order_form,
    }
    return render(request, 'create.html', context)


class EmployeeOrderForm(forms.Form):
    order_by = forms.ChoiceField(
        choices=(('first_name', 'lastname'),
                 ('last_name', 'first_name'))
    )


def home(request):
    return (request, 'demo.html')


# we can use the same form for eddit as for create
def edit_employee(request, pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == 'POST':
        # the form will take values of request.POST and update employee
        employee_form = EmployeeFormTwo(request.POST,request.FILES, instance=employee)
        if employee_form.is_valid():
            employee_form.save()
            return redirect('create employee')
    # this automatically fills our form with required data
    else:
        employee_form = EmployeeFormTwo(instance=employee)
    ctx = {
        'employee': employee,
        'employee_form': employee_form,
    }
    return render(request, 'edit.html', ctx)


# making parts of the editform unalterable
# validation on modelforms are done with clean methods
class EditEmployeeForm(EmployeeFormTwo):

    def clean_egn(self):
        if self.egn.length < 10:
            raise ValidationError

    class Meta:
        widgets = {
            'egn': forms.TextInput(
                attrs={'readonly': 'readonly'},
            )
        }
# Bot Catchers - csrf token or hidden input field
# Media file configuration just like static files require settings setup