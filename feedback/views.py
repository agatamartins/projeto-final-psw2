from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from usuarios.models import Usuario

from .forms import FeedbackForm
from .models import Feedback


@login_required
def feedback_list(request):
    feedbacks = Feedback.objects.select_related('usuario')

    return render(
        request,
        'feedback/feedback_list.html',
        {
            'feedbacks': feedbacks,
        }
    )


@login_required
def feedback_create(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            usuario = get_object_or_404(
                Usuario,
                pk=request.user.pk
            )

            feedback = form.save(commit=False)
            feedback.usuario = usuario
            feedback.save()

            messages.success(
                request,
                'Sua opinião foi enviada com sucesso!'
            )

            return redirect('feedback:feedback_list')
    else:
        form = FeedbackForm()

    return render(
        request,
        'feedback/feedback_form.html',
        {
            'form': form,
        }
    )
