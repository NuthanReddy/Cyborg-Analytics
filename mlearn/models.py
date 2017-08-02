from django.contrib.auth.models import Permission, User
from django.db import models


class Dataset(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    data_file = models.FileField(default='')
    file_path = models.CharField(max_length=500)
    file_name = models.CharField(max_length=250)
    file_type = models.CharField(max_length=50)

    def __str__(self):
        return self.file_name


class DataInfo(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    fname = models.CharField(max_length=250)
    fsize = models.IntegerField
    ftype = models.CharField(max_length=50)
    fields = models.CharField(max_length=1000)
    num_fields = models.CharField(max_length=500)
    tex_fields = models.CharField(max_length=500)
    predict_fields = models.CharField(max_length=500)
    use_fields = models.CharField(max_length=1000)

    def __str__(self):
        return self.fname

