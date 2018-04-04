from django.db import models

# Create your models here.
class user(models.Model):
    title=models.CharField(max_length=50) #职称
    name=models.CharField(max_length=50) #姓名

    password=models.CharField(max_length=50) #密码

    email = models.CharField(max_length=50) # 邮箱
    registration_type=models.CharField(max_length=50) #参会类型
    student_img_proof=models.CharField(max_length=50) # 学生证明
    company_name=models.CharField(max_length=50) # 单位名称
    phonenumber=models.CharField(max_length=50) # 电话号码
    address=models.CharField(max_length=50)#地址
    submitted=models.CharField(max_length=50)#是否投稿
    paper_id=models.CharField(max_length=50)#文章号
    paper_competition=models.CharField(max_length=50)#是否参与优秀论文评选
    pay_type=models.CharField(max_length=50)#支付方式
    invoice=models.CharField(max_length=50)#发票抬头
    tax_identification_number=models.CharField(max_length=50) #纳税人识别号
    invoice_img_proof=models.CharField(max_length=50) #发票证明

    payment = models.CharField(max_length=50)

