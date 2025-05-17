from django.contrib import admin
from .models import Groups, Worker, Product, WorkerProduct, DailyProduction

class GroupsAdmin(admin.ModelAdmin):
    list_display = ('name', 'worker_count')

    def worker_count(self, obj):
        return obj.workers.count()
    worker_count.short_description = 'Number of Workers'

admin.site.register(Groups, GroupsAdmin)
admin.site.register(Worker)
admin.site.register(Product)
admin.site.register(WorkerProduct)
admin.site.register(DailyProduction)
