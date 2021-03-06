"""
Libra Static Neural Network Analyzer
====================================

:Author: Caterina Urban
"""
import argparse
from multiprocessing import cpu_count

from libra.engine.bias_analysis import BiasAnalysis, AbstractDomain


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'specification',
        help='input specification')
    parser.add_argument(
        'neural_network',
        help='neural network (.py file) to analyze')

    parser.add_argument(
        '--domain',
        help='abstract domain to be used for the forward pre-analysis (boxes, symbolic, or deeppoly)',
        default='symbolic')

    parser.add_argument(
        '--lower',
        help='lower bound for the forward pre-analysis',
        type=float,
        default=0.25)

    parser.add_argument(
        '--upper',
        help='upper bound for the forward pre-analysis',
        type=int,
        default=2)

    parser.add_argument(
        '--cpu',
        help='number of CPUs to be used for the analysis',
        type=int,
        default=cpu_count())

    args = parser.parse_args()

    if args.domain == 'boxes':
        BiasAnalysis(args.specification, domain=AbstractDomain.BOXES, difference=args.lower, widening=args.upper, cpu=args.cpu).main(args.neural_network)
    if args.domain == 'symbolic':
        BiasAnalysis(args.specification, domain=AbstractDomain.SYMBOLIC2, difference=args.lower, widening=args.upper, cpu=args.cpu).main(args.neural_network)
    if args.domain == 'deeppoly':
        BiasAnalysis(args.specification, domain=AbstractDomain.DEEPPOLY, difference=args.lower, widening=args.upper, cpu=args.cpu).main(args.neural_network)


if __name__ == '__main__':
    main()
