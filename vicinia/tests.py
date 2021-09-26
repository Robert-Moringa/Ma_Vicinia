from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

class ProfileTest(TestCase):
    def setUp(self):
        self.robert= User.objects.create(username="Robert")
        self.test_profile= Profile.objects.create(user=self.robert,
                                                email='rober@gmail.com',
                                                pub_date='12',                                   
                                                why_here ='No retreat no surrender',
                                                profile_pic ='picture.jpg',
                                                )
        self.test_profile.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.test_profile, Profile))

    #Testing Save method
    def test_save_method(self):
        self.test_profile.save()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)>0)

    # Tear down
    def tearDown(self):
        Profile.objects.all().delete()

    # delete methodTesting 
    def test_delete_profile(self):
        self.test_profile.delete()
        self.assertEqual(len(Profile.objects.all()), 0)