import pytest
from .models import Task

@pytest.mark.django_db
class TestTaskModel:

    def test_create_task(self):
        task = Task.objects.create(
            title='Learn pytest',
            priority='high',
            category='study'
        )

        assert task.title == 'Learn pytest'
        assert task.priority == 'high'

        assert task.complete is False
        assert task.category == 'study'

        assert Task.objects.count() == 1
    
    def test_task_string_representation(self):
        task = Task.objects.create(title='Buy milk')
        assert str(task) == 'Buy milk'
