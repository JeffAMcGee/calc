import operator


OPS = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
}


def tokenize(line):
    return [ OPS.get(c) or int(c) for c in line]


def eval_tokens(tkns):
    if len(tkns)==1:
        return tkns[0]
    subexp,func,val = tkns[:-2],tkns[-2],tkns[-1]
    return func(eval_tokens(subexp),val)


def eval_exp(exp):
    return eval_tokens(tokenize(exp))


def main():
    exp = raw_input('>').strip()
    print eval_exp(exp)


if __name__=='__main__':
    main()

