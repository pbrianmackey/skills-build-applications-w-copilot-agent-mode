from django.core.management.base import BaseCommand
from tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate octofit_db with test data'

    def handle(self, *args, **kwargs):
        # Create users
        user1 = User.objects.create(username='alice', email='alice@example.com')
        user2 = User.objects.create(username='bob', email='bob@example.com')

        # Create teams
        team1 = Team.objects.create(name='Team Alpha')
        team2 = Team.objects.create(name='Team Beta')
        team1.members.add(user1)
        team2.members.add(user2)

        # Create activities
        Activity.objects.create(user=user1, activity_type='Running', duration=30, date='2026-02-26')
        Activity.objects.create(user=user2, activity_type='Cycling', duration=45, date='2026-02-25')

        # Create leaderboard
        Leaderboard.objects.create(team=team1, points=100)
        Leaderboard.objects.create(team=team2, points=80)

        # Create workouts
        Workout.objects.create(user=user1, workout_type='Yoga', suggested=True, date='2026-02-26')
        Workout.objects.create(user=user2, workout_type='HIIT', suggested=False, date='2026-02-25')

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
