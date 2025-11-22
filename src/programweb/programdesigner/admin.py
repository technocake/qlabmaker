from django.contrib import admin

# Register your models here.

from .models import Speaker, Talk, Program, Event, ProgramTalk
from .forms import ProgramTalkAdminForm

class SpeakerInline(admin.TabularInline):
	verbose_name = "Speaker"
	verbose_name_plural = "Speakers"
	model = Talk.speakers.through
	extra = 1

class TalkInline(admin.TabularInline):
	fields = ('start_time', 'end_time', 'talk', 'program')
	form = ProgramTalkAdminForm
	verbose_name = "Talk"
	verbose_name_plural = "Talks"
	model = Program.talks.through
	extra = 5


class TalkAdmin(admin.ModelAdmin):
	exclude = ('updated_at', "speakers") # Replace 'field_to_hide' with the actual field name
	inlines = [SpeakerInline]
	list_display = ('title', 'speakers_as_str')

	def speakers_as_str(self, obj):
		speakers = obj.speakers.all()
		return ", ".join([str(speaker) for speaker in speakers])

	speakers_as_str.short_description = "Speakers"


class EventAdmin(admin.ModelAdmin):
	pass

class ProgramAdmin(admin.ModelAdmin):
	inlines = [TalkInline]

class ProgramTalkAdmin(admin.ModelAdmin):
	list_display = ('start_time', 'end_time', 'talk', 'program')
	form = ProgramTalkAdminForm

	def start_time_display(self, obj):
		return obj.start_time.strftime("%H:%M")
	start_time_display.short_description = "Start Time"

	def end_time_display(self, obj):
		return obj.end_time.strftime("%H:%M")
	start_time_display.short_description = "End Time"

admin.site.register(Speaker)
admin.site.register(Talk, TalkAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Program, ProgramAdmin)
#admin.site.register(ProgramTalk, ProgramTalkAdmin)
