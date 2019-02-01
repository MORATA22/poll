# import os
#
# from django.conf import settings
# from django_tutorial import settings as django_tutorial
from poll.models import Question
import datetime
from django.utils import timezone
#
# settings.configure(default_settings=django_tutorial, DEBUG=True)
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_tutorial.settings')
future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
future_question.was_published_recently()

# def test():
#     future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
#     future_question.was_published_recently()


# if __name__ == "__main__":
#     test()
