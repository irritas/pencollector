from django.db import models
from django.urls import reverse
from datetime import date

COLORS = (
	('K', 'Black'),
    ('R', 'Red'),
    ('G', 'Green'),
    ('B', 'Blue')
)

class Ink(models.Model):
	name = models.CharField(max_length=50)
	color = models.CharField(
		max_length=1,
		choices=COLORS,
    	default=COLORS[0][0]
	)
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('inks_detail', kwargs={'pk': self.id})

class Pen(models.Model):
	name = models.CharField(max_length=100)
	brand = models.CharField(max_length=100)
	style = models.CharField(max_length=100)
	features = models.TextField(max_length=250)
	inks = models.ManyToManyField(Ink)
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('detail', kwargs={'pen_id': self.id})
	def refill_for_year(self):
		if not self.refill_set.first():
			return False
		if self.refill_set.first().date.year == date.today().year:
			return True
		return False

class Refill(models.Model):
	date = models.DateField()
	color = models.CharField(
		max_length=1,
		choices=COLORS,
    	default=COLORS[0][0]
	)
	pen = models.ForeignKey(Pen, on_delete=models.CASCADE)
	def __str__(self):
		return f"{self.get_color_display()} ink on {self.date}"
	class Meta:
		ordering = ['-date']