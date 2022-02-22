
from django.contrib import admin


from .models import Hero, Works, Category, OurAvesome, DescriptionOur, WhoAreWe, OurProc, OurTeam, Button, Feedback, GetInTuch, CompanyData


class HeroAdmin(admin.ModelAdmin):
    list_display = ('top', 'bottom', 'is_active')
    list_display_links = ('top', 'bottom')
    list_filter = ('is_active',)       
    

admin.site.register(Hero,HeroAdmin)
# Register your models here.

class WorksAdmin(admin.ModelAdmin):
    list_display = ('cetegory', 'name_work', 'is_active')
    list_display_links = ('cetegory', 'name_work')
    list_filter = ('is_active',)
admin.site.register(Works,WorksAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('namee',)
    list_display_links = ('namee', )
    
admin.site.register(Category,CategoryAdmin)

class OurAdmin(admin.ModelAdmin):
    list_display = ('textt','textt2')
    list_display_links = ('textt', )
admin.site.register(OurAvesome,OurAdmin)

class DescriptionAdmin(admin.ModelAdmin):
    list_display = ('category', 'text','is_active')
    list_display_links = ('text', )
    list_filter = ('is_active',)
admin.site.register(DescriptionOur,DescriptionAdmin)

class WhoAreWeAdmin(admin.ModelAdmin):
    list_display = ('who_are', 'description_who')
    list_display_link = ('who_are')
admin.site.register(WhoAreWe,WhoAreWeAdmin)

class OurProcAdmin(admin.ModelAdmin):
    list_display = ('text1', 'text2')
    list_display_link = ('text1')
admin.site.register(OurProc,OurProcAdmin)


class OurTeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'position','is_active')
    list_display_link = ('name')
admin.site.register(OurTeam,OurTeamAdmin)

class ButtonAdmin(admin.ModelAdmin):
    list_display = ('text', 'button','is_active')
    list_display_link = ('text')
    list_filter = ('is_active',)
admin.site.register(Button,ButtonAdmin)

class FreedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_active')
    list_display_link = ('name')
admin.site.register(Feedback,FreedbackAdmin)

class GetInAdmin(admin.ModelAdmin):
    list_display = ('contactName','contactEmail','date')
    list_display_link = ('contactName')
    search_fields = ('contactName', 'contactMessage',) 
admin.site.register(GetInTuch,GetInAdmin)

class CompanyDataAdmin(admin.ModelAdmin):
    list_display = ('num',)
    list_display_link = ('num')
admin.site.register(CompanyData,CompanyDataAdmin)