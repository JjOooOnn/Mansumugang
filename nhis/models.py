from django.db import models


class Question(models.Model):
	name = models.CharField(max_length=5)
	age = models.IntegerField()

# 일반 건강검진 - 이하 DB 직접 입력
class NormalChk(models.Model):
	n_age = models.IntegerField(default=0)
	n_chkitem = models.CharField(max_length=50, default='')

# 암 건강검진
class CancerChk(models.Model):
	c_age = models.IntegerField(default=0)
	c_type = models.CharField(max_length=15, default='')
	c_cycle = models.CharField(max_length=15, default='')

# 영유아 건강검진
class ChildChk(models.Model):
	ch_type = models.CharField(max_length=15, default='')
	ch_month = models.IntegerField(default=0)
	ch_item = models.CharField(max_length=50, default='')
	ch_method = models.CharField(max_length=50, default='')

# 장애인 급여비
class DisaFund(models.Model):
	d_type = models.CharField(max_length=15, default='')
	d_money = models.IntegerField(default=0)

# 출산양육비
class PragFund(models.Model):
	p_month = models.IntegerField(default=0)
	p_money = models.IntegerField(default=0)