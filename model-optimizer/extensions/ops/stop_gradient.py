# Copyright (C) 2018-2021 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from mo.front.common.partial_infer.elemental import copy_shape_infer
from mo.graph.graph import Graph
from mo.ops.op import Op


class StopGradientOp(Op):
    op = 'StopGradient'
    enabled = True

    def __init__(self, graph: Graph, attrs: dict):
        super().__init__(graph, {
            'type': None,
            'op': self.op,
            'identity': True,
            'in_ports_count': 1,
            'out_ports_count': 1,
            'infer': copy_shape_infer
        }, attrs)

