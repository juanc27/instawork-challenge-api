from django.test import TestCase
from api.members.models import Member
from django.core.exceptions import ValidationError

class MemberTestCase(TestCase):
    def setUp(self):
        pass

    def test_create_member_with_invalid_role(self):
        """Member role can only be one of the choices included in the model"""
        member = Member(
            first_name = 'Joe',
            last_name = 'Doe',
            email = 'test@test.com',
            phone = '555-555-5555',
            role = 'TEST')
        self.assertRaises(ValidationError, member.full_clean)

    def test_create_member_with_invalid_phone(self):
        """Member role can only be one of the choices included in the model"""
        member = Member(
            first_name = 'Joe',
            last_name = 'Doe',
            email = 'test@test.com',
            phone = '55',
            role = 'admin')
        self.assertRaises(ValidationError, member.full_clean)
