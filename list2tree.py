source = [
    (None, 'a'),
    (None, 'b'),
    (None, 'c'),
    ('a', 'a1'),
    ('a', 'a2'),
    ('a2', 'a21'),
    ('a2', 'a22'),
    ('b', 'b1'),
    ('b1', 'b11'),
    ('b11', 'b111'),
    ('b', 'b2'),
    ('c', 'c1'),
]

expected = {
    'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
    'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
    'c': {'c1': {}},
}


def to_tree():
    roots = set()
    mapping = {}
    for parent, child in source:
        childitem = mapping.get(child)
        if childitem is None:
            childitem = {}
            mapping[child] = childitem
        else:
            roots.discard(child)
        parentitem = mapping.get(parent)
        if parentitem is None:
            mapping[parent] = {child: childitem}
            roots.add(parent)
        else:
            parentitem[child] = childitem
    tree = {id_: mapping[id_] for id_ in roots}
    return tree[None]


assert to_tree() == expected
