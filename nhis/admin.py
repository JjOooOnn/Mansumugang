from django.contrib import admin
from .models import NormalChk, CancerChk, ChildChk, DisaFund, PragFund
# Register your models here.

admin.site.register(NormalChk)
admin.site.register(CancerChk)
admin.site.register(ChildChk)
admin.site.register(DisaFund)
admin.site.register(PragFund)
