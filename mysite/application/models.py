from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib import admin
# Create your models here.

class ScriptCodeStatus(models.Model):
    status_id = models.CharField(max_length=200)
    status_name = models.CharField(max_length=200)

    def publish(self):
        self.save()

    def __int__(self):
        return self.status_id
    
    class Meta:
        db_table = "scripts_code_status"

class Testbed(models.Model):
    tb_id = models.IntegerField(unique=True)
    tb_name = models.CharField(max_length=200)
    tb_platform = models.CharField(max_length=200)
    tb_status = models.CharField(max_length=200)
    tb_status_reservation_id = models.CharField(max_length=200)
    tb_status_reservation_time =  models.DateTimeField(auto_now_add=True, blank=True)
    tb_topology_base = models.CharField(max_length=200)
    tb_topology_cli = models.CharField(max_length=200)
    tb_topology_diagram = models.CharField(max_length=200)
    tb_status_comments = models.CharField(max_length=200)
    reserved = models.IntegerField()
    tb_reserved_till_datetime = models.DateTimeField()
    row_ver = models.IntegerField()
    #scripts = models.ManyToManyField(Scripts,through='ScriptsTestbedSupport', through_fields=('scripts', 'testbeds'))
    def publish(self):
        self.save()
    def __int__(self):
        return self.tb_id
    def __str__(self):
        return self.tb_name
    def save(self, args, *kwargs):
        # On save, update timestamps 
        self.tb_status_reservation_time = timezone.now()
        return super(Testbed, self).save(*args, **kwargs)

    class Meta:
        db_table = "testbeds"

class Script(models.Model):
    script_id = models.IntegerField(unique=True)
    script_name = models.CharField(max_length=200)
    status_id = models.CharField(max_length=200)
    #status_id = models.ForeignKey(ScriptCodeStatus, db_column='status_id',)
    #status_id = models.ForeignKey(ScriptCodeStatus, blank=False, null=False, db_column='status_id')
    script_status_comments = models.CharField(max_length=200)
    request = models.CharField(max_length=200)
    script_version = models.CharField(max_length=200)
    script_repo = models.CharField(max_length=200)
    script_branch = models.CharField(max_length=200)
    testbeds = models.ManyToManyField(Testbed, through='ScriptsTestbedSupport', through_fields=('scripts', 'testbeds'))
    def publish(self):
        self.save()
    def __int__(self):
        return self.script_id
    def __str__(self):
        return self.script_name
    #def __int__(self):
        #return self.script_id
    class Meta:
        db_table = "scripts"

class ScriptsTestbedSupport(models.Model):
    #scripts = models.ForeignKey(Scripts,db_column='script_id')
    #testbed = models.ForeignKey(Testbed,db_column='testbed_id') 
    scripts = models.ForeignKey(Script, db_column='script_id', to_field='script_id', on_delete=models.CASCADE)
    testbeds = models.ForeignKey(Testbed, db_column='testbed_id', to_field='tb_id', on_delete=models.CASCADE)
    #def publish(self):
        #self.save()

    def __int__(self):
        return self.script_id

    class Meta:
        db_table = "scripts_testbed_support"
        auto_created = True

class ScriptsTestbedSupportInline(admin.TabularInline):
    model = ScriptsTestbedSupport
    extra = 1

class ScriptAdmin(admin.ModelAdmin):
    inlines = (ScriptsTestbedSupportInline,)

class TestbedAdmin(admin.ModelAdmin):
    inlines = (ScriptsTestbedSupportInline,)

class TestbedCodePlatform(models.Model):
     platform_id = models.CharField(max_length=10)
     platform_name = models.CharField(max_length=20)

     def publish(self):
         self.save()

     def __str__(self):
         return self.platform_name
     class Meta:
         db_table = "testbeds_code_platforms"
