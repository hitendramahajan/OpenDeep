"""
.. module:: statistics

This module is used for computing statistics such as mean, variance, mode, regularization values, etc.
"""

__authors__ = "Markus Beissinger"
__copyright__ = "Copyright 2015, Vitruvian Science"
__credits__ = ["Markus Beissinger"]
__license__ = "Apache"
__maintainer__ = "OpenDeep"
__email__ = "opendeep-dev@googlegroups.com"

# standard libraries
import logging
# third party libraries
import theano.tensor as T
# internal imports
from opendeep.utils.misc import raise_to_list

log = logging.getLogger(__name__)

def get_stats(input, stat=None):
    """
    returns a dictionary mapping the name of the statistic to the result on the input

    :param input: theano tensor
    :type input: tensor

    :return: dictionary of all the statistics expressions
    :rtype: dict(string: theano expression)
    """
    stats = {
        'mean': T.mean(input),
        'var': T.var(input),
        'std': T.std(input),
        'min': T.min(input),
        'max': T.max(input),
        'l1': input.norm(L=1),
        'l2': input.norm(L=2),
        #'num_nonzero': T.sum(T.nonzero(input)),
    }
    stat_list = raise_to_list(stat)
    compiled_stats = {}
    if stat_list is None:
        return stats

    for stat in stat_list:
        if isinstance(stat, basestring) and stat in stats:
            compiled_stats.update({stat: stats[stat]})
    return compiled_stats