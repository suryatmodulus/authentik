"""dummy tests"""
from django.urls import reverse

from authentik.core.models import User
from authentik.flows.models import Flow, FlowDesignation, FlowStageBinding
from authentik.flows.tests import FlowTestCase
from authentik.stages.dummy.models import DummyStage


class TestDummyStage(FlowTestCase):
    """Dummy tests"""

    def setUp(self):
        super().setUp()
        self.user = User.objects.create(username="unittest", email="test@beryju.org")

        self.flow = Flow.objects.create(
            name="test-dummy",
            slug="test-dummy",
            designation=FlowDesignation.AUTHENTICATION,
        )
        self.stage = DummyStage.objects.create(
            name="dummy",
        )
        FlowStageBinding.objects.create(
            target=self.flow,
            stage=self.stage,
            order=0,
        )

    def test_valid_render(self):
        """Test that View renders correctly"""
        response = self.client.get(
            reverse("authentik_api:flow-executor", kwargs={"flow_slug": self.flow.slug})
        )
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        """Test with valid email, check that URL redirects back to itself"""
        url = reverse("authentik_api:flow-executor", kwargs={"flow_slug": self.flow.slug})
        response = self.client.post(url, {})
        self.assertEqual(response.status_code, 200)
        self.assertStageRedirects(response, reverse("authentik_core:root-redirect"))
