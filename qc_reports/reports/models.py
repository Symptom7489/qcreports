from django.db import models


class JMF(models.Model):
    mix_type = models.CharField(max_length= 50, choices = [
        ('L1 WC', 'Level 1 Wearing Course'),
        ('L1 BC', 'Level 1 Binder Course'),
        ('L1 Base', 'Level 1 Base Course'),
        ('L2 WC', 'Level 2 Wearing Course'),
        ('L2 BC', 'Level 2 Binder Course'),
        ('L2F WC', 'Level 2F Wearing Course'),
        ('SMA', 'Stone Matrix Asphalt'),
        ('Dense', 'Dense Graded Asphalt'),
        ('OGFC', 'Open-Graded Friction Course'),
    ], default='L1 WC')
    mix_size = models.CharField(max_length=50, choices= [
        ('3/8', '3/8 inch mixture'),
        ('1/2', '1/2 inch mixture'),
        ('3/4', '3/4 inch mixture'),
        ('1', '1 inch mixture'),
    ], default='1/2')
    jmf_number = models.CharField(max_length=20)
    gmm = models.CharField(max_length= 10)
    gauge_density = models.CharField(max_length=10)
    project_name = models.ManyToManyField('Project', blank=True)
    pdf = models.FileField(upload_to='uploads/', blank=True)

    def __str__(self):
        return self.jmf_number + ' ' + self.mix_size + ' ' + self.mix_type


class Project(models.Model):
    barber_number = models.CharField(max_length=10)
    state_number = models.CharField(max_length=15)
    project_name = models.CharField(max_length=50)
    jmfs = models.ManyToManyField(JMF, blank=True)

    def __str__(self):
        return self.project_name + ' -- ' + self.barber_number


class CoreReadings(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    jmf = models.ForeignKey(JMF, on_delete=models.CASCADE)
    job_type = models.CharField(max_length=10, choices=[
        ('DOTD', 'LA DOTD'),
        ('Barber', 'Barber Brothers - Non DOTD Project')
    ], default='DOTD')
    core_type = models.CharField(max_length=10, choices=[
        ('DOTD', 'LA DOTD'),
        ('Check', 'Check Core')
    ], default='DOTD')
    core_lot = models.CharField(max_length=60, null=True)
    core_id = models.CharField(max_length=30)
    core_location = models.CharField(max_length=30)
    lane_direction = models.CharField(max_length=30, choices=[
        ('N','North'),('S','South'),('E','East'),('W','West')
    ],default= 'N')
    gauge_reading_1 = models.CharField(max_length=10, blank=True)
    gauge_reading_2 = models.CharField(max_length=10, blank=True)
    gauge_reading_3 = models.CharField(max_length=10, blank=True)
    gauge_reading_4 = models.CharField(max_length=10, blank=True)
    gauge_reading_5 = models.CharField(max_length=10, blank=True)
    gauge_reading_average = models.CharField(max_length=10)
    date_time = models.DateField()

    def __str__(self):
        return self.project.project_name + ' - ' + self.project.state_number + ' - Core ' + self.core_id



class QCReport(models.Model):
    project = models.ManyToManyField(Project)
    jmf = models.ManyToManyField(JMF)
    readings = models.ManyToManyField(CoreReadings)
    notes = models.TextField(null=True, blank=True)
    report_date = models.DateField(auto_now=False)



class NightlyReadings(models.Model):
    project = models.ManyToManyField(Project)
    jmf = models.ManyToManyField(JMF)
    nightly_readings = models.CharField(max_length=20, blank=True)
    date = models.DateField(auto_now=False, null=True)

class NRSetup(models.Model):
    jmf = models.CharField(max_length=12,null=True)
    project = models.CharField(max_length=30, null=True)
    numberOfEntries = models.IntegerField()
    date = models.DateField(auto_now=False, null=True)