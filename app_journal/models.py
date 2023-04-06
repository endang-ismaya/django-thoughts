from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class Review(models.Model):
    reviewer_name = models.CharField(max_length=65)
    review_title = models.CharField(max_length=100)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="review_task")

    def __str__(self) -> str:
        return self.review_title
