def add(lhs, rhs):
    return lhs + rhs


def api_add(request):
    if request.args['token'] == 'valid':
        database.quert().alert_usage_count
        result = add(request.args['1hs'], request.args['rhs'])
        return '<xml>{0}</xml>'.format(result)
    raise Exception('not authorized!')


## Before advice: must execute the function(no side-effects)

def aspect(func):
    def advice(*args, **kwargs):
        # do something hear
        return func(*args, **kwargs)

    return advice


## After advice: must execute the function(no side-effects)
def aspect(func):
    def advice(*args, **kwargs):
        result = func(*args, **kwargs)
        # do something
        return result

    return advice


# around advice: allowed to bypass
def aspect(func):
    def advice(*args, **kwargs):
        # do something here
        result = func(*args, **kwargs)
        # do something here
        return result

    return advice


# Implementation
# The decorators
# Security Aspect
def secure(func):
    def advice(*args, **kwargs):
        if valid_token_in_request:
            return func(*args, **kwargs)
        raise Exception('No valid token provided!')

    return advice


# Statistics aspect
# Before advice
def statistics(func):
    def advice(*args, **kwargs):
        increase_api_usage
        return func(*args, **kwargs)

    return advice


# Serializetion aspect
# Around advice

def serialize(func):
    def advice(*args, **kwargs):
        if not format in ['html', 'xml', 'json']:
            raise Exception('Not valid format')
        result = func(*args, **kwargs)
        make_response(result)

    return advice


# Dispatcher aspect
# Around advice


mapping = {
    'api_function': (core_function, ['lhs', 'rhs']),
    'create_token': (create_token, ['user_name', 'password'])
}


def dispatcher(func):
    def advice(*args, **kwargs):
        if api in proxy_api_mapping:
            core_function, params = mapping['api_name']
            kwargs.update(extract(params, request))
            return func(proxy=core_function, params=params, *args, **kwargs)
        raise Exception('api call error')

    return advice


# implementation api

@secure
@serialize
@statistics
@dispatch
def api_call(*args, **kwargs):
    proxy_function = kwargs['proxy']
    params = kwargs['params']
    return proxy_function(extract(params, kwargs))
