from persistent.dict import PersistentDict
from persistent.list import PersistentList

from deform_treepy.utilities.tree_utility import (
    tree_to_keywords, get_all_branches)

from novaideo.content.keyword import ROOT_TREE, DEFAULT_TREE


def deepcopy(obj):
    result = None
    if isinstance(obj, (dict, PersistentDict)):
        result = {}
        for key, value in obj.items():
            result[key] = deepcopy(value)

    elif isinstance(obj, (list, tuple, PersistentList)):
        result = [deepcopy(value) for value in obj]
    else:
        result = obj

    return result


def synchronize_tree():
    """Return a property. The getter of the property returns the
    ``_tree`` attribute of the instance on which it's defined. The setter
    of the property calls ``synchronize_tree()``.

      class SomeContentType(Persistent):
          tree = synchronize_tree()
    """
    def _get(self):
        return getattr(self, '_tree', DEFAULT_TREE)

    def _set(self, newtree):
        self._tree = PersistentDict(deepcopy(newtree))
        self.branches = PersistentList(
            [k.lower() for k in get_all_branches(self._tree)])
        self.keywords = PersistentList(
            tree_to_keywords(self._tree, False))
        if ROOT_TREE in self.keywords:
            self.keywords.remove(ROOT_TREE)

    return property(_get, _set)
