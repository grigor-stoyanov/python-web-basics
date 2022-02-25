from django.shortcuts import render, redirect

from ExpensesTracker.main.forms import ProfileForm, ExpenseForm, DeleteExpenseForm, DeleteProfileForm
from ExpensesTracker.main.models import Profile, Expense


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def form_action(request, form_class, success_url, instance, template_name, ctx):
    if request.method == 'POST':
        form = form_class(data=request.POST, files=request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = form_class(instance=instance)
    ctx.update({
        'instance': instance,
        'form': form
    })
    return render(request, template_name, ctx)


# Create your views here.
def home_view(request):
    profile = get_profile()
    ctx = {
        'user': profile,
        'is_hidden': True if not profile else False
    }
    if profile:
        ctx.update(
            {
                'expenses': Expense.objects.all()
            }
        )
        return render(request, 'home-with-profile.html', ctx)
    return form_action(request, ProfileForm, 'main:home', None, 'home-no-profile.html', ctx)


def create_expense_view(request):
    ctx = {}
    return form_action(request, ExpenseForm, 'main:home', None, 'expense-create.html', ctx)


def edit_expense_view(request, pk):
    ctx = {
        'pk': pk,
    }
    return form_action(request, ExpenseForm, 'main:home', Expense.objects.get(pk=pk), 'expense-edit.html', ctx)


def delete_expense_view(request, pk):
    ctx = {
        'pk': pk
    }
    return form_action(request, DeleteExpenseForm, 'main:home', Expense.objects.get(pk=pk), 'expense-delete.html', ctx)


def profile_view(request):
    profile = get_profile()
    ctx = {
        'profile': profile,
    }
    return render(request, 'profile.html', ctx)


def delete_profile_view(request):
    ctx = {}
    return form_action(request, DeleteProfileForm, 'main:home', get_profile(), 'profile-delete.html', ctx)


def edit_profile_view(request):
    ctx = {}
    return form_action(request, ProfileForm, 'main:profile', get_profile(), 'profile-edit.html', ctx)
