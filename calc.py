import operator


OPS = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
}


def parse(line):
    return [ OPS.get(c) or int(c) for c in line]


def eval_exp(exp):
    if len(exp)==1:
        return exp[0]
    subexp,func,val = exp[:-2],exp[-2],exp[-1]
    return func(eval_exp(subexp),val)


def main():
    exp = parse(raw_input('>').strip())
    print eval_exp(exp)


if __name__=='__main__':
    main()

