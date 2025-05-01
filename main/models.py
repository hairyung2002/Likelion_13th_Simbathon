from django.db import models

#계정 정보를 저장할 데이터 테이블 Member
class Member(models.Model):
    id = models.CharField(max_length=12, primary_key=True)
    password = models.CharField(max_length=12)
    name = models.CharField(max_length=5)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.id 