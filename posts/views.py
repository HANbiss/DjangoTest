from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views import generic
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm


class IndexView(generic.ListView):
    def get_queryset(self):
        return Question.objects.order_by('-create_date')


class DetailView(generic.DetailView):
    model = Question

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('posts:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'posts/question_detail.html', context)

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('posts:list')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'posts/question_form.html', {'form': form})