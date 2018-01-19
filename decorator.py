def wrap_tag(tag):
    def wrapper(func):
        def inner_wrapper(name,family):
            return "<{0}>{1}</{0}>".format(tag,func(name,family))
        return inner_wrapper
    return wrapper

@wrap_tag("a")
@wrap_tag("b")
@wrap_tag("c")
def get_fullname(name,family):
    return name+" "+family

get_fullname("hello","world")
