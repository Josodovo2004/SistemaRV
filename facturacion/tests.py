# myapp/tests.py
from django.test import TestCase
from celery import Celery
from celery.result import AsyncResult
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from tasks import emisionResumenDeBoletas

class CeleryTestCase(TestCase):
    
    def setUp(self):
        # Set up any required objects for the test
        pass
    
    def test_emisionResumenDeBoletas(self):
        # Manually trigger the task
        result = emisionResumenDeBoletas.delay()
        
        # Wait for the task to complete
        self.assertTrue(result.ready())
        
        # Check the result of the task
        self.assertEqual(result.result, None)  # Adjust based on your task's expected result
        
        # Alternatively, you can check if the task was executed by other means
        # (e.g., checking a log file or database entry)
    
    def test_emisionResumenDeBoletas_schedule(self):
        # Create a periodic task
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=1,
            period=IntervalSchedule.MINUTES
        )
        PeriodicTask.objects.create(
            interval=schedule,
            name='Test periodic task',
            task='myapp.tasks.my_periodic_task'
        )
        
        # Check if the periodic task exists in the database
        task_exists = PeriodicTask.objects.filter(name='Test periodic task').exists()
        self.assertTrue(task_exists)
