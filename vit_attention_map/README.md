# Attention Rollout

Attention rollout 是一种在 Transformer 模型中可视化和解释注意力机制的方法。它解决了一个问题，即 Transformer 模型更深层次的注意力权重变得越来越混合且可解释性越来越差。

Attention rollout 背后的关键思想是通过将各层注意力矩阵相乘来递归计算 Transformer 每一层的 tokens attention。这使得注意力信号可以在整个网络中传播，而不仅仅是在前几层可见。

具体来说，Attention Rollout 算法的工作原理如下：

1. 从第一层的注意力矩阵开始
2. 对于每个后续层，将当前层的注意力矩阵与前一层的注意力矩阵相乘
3. 对最终注意力矩阵的行进行归一化，确保总注意力流总和为1

这种递归计算使该方法能够捕获信息如何流经 Transformer 的自注意层。

与仅查看原始注意力权重相比，Attention rollout 已被证明可以产生更具有可解释性和更具有意义的注意力可视化，特别是对于 Transformer 模型的更深层。它提供了一种量化信息如何通过自我关注机制传播的方法。

