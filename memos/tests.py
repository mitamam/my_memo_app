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


class MemoCreateTests(TestCase):
    def test_empty_input_field(self):
        data = {
            "title": "",
            "content": "This is the test memo.",
            "created_at": timezone.now()
        }
        response = self.client.post(reverse("memos:memo-create"), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "正しい値を入力してください")

    def test_incorrect_date_time(self):
        data = {
            "title": "test memo",
            "content": "This is the test memo.",
            "created_at": "Incorrect date"
        }
        response = self.client.post(reverse("memos:memo-create"), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "正しい値を入力してください")

    def test_title_is_more_than_max_length(self):
        data = {
            # 101 characters
            "title": "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabc"\
            "defghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvw",
            "content": "This is the test memo.",
            "created_at": timezone.now()
        }
        response = self.client.post(reverse("memos:memo-create"), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "正しい値を入力してください")

    def test_correct_values(self):
        data = {
            "title": "test memo",
            "content": "This is the test memo.",
            "created_at": timezone.now()
        }
        response = self.client.post(reverse("memos:memo-create"), data)
        memo = Memo.objects.get(title="test memo")
        self.assertEqual(response.status_code, 302)


class MemoEditTests(TestCase):
    def test_empty_input_field(self):
        test_memo = create_memo(
            title="test memo",
            content="This is the test memo."
        )
        data = {
            "title": "",
            "content": test_memo.content,
            "created_at": test_memo.created_at
        }
        response = self.client.post(
            reverse("memos:memo-edit", args=(test_memo.id,)),
            data
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "正しい値を入力してください")

    def test_incorrect_date_time(self):
        test_memo = create_memo(
            title="test memo",
            content="This is the test memo."
        )
        data = {
            "title": test_memo.title,
            "content": test_memo.content,
            "created_at": "Incorrect date"
        }
        response = self.client.post(
            reverse("memos:memo-edit", args=(test_memo.id,)),
            data
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "正しい値を入力してください")

    def test_title_is_more_than_max_length(self):
        test_memo = create_memo(
            title="test memo",
            content="This is the test memo."
        )
        data = {
            # 101 characters
            "title": "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabc"\
            "defghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvw",
            "content": test_memo.content,
            "created_at": test_memo.created_at
        }
        response = self.client.post(
            reverse("memos:memo-edit", args=(test_memo.id,)),
            data
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "正しい値を入力してください")

    def test_correct_values(self):
        test_memo = create_memo(
            title="test memo",
            content="This is the test memo."
        )
        data = {
            "title": "edited memo",
            "content": test_memo.content,
            "created_at": test_memo.created_at
        }
        response = self.client.post(
            reverse("memos:memo-edit", args=(test_memo.id,)),
            data
        )
        memo = Memo.objects.get(title="edited memo")
        self.assertEqual(response.status_code, 302)