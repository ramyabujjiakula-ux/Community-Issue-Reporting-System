from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    name = models.CharField(max_length=100)
    contact_email = models.EmailField()

    def __str__(self):
        return self.name


class Issue(models.Model):

    CATEGORY_CHOICES = [
        ('road', 'Road'),
        ('education', 'Education'),
        ('water', 'Water'),
        ('health', 'Health'),
        ('other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('submitted', 'Submitted'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(upload_to='issues/', blank=True, null=True)

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    custom_category = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='submitted'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    submitted_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.title} ({self.status})"

    def get_category_display_name(self):
        if self.category == "other" and self.custom_category:
            return self.custom_category

        return dict(self.CATEGORY_CHOICES).get(
            self.category,
            self.category
        )
class Reply(models.Model):
    issue = models.ForeignKey(
        Issue,
        on_delete=models.CASCADE,
        related_name="replies"
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    is_admin_reply = models.BooleanField(default=True)

    def __str__(self):
        return f"Reply to {self.issue.title}"


    