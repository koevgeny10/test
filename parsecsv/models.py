from django.db import models


class CSVFile(models.Model):
    file = models.FileField(upload_to='csv/%Y/%m/%d/')
    moment = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Удаляю файл перед сохранением нового потому что он в этом задании всего 1.
        # Что бы было 3 строки в таблице со строками
        try:
            old = CSVFile.objects.latest('file')
            old.delete()
        except self.DoesNotExist:
            pass

        # Паршу csv по строкам
        super().save(*args, **kwargs)
        with self.file.open(mode='r') as f:
            for i in f.readlines():
                ParsedCSV.objects.create(file=self, string=i)


class ParsedCSV(models.Model):
    file = models.ForeignKey(CSVFile, on_delete=models.CASCADE, related_name='strings', related_query_name='string')
    string = models.CharField(max_length=200)
