import json
from django.test import TestCase
from api.members.models import Member
from django.core.exceptions import ValidationError

class MemberModelTestCase(TestCase):
    def setUp(self):
        pass

    def test_create_member_with_invalid_role(self):
        """Member role can only be one of the choices included in the model"""
        member = Member(
            first_name = 'Joe',
            last_name = 'Doe',
            email = 'test@test.com',
            phone = '5555555555',
            role = 'TEST')
        self.assertRaises(ValidationError, member.full_clean)

    def test_create_member_with_invalid_email(self):
        """Member role can only be one of the choices included in the model"""
        member = Member(
            first_name = 'Joe',
            last_name = 'Doe',
            email = 'invalidEmail',
            phone = '5555555555',
            role = 'admin')
        self.assertRaises(ValidationError, member.full_clean)

    def test_create_member_with_a_short_phone(self):
        """Member phone needs to be min 10 chars long"""
        member = Member(
            first_name = 'Joe',
            last_name = 'Doe',
            email = 'test@test.com',
            phone = '123456789',
            role = 'admin')
        self.assertRaises(ValidationError, member.full_clean)

    def test_create_member_with_invalid_phone_hyphens(self):
        """Member phone can not have hyphens """
        member = Member(
            first_name = 'Joe',
            last_name = 'Doe',
            email = 'test@test.com',
            phone = '123-456-7890',
            role = 'admin')
        self.assertRaises(ValidationError, member.full_clean)

    def test_create_member_with_plus_sign(self):
        """Member phone can allow a + sign character """
        member = Member.objects.create(
            first_name = 'Joe',
            last_name = 'Doe',
            email = 'test@test.com',
            phone = '+11234567890',
            role = 'admin')
        self.assertEqual(member.phone, '+11234567890')

class MemberViewTestCase(TestCase):
    def setUp(self):
        member1 = Member.objects.create(
            first_name = 'Joe',
            last_name = 'Doe',
            email = 'test@test.com',
            phone = '+11234567890',
            role = 'admin')
        member2 = Member.objects.create(
            first_name = 'AJoe',
            last_name = 'BDoe',
            email = 'test1@test.com',
            phone = '1234567890',
            role = 'regular')

    def test_call_member_view_sorts_item_by_first_name(self):
        response = self.client.get('/members/', follow=True)
        parsed = json.loads(response.content)
        self.assertEqual(len(parsed), 2)
        self.assertEqual(parsed[0]['first_name'], 'AJoe')
        self.assertEqual(parsed[1]['first_name'], 'Joe')
