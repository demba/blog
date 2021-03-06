# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548692602.946999
_enable_loop = True
_template_filename = u'/home/demba/.pyenv/versions/blgng/local/lib/python2.7/site-packages/nikola/data/themes/base/templates/post_helper.tmpl'
_template_uri = u'post_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_tags', 'html_pager', 'twitter_card_information', 'meta_translations', 'mathjax_script', 'open_graph_metadata']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_tags(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        _link = context.get('_link', UNDEFINED)
        hidden_tags = context.get('hidden_tags', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if post.tags:
            __M_writer(u'        <ul itemprop="keywords" class="tags">\n')
            for tag in post.tags:
                if tag not in hidden_tags:
                    __M_writer(u'            <li><a class="tag p-category" href="')
                    __M_writer(unicode(_link('tag', tag)))
                    __M_writer(u'" rel="tag">')
                    __M_writer(unicode(tag))
                    __M_writer(u'</a></li>\n')
            __M_writer(u'        </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_pager(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if post.prev_post or post.next_post:
            __M_writer(u'        <ul class="pager hidden-print">\n')
            if post.prev_post:
                __M_writer(u'            <li class="previous">\n                <a href="')
                __M_writer(unicode(post.prev_post.permalink()))
                __M_writer(u'" rel="prev" title="')
                __M_writer(filters.html_escape(unicode(post.prev_post.title())))
                __M_writer(u'">')
                __M_writer(unicode(messages("Previous post")))
                __M_writer(u'</a>\n            </li>\n')
            if post.next_post:
                __M_writer(u'            <li class="next">\n                <a href="')
                __M_writer(unicode(post.next_post.permalink()))
                __M_writer(u'" rel="next" title="')
                __M_writer(filters.html_escape(unicode(post.next_post.title())))
                __M_writer(u'">')
                __M_writer(unicode(messages("Next post")))
                __M_writer(u'</a>\n            </li>\n')
            __M_writer(u'        </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_twitter_card_information(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        twitter_card = context.get('twitter_card', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if twitter_card and twitter_card['use_twitter_cards']:
            __M_writer(u'    <meta name="twitter:card" content="')
            __M_writer(filters.html_escape(unicode(twitter_card.get('card', 'summary'))))
            __M_writer(u'">\n')
            if 'site:id' in twitter_card:
                __M_writer(u'    <meta name="twitter:site:id" content="')
                __M_writer(unicode(twitter_card['site:id']))
                __M_writer(u'">\n')
            elif 'site' in twitter_card:
                __M_writer(u'    <meta name="twitter:site" content="')
                __M_writer(unicode(twitter_card['site']))
                __M_writer(u'">\n')
            if 'creator:id' in twitter_card:
                __M_writer(u'    <meta name="twitter:creator:id" content="')
                __M_writer(unicode(twitter_card['creator:id']))
                __M_writer(u'">\n')
            elif 'creator' in twitter_card:
                __M_writer(u'    <meta name="twitter:creator" content="')
                __M_writer(unicode(twitter_card['creator']))
                __M_writer(u'">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_meta_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if len(translations) > 1:
            for langname in sorted(translations):
                if langname != lang and post.is_translation_available(langname):
                    __M_writer(u'                <link rel="alternate" hreflang="')
                    __M_writer(unicode(langname))
                    __M_writer(u'" href="')
                    __M_writer(unicode(post.permalink(langname)))
                    __M_writer(u'">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_mathjax_script(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n')
        if post.is_mathjax:
            __M_writer(u'        <script type="text/x-mathjax-config">\n        MathJax.Hub.Config({tex2jax: {inlineMath: [[\'$latex \',\'$\'], [\'\\\\(\',\'\\\\)\']]}});</script>\n        <script src="/assets/js/mathjax.js"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_open_graph_metadata(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        striphtml = context.get('striphtml', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if use_open_graph:
            __M_writer(u'    <meta property="og:site_name" content="')
            __M_writer(striphtml(unicode(blog_title)))
            __M_writer(u'">\n    <meta property="og:title" content="')
            __M_writer(filters.html_escape(unicode(post.title()[:70])))
            __M_writer(u'">\n    <meta property="og:url" content="')
            __M_writer(unicode(abs_link(permalink)))
            __M_writer(u'">\n')
            if post.description():
                __M_writer(u'    <meta property="og:description" content="')
                __M_writer(filters.html_escape(unicode(post.description()[:200])))
                __M_writer(u'">\n')
            else:
                __M_writer(u'    <meta property="og:description" content="')
                __M_writer(filters.html_escape(unicode(post.text(strip_html=True)[:200])))
                __M_writer(u'">\n')
            if post.previewimage:
                __M_writer(u'    <meta property="og:image" content="')
                __M_writer(unicode(url_replacer(permalink, post.previewimage, lang, 'absolute')))
                __M_writer(u'">\n')
            __M_writer(u'    <meta property="og:type" content="article">\n')
            if post.date.isoformat():
                __M_writer(u'    <meta property="article:published_time" content="')
                __M_writer(unicode(post.formatted_date('webiso')))
                __M_writer(u'">\n')
            if post.tags:
                for tag in post.tags:
                    __M_writer(u'           <meta property="article:tag" content="')
                    __M_writer(unicode(tag))
                    __M_writer(u'">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"15": 0, "20": 2, "21": 11, "22": 23, "23": 40, "24": 69, "25": 85, "26": 93, "32": 13, "38": 13, "39": 14, "40": 15, "41": 16, "42": 17, "43": 18, "44": 18, "45": 18, "46": 18, "47": 18, "48": 21, "54": 25, "59": 25, "60": 26, "61": 27, "62": 28, "63": 29, "64": 30, "65": 30, "66": 30, "67": 30, "68": 30, "69": 30, "70": 33, "71": 34, "72": 35, "73": 35, "74": 35, "75": 35, "76": 35, "77": 35, "78": 38, "84": 71, "89": 71, "90": 72, "91": 73, "92": 73, "93": 73, "94": 74, "95": 75, "96": 75, "97": 75, "98": 76, "99": 77, "100": 77, "101": 77, "102": 79, "103": 80, "104": 80, "105": 80, "106": 81, "107": 82, "108": 82, "109": 82, "115": 3, "123": 3, "124": 4, "125": 5, "126": 6, "127": 7, "128": 7, "129": 7, "130": 7, "131": 7, "137": 87, "141": 87, "142": 88, "143": 89, "149": 42, "160": 42, "161": 43, "162": 44, "163": 44, "164": 44, "165": 45, "166": 45, "167": 46, "168": 46, "169": 47, "170": 48, "171": 48, "172": 48, "173": 49, "174": 50, "175": 50, "176": 50, "177": 52, "178": 53, "179": 53, "180": 53, "181": 55, "182": 60, "183": 61, "184": 61, "185": 61, "186": 63, "187": 64, "188": 65, "189": 65, "190": 65, "196": 190}, "uri": "post_helper.tmpl", "filename": "/home/demba/.pyenv/versions/blgng/local/lib/python2.7/site-packages/nikola/data/themes/base/templates/post_helper.tmpl"}
__M_END_METADATA
"""
