from django.shortcuts import redirect


def request_set_cookies_and_render(request, cookie_key, cookie_value=' ', cookie_expires=7):
    previous_url = request.META.get('HTTP_REFERER')
    response = redirect(previous_url)
    exist_cookie = request.COOKIES.get(cookie_key)

    if cookie_expires is None:
        max_age_cookies = 365 * 24 * 60 * 60
    else:
        max_age_cookies = cookie_expires * 24 * 60 * 60

    if exist_cookie is None:
        response.set_cookie(cookie_key, cookie_value,
                            max_age=max_age_cookies)
        return response
    elif exist_cookie is not None:
        cookie_last_value: str = request.COOKIES.get(cookie_key)
        if cookie_value in cookie_last_value:
            return response
        else:
            cookie_last_value += cookie_value
            response.set_cookie(cookie_key, cookie_last_value, max_age=max_age_cookies)
            return response
