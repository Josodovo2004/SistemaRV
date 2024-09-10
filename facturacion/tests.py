from django.test import TestCase
from ..tasks import emisionResumenDeBoletas  # Ensure correct import
from celery.result import AsyncResult
from django_celery_beat.models import PeriodicTask, IntervalSchedule

class CeleryTestCase(TestCase):

    def setUp(self):
        # Set up any required objects for the test
        pass
    
    def test_emisionResumenDeBoletas(self):
        # Trigger the task
        result = emisionResumenDeBoletas.delay()
        
        # Wait for task to complete (poll until it's ready)
        result.wait(timeout=10)  # Set timeout as needed
        
        # Check if the task completed successfully
        self.assertTrue(result.successful())
        
        # Check the result of the task (adjust this based on what your task returns)
        self.assertEqual(result.result, None)  # If the task returns something, check it here

    def test_emisionResumenDeBoletas_schedule(self):
        # Create a periodic task schedule (every 1 minute)
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=1,
            period=IntervalSchedule.MINUTES
        )
        
        # Create the periodic task
        PeriodicTask.objects.create(
            interval=schedule,
            name='Test periodic task',
            task='core.tasks.emisionResumenDeBoletas'  # Adjust path if needed
        )
        
        # Check if the periodic task exists in the database
        task_exists = PeriodicTask.objects.filter(name='Test periodic task').exists()
        self.assertTrue(task_exists)
