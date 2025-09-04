# Create your models here.
from django.db import models

# BaseModel to be inherited by other models
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # This model won’t create a table itself

# College model
class Priority(BaseModel):
    name = models.CharField(max_length=150)
    class Meta:
        verbose_name = "Priority"
        verbose_name_plural = "Priorities"

    def __str__(self):
        return self.name

# Organization model
class Category(BaseModel):
    name = models.CharField(max_length=250)
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"  

    def __str__(self):
        return self.name

# Program model
class Task(BaseModel):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=1000)
    deadline = models.DateField()
    status = models.CharField(
        max_length=50,
        choices=[
            ("Pending", "Pending"),
            ("In Progress", "In Progress"),
            ("Completed", "Completed"),
        ],
        default="Pending"
    )
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# Student model
class Note(BaseModel):
    task = models.CharField(max_length=15)
    content = models.CharField(max_length=25)
    
    def __str__(self):
        return f"{self.task}, {self.content}"

# OrgMember model
class SubTask(BaseModel):
    parent_task = models.ForeignKey(Task, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    status = models.CharField(
        max_length=50,
        choices=[
            ("Pending", "Pending"),
            ("In Progress", "In Progress"),
            ("Completed", "Completed"),
        ],
        default="Pending"
    )
