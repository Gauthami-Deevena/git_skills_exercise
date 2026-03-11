from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel', members=['Iron Man', 'Captain America', 'Thor', 'Black Widow'])
        dc = Team.objects.create(name='dc', members=['Superman', 'Batman', 'Wonder Woman', 'Flash'])

        # Create users
        User.objects.create(email='ironman@marvel.com', name='Iron Man', team='marvel')
        User.objects.create(email='cap@marvel.com', name='Captain America', team='marvel')
        User.objects.create(email='thor@marvel.com', name='Thor', team='marvel')
        User.objects.create(email='widow@marvel.com', name='Black Widow', team='marvel')
        User.objects.create(email='superman@dc.com', name='Superman', team='dc')
        User.objects.create(email='batman@dc.com', name='Batman', team='dc')
        User.objects.create(email='wonderwoman@dc.com', name='Wonder Woman', team='dc')
        User.objects.create(email='flash@dc.com', name='Flash', team='dc')

        # Create activities
        Activity.objects.create(user='Iron Man', type='run', duration=30, date='2026-03-11')
        Activity.objects.create(user='Captain America', type='cycle', duration=45, date='2026-03-11')
        Activity.objects.create(user='Thor', type='swim', duration=60, date='2026-03-11')
        Activity.objects.create(user='Black Widow', type='yoga', duration=20, date='2026-03-11')
        Activity.objects.create(user='Superman', type='run', duration=50, date='2026-03-11')
        Activity.objects.create(user='Batman', type='cycle', duration=40, date='2026-03-11')
        Activity.objects.create(user='Wonder Woman', type='swim', duration=55, date='2026-03-11')
        Activity.objects.create(user='Flash', type='yoga', duration=25, date='2026-03-11')

        # Create leaderboard
        Leaderboard.objects.create(team='marvel', points=185)
        Leaderboard.objects.create(team='dc', points=170)

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do pushups', difficulty='easy')
        Workout.objects.create(name='Pullups', description='Do pullups', difficulty='medium')
        Workout.objects.create(name='Squats', description='Do squats', difficulty='easy')
        Workout.objects.create(name='Plank', description='Hold plank', difficulty='hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
