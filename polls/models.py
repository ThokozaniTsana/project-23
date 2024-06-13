from django.db import models

# Create your models here.
class Question(models.Model):
    """A class representing questions for voters."""

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """A method for questions, and it returns the questions-text."""
        return self.question_text

class Choice(models.Model):
   """A Class to represent the user's choice of answers to the questions."""

   question = models.ForeignKey(Question, on_delete=models.CASCADE)
   choice_text = models.CharField(max_length=200)
   votes = models.IntegerField(default=0)

   def __str__(self):
        """A method of class choices which returns the choice-text."""
        return self.choice_text