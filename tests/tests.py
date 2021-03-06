from lxml.html import fromstring
from django.core.cache import cache
from django.template import Template, Context, loader
from django.test.client import RequestFactory
try:
    from hashlib import md5 as md5_constructor
except ImportError:
    from django.utils.hashcompat import md5_constructor

loader.add_to_builtins('django_activeurl.templatetags.activeurl')

requests = RequestFactory()


def render(template, context=None):
    context = Context(context)
    return Template(template).render(context)


def test_basic():
    template = '''
        {% activeurl %}
            <ul>
                <li>
                    <a href="/page/">page</a>
                </li>
                <li>
                    <a href="/other_page/">other_page</a>
                </li>
            </ul>
        {% endactiveurl %}
    '''

    context = {'request': requests.get('/page/')}
    html = render(template, context)

    print '''
        %s
        ----
        %s
    ''' % (template, html)

    tree = fromstring(html)
    li_elements = tree.xpath('//li')

    active_li = li_elements[0]
    assert 'class' in active_li.attrib.keys()
    css_class = active_li.attrib['class']
    assert css_class == 'active'

    inactive_li = li_elements[1]
    assert not 'class' in inactive_li.attrib.keys()


def test_cache():
    html = '<ul><li><a href="/page/">page</a></li></ul>'
    template = '{% activeurl %}<ul><li><a href="/page/">page</a></li></ul>{% endactiveurl %}'

    context = {'request': requests.get('/page/')}
    set_cache = render(template, context)

    cache_key = 'django_activeurl.' \
    + md5_constructor(
        html + 'active' + 'li' + '/page/'
    ).hexdigest()

    assert cache.get(cache_key)


def test_submenu():
    template = '''
        {% activeurl %}
            <ul>
                <li>
                    <a href="/menu/">menu</a>
                </li>
                <li>
                    <a href="/menu/submenu/">submenu</a>
                </li>
                <li>
                    <a href="/menu/other_submenu/">other_submenu</a>
                </li>
            </ul>
        {% endactiveurl %}
    '''

    context = {'request': requests.get('/menu/submenu/')}
    html = render(template, context)

    print '''
        %s
        ----
        %s
    ''' % (template, html)

    tree = fromstring(html)
    li_elements = tree.xpath('//li')

    active_menu = li_elements[0]
    assert 'class' in active_menu.attrib.keys()
    css_class = active_menu.attrib['class']
    assert css_class == 'active'

    active_submenu = li_elements[1]
    assert 'class' in active_submenu.attrib.keys()
    css_class = active_submenu.attrib['class']
    assert css_class == 'active'

    inactive_submenu = li_elements[2]
    assert not 'class' in inactive_submenu.attrib.keys()


def test_kwargs():
    template = '''
        {% activeurl parent_tag='div' css_class='current' %}
            <div>
                <div>
                    <a href="/page/">page/</a>
                </div>
                <div>
                    <a href="/other_page/">other_page</a>
                </div>
            </div>
        {% endactiveurl %}
    '''

    context = {'request': requests.get('/page/')}
    html = render(template, context)

    print '''
        %s
        ----
        %s
    ''' % (template, html)

    tree = fromstring(html)
    div_elements = tree.xpath('//div')

    active_div = div_elements[1]
    assert 'class' in active_div.attrib.keys()
    css_class = active_div.attrib['class']
    assert css_class == 'current'

    inactive_div = div_elements[2]
    assert not 'class' in inactive_div.attrib.keys()
