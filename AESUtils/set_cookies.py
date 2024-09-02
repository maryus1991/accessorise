from django.shortcuts import render


def request_set_cookies_and_render(request, template_name, context, cookie_key, cookie_value=' ', cookie_expires=7):
    response = render(request, template_name, context)
    exist_cookie = request.COOKIES.get(cookie_key)
    if cookie_expires is None:
        max_age_cookies = 365*24*60*60
    else:
        max_age_cookies = cookie_expires * 24 * 60 * 60

    if exist_cookie is None:
        response.set_cookie(cookie_key, cookie_value,
                            max_age=max_age_cookies)
        return response
    elif exist_cookie is not None:
        cookie_last_value = str(request.COOKIES.get(cookie_key))
        cookie_value += str(cookie_last_value)
        response.set_cookie(cookie_key, cookie_value, max_age=max_age_cookies)
        return response
