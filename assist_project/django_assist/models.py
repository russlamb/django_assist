from django.db import models


# Create your models here.

class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-
    updating ``created`` and ``modified`` fields.
    """
    created = models.DateTimeField('CreatedOn',auto_now_add=True)
    modified = models.DateTimeField('ModifiedOn',auto_now=True)

    class Meta:
        abstract = True


class Project(TimeStampedModel):
    project_name = models.CharField(max_length=500)
    def __str__(self):
        return ("Project {}".format(self.project_name))

class StepStatus(models.Model):
    status_name = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return "StepStatus: {}".format(self.status_name)

class Step(TimeStampedModel):
    step_name = models.CharField(max_length=200)
    status = models.CharField(max_length=20,default="")
    step_order = models.IntegerField(default=1)

    def __str__(self):
        return ("Step {} [{}]".format(self.step_name,self.status))


class Command(TimeStampedModel):
    step = models.ForeignKey(Step, on_delete=models.CASCADE)
    command_text = models.CharField(max_length=1000)
    output_text = models.TextField(default="")
    def __str__(self):
        return ("Command {}".format(self.command_text))

class CommandOutput(TimeStampedModel):
    command = models.ForeignKey(Command, on_delete=models.CASCADE)
    output_text = models.TextField()
    def __str__(self):
        return ("Output {}".format(self.output_text))
