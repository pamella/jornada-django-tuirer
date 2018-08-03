from django.test import TestCase, Client
from django.urls import reverse

from model_mommy import mommy
from tuites.models import Tuite

# métodos de teste sempre começam com o termo 'test'


class TestPostTuiteView(TestCase):
    def setUp(self):
        super().setUp()
        # criando usuário no banco de dados de teste
        self.view_url = reverse('tuites:post_tuite')
        self.user = mommy.prepare('users.User')
        self.user.set_password('123456')
        self.user.save()

        # usuário logado
        self.auth_client = Client()
        self.auth_client.login(username=self.user.username, password='123456')

    def test_status_code_200_for_authententicated_users(self):
        response = self.auth_client.get(self.view_url)
        self.assertEqual(response.status_code, 200)

    def test_redirect_non_authenticaded_users(self):
        response = self.client.get(self.view_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=/postar/')

    def test_post_tuite_creates_tuite(self):
        tuite_params = {
            'content': 'Meu tuite!',
            'author': self.user.id,
        }
        response = self.auth_client.post(self.view_url, tuite_params, follow=True)
        tuite_exists = Tuite.objects.filter(content=tuite_params.get('content')).exists()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(tuite_exists)
