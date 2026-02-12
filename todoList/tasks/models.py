from django.db import models

class Task(models.Model):

    category_choices = [
        ('work', 'Work'),
        ('study', 'Study'),
        ('personal', 'Personal'),
        ('health', 'Health'),
        ('finance', 'Finance'),
        ('other', 'Other'),
    ]

    priority_choices = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(
        max_length=10,
        choices=priority_choices,
        default='medium',
        verbose_name='Task Priority'
    )

    category = models.CharField(
        max_length=20,
        choices=category_choices,
        default='personal',
        verbose_name='Category'
    )
    

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete', '-created_at']


class TaskHistory(models.Model):
    ACTION_CHOICES = [
        ('created', 'Created'),
        ('completed', 'Completed'),
        ('uncompleted', 'Uncompleted'),
        ('deleted', 'Deleted'),
    ]

    task_title = models.CharField(max_length=200)
    action = models.CharField(max_length=20, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action}: {self.task_title}"

    class Meta:
        ordering = ['-timestamp']