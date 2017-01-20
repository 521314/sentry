from __future__ import absolute_import, print_function

from django.views.generic import View

from sentry.security.emails import generate_security_email

from .mail import MailPreview


class DebugPasswordChangedEmailView(View):
    def get(self, request):
        email = generate_security_email(
            account=request.user,
            actor=request.user,
            type='password-changed',
            ip_address=request.META['REMOTE_ADDR'],
        )
        return MailPreview(
            html_template=email.html_template,
            text_template=email.template,
            context=email.context,
        ).render(request)