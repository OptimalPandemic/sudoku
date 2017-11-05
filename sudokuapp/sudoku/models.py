from django.db import models
import json

# Create your models here.


class Puzzle(models.Model):
    data = models.CharField(max_length=81)

    def get_data(self):
        return json.loads(self.data)

    def set_data(self, d):
        self.data = json.dumps(d)
