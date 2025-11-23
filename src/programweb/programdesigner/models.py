from django.db import models


class Speaker(models.Model):
    name = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200, blank=True)

    def __str__(self):
    	return self.name


class Talk(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(default="", blank=True)
    updated_at = models.DateTimeField(auto_now=True, help_text="date last updated")
    speakers = models.ManyToManyField(Speaker)

    def __str__(self):
    	return f"{self.title} ({", ".join(str(speaker) for speaker in self.speakers.all())})"


class Event(models.Model):
	name = models.CharField(max_length=200, unique=True)
	venue = models.CharField(max_length=200)
	start = models.DateTimeField()
	end = models.DateTimeField()

	def __str__(self):
		return f"{self.name}"


class Program(models.Model):
	day = models.PositiveIntegerField(default=1)
	event = models.ForeignKey(Event, on_delete=models.CASCADE)
	talks = models.ManyToManyField(Talk, through='ProgramTalk')

	def __str__(self):
		if self.event.name == "Konsoll":
			return f"{self.event} Day {self.day} (@{self.event.venue})"
		else:
			return f"{self.event} (@{self.event.venue})"

	class Meta:
		unique_together = ('event', 'day')


class ProgramTalk(models.Model):
	program = models.ForeignKey(Program, on_delete=models.CASCADE)
	talk = models.ForeignKey(Talk, on_delete=models.CASCADE)
	start_time = models.TimeField()
	end_time = models.TimeField()

	class Meta:
		ordering = ['start_time']
		unique_together = ('talk', 'program')

	def __str__(self):
		return f"{self.start_time.strftime('%H:%M')} -  {self.talk}"

