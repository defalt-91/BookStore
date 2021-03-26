import stripe
from django.views.generic import TemplateView
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


class OrdersPageView(LoginRequiredMixin, TemplateView):
    template_name = 'orders/purchase.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context


@login_required
def charge(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=3900,
            currency='usd',
            description='Purchase all books',
            source=request.POST['stripeToken']
        )
    user = request.user
    permission = Permission.objects.get(codename='special_status')
    user.user_permissions.add(permission)
    return render(request, 'orders/charge.html')
