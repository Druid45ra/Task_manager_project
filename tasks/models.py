from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)  # Titlu sarcină
    description = models.TextField(blank=True, null=True)  # Descriere
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed')],
        default='pending',
    )  # Status
    due_date = models.DateField(blank=True, null=True)  # Termen limită
    created_at = models.DateTimeField(auto_now_add=True)  # Data creării
    updated_at = models.DateTimeField(auto_now=True)  # Data actualizării

    def __str__(self):
        return self.title
