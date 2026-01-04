from django.db import models

class Todo(models.Model):
    PRIORITY_CHOICES = (
        (1, "Past"),
        (2, "O'rtacha"),
        (3, "Yuqori"),
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=1)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title
