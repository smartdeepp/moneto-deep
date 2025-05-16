from django.contrib import messages


class ToastClass():
    @staticmethod
    def success(request, data):
        message = data.get('message')
        title = data.get('title')
        messages.success(
            request, message,
            extra_tags=dict(title=title)
        )

    @staticmethod
    def error(request, data):
        message = data.get('message')
        title = data.get('title')
        messages.error(
            request, message,
            extra_tags=dict(title=title)
        )


Toast = ToastClass()
