from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from memos.models import Memo


def create_memo(title, content):
    return Memo.objects.create(title=title, content=content)


class MemoListTests(TestCase):
    def test_no_memos(self):
        response = self.client.get(reverse("memos:memo-list"))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context["memo_list"], [])

    def test_create_new_memo(self):
        test_memo = create_memo(
            title="test memo",
            content="This is the test memo."
        )
        response = self.client.get(reverse("memos:memo-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test memo")
        self.assertQuerysetEqual(response.context["memo_list"], [test_memo])