{% extends "mail_templated/base.tpl" %}

{% block subject %}
Reset Your Password
{% endblock %}

{% block html %}
<h2>Password Reset</h2>

<p>Click the link below to reset your password:</p>

<a href="http://127.0.0.1:8001/accounts/api/v1/reset-password/confirm/{{ uid }}/{{ token }}/">
    Reset Password
</a>

{% endblock %}