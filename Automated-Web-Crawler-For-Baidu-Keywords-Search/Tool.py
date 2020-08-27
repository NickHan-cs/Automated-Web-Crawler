from lxml import etree as le
from threading import Thread


def xpath_one(contentx, path, default=None):
    rets = contentx.xpath(path)
    return rets[0] if rets else default


def xpath_all(contentx, path):
    return contentx.xpath(path)


def xpath_union(contentx, path, split_str=''):
    rets = [ret.strip() for ret in contentx.xpath(path)]
    return split_str.join(rets)


def to_xml(content: str):
    return le.HTML(content)


def thread_wrapper(func):
    def wrapper(*args, **kwargs):
        t = Thread(target=func, args=args, kwargs=kwargs)
        t.start()
        return t

    return wrapper
