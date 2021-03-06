from django import template


register = template.Library()

@register.simple_tag
def my_url(value, field_name, urlencode=None):
    url = '?{}={}'.format(field_name,value)
    print(url)
    if urlencode:
        querystring = urlencode.split('&')
        filterd_querystring = filter(lambda p: p.split('=')[0] != field_name,querystring)
        encoded_querystring = '&'.join(filterd_querystring)
        url = '{}&{}'.format(url,encoded_querystring)

    
    return url