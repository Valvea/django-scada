from django.db import models


class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField (max_length=250)
    start = models.DateTimeField()
    end = models.DateTimeField()
    progress = models.IntegerField()
    dependencies =  models.CharField(max_length=50)
    custom_class =  models.CharField(max_length=50)

    def save_tasks(self,tasks):
        tasks_to_db=list(map( lambda x: self(id=x['id'],
                                name=x['name'],
                                start=x['start'],
                                end=x['end'],
                                progress=x['tasks']['progress'],
                                dependencies=x['dependencies'],
                                custom_class=x['custom_class']

        )  ,tasks))
        self.objects.bulk_create(tasks_to_db)
        

