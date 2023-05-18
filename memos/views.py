from django.shortcuts import get_object_or_404, render

from .models import Memo


def memo_list_view(request):
    memo_list = Memo.objects.all()
    context = {"memo_list": memo_list}
    return render(request, "memos/memo_list.html", context)


def memo_create_view(request):
    return render(request, "memos/memo_form.html")


def memo_edit_view(request, memo_id):
    memo = get_object_or_404(Memo, pk=memo_id)
    context = {"memo": memo}
    return render(request, "memos/memo_form.html", context)


def memo_delete_view(request, memo_id):
    memo = get_object_or_404(Memo, pk=memo_id)
    context = {"memo": memo}
    return render(request, "memos/memo_confirm_delete.html", context)

