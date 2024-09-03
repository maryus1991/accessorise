import json

from django.shortcuts import redirect


def request_set_cookies_and_render(request, cookie_key, cookie_value=' ', counter=0, sizer=0, cookie_expires=7):
    previous_url = request.META.get('HTTP_REFERER')
    response = redirect(previous_url)
    exist_cookie = request.COOKIES.get(cookie_key)

    if cookie_expires is None:
        max_age_cookies = 365 * 24 * 60 * 60
    else:
        max_age_cookies = cookie_expires * 24 * 60 * 60

    if exist_cookie is None:
        cookie_json = [{
            'pid': cookie_value,
            'count': counter,
            'size': sizer
        }]

        response.set_cookie(
            cookie_key,
            json.dumps(cookie_json),
            max_age=max_age_cookies)
        return response

    elif exist_cookie is not None:
        cookie_last_value: list = json.loads(request.COOKIES.get(cookie_key))
        print(cookie_last_value)
        for cookie_dict in cookie_last_value:
            pid: int = cookie_dict.get('pid')
            count: int = cookie_dict.get('count')
            if cookie_value == pid:
                cookie_dict = {
                    'pid': pid,
                    'count': count + counter,
                    'size': sizer
                }
                cookie_last_value.append(cookie_dict)

            else:
                cookie_dict = {
                    'pid': cookie_value,
                    'count': counter,
                    'size': sizer
                }
                cookie_last_value.append(cookie_dict)

        response.set_cookie(cookie_key,
                            json.dumps(cookie_last_value), max_age=max_age_cookies)
        return response
