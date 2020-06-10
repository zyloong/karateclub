import networkx as nx

from karateclub import Role2Vec, GraphWave


def test_role2vec():
    """
    Testing the Role2Vec class.
    """
    model = Role2Vec()

    graph = nx.watts_strogatz_graph(100, 10, 0.5)

    model.fit(graph)

    embedding = model.get_embedding()

    assert embedding.shape[0] == graph.number_of_nodes()
    assert embedding.shape[1] == model.dimensions


def test_graphwave():
    """
    Testing the GraphWave class.
    """
    model = GraphWave()

    graph = nx.watts_strogatz_graph(100, 10, 0.5)

    model.fit(graph)

    embedding = model.get_embedding()

    assert embedding.shape[0] == graph.number_of_nodes()
    assert embedding.shape[1] == 2*model.sample_number
