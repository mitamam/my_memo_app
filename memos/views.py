from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Memo
from .forms import MemoForm


def memo_list_view(request):
    memo_list = Memo.objects.all()
    context = {"memo_list": memo_list}
    return render(request, "memos/memo_list.html", context)


def memo_create_view(request):
    context = {"memo": None}
    return render(request, "memos/memo_form.html", context)


def memo_edit_view(request, memo_id):
    if request.method == "POST":
        form = MemoForm(request.POST)
        memo = get_object_or_404(Memo, pk=memo_id)
        if form.is_valid():
            memo.title = form.cleaned_data["title"]
            memo.content = form.cleaned_data["content"]
            memo.created_at = form.cleaned_data["created_at"]
            memo.save()
            return HttpResponseRedirect(reverse("memos:memo-list"))
        else:
            return render(
                request,
                "memos/memo_form.html",
                {"memo": memo, "error_message:": "Incorrect Input!"},
            )
    else:
        memo = get_object_or_404(Memo, pk=memo_id)
        initial_data = {'title': memo.title, 'content': memo.content, 'created_at': memo.created_at}
        form = MemoForm(initial=initial_data)
        context = {"memo": memo, "form": form}
        return render(request, "memos/memo_form.html", context)


def memo_delete_view(request, memo_id):
    memo = get_object_or_404(Memo, pk=memo_id)
    context = {"memo": memo}
    return render(request, "memos/memo_confirm_delete.html", context)
