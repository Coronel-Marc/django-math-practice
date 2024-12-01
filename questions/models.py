from django.db import models

class Question(models.Model):
    question_text = models.TextField()
    correct_answer = models.CharField(max_length=1)  # Ex.: "A", "B", etc.
    explanation = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.question_text

class UserResponse(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    chosen_answer = models.CharField(max_length=1)
    is_correct = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)
