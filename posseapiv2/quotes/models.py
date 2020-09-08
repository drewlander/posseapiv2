from django.db import models

class PosseQuote(models.Model):
    quote = models.TextField()
    dateadded = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.quote

