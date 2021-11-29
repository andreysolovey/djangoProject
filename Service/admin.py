from django.contrib import admin
from Service.models import Pay
import csv
from django.http import HttpResponse
import datetime


def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)
    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    writer.writerow([field.verbose_name for field in fields])
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response
export_to_csv.short_description = 'Export to CSV'


class PostAdmin(admin.ModelAdmin):
    list_display = ('bank_account', 'card_number', 'date')
    list_filter = ('bank_account', 'date', 'amount_to_pay')
    actions = [export_to_csv]


admin.site.register(Pay, PostAdmin)
