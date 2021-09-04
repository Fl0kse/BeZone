from django.test import TestCase
from django.contrib.auth.models import User
from Counter.util import get_count, check_counter, add_count, remove_count


class CounterCase(TestCase):
    def test_counter_get(self):
        user = 'myuser'
        res = get_count(user)
        user = User.objects.filter(username=user).first()
        counter = check_counter(user)
        self.assertEqual(res, counter.counter)

    def test_counter_get_new(self):
        user = 'kek'
        res = get_count(user)
        user = User.objects.filter(username=user).first()
        counter = check_counter(user)
        self.assertEqual(res, counter.counter)

    def test_counter_post(self):
        user = 'myuser'
        res = add_count(user)
        user = User.objects.filter(username=user).first()
        counter = check_counter(user)
        counter.counter += 1
        counter.save()
        counter = check_counter(user)
        self.assertEqual(res, counter.counter)

    def test_counter_post_new(self):
        user = 'kek'
        res = add_count(user)
        user = User.objects.filter(username=user).first()
        counter = check_counter(user)
        counter.counter += 1
        counter.save()
        counter = check_counter(user)
        self.assertEqual(res, counter.counter)

    def test_counter_delete(self):
        user = 'myuser'
        res = remove_count(user)
        user = User.objects.filter(username=user).first()
        counter = check_counter(user)
        counter.counter -= 1
        counter.save()
        counter = check_counter(user)
        self.assertEqual(res, counter.counter)

    def test_counter_delete_new(self):
        user = 'kek'
        res = remove_count(user)
        user = User.objects.filter(username=user).first()
        counter = check_counter(user)
        counter.counter -= 1
        counter.save()
        counter = check_counter(user)
        self.assertEqual(res, counter.counter)
