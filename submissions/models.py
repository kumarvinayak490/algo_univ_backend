from django.db import models


class CodeSubmission(models.Model):
    LANGUAGE_CHOICES = [
        ('cpp', 'C++'),
        ('python', 'Python'),
        ('java', 'Java'),
    ]

    code = models.TextField()
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)
    submitted_at = models.DateTimeField(auto_now_add=True)
    verdict = models.CharField(max_length=20, null=True, blank=True)
    output = models.TextField(null=True, blank=True)
    # user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return f"Code submitted  {self.code}"
