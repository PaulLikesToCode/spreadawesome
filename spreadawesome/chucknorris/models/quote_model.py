from django.db import models

class Quote(models.Model):
	quote_text = models.TextField()

	class Meta:
		app_label = "chucknorris"