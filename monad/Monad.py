
def do_block(bind, *stmts):
    if len(stmts) == 1:
        return lambda y: stmts[0](y)
    else:
        return lambda x: bind(stmts[0](x), do_block(bind, *stmts[1:]))