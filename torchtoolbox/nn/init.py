# -*- coding: utf-8 -*-
# @Author  : DevinYang(pistonyang@gmail.com)

from torch import nn
from torch.nn.init import xavier_normal_, xavier_uniform_, \
    kaiming_normal_, kaiming_uniform_
import math


def Xavier(model, random_type='uniform', gain=math.sqrt(2.0)):
    """Initialize a model params by Xavier.

    Fills the input `Tensor` with values according to the method
    described in `Understanding the difficulty of training deep feedforward
    neural networks` - Glorot, X. & Bengio, Y. (2010)

    Args:
        model (nn.Module): model you need to initialize.
        random_type (string): random_type
        gain (float): an optional scaling factor, default is sqrt(2.0)


    """
    assert random_type in ('uniform', 'normal')
    initializer = xavier_uniform_ if random_type == 'uniform' else xavier_normal_

    for m in model.modules():
        if isinstance(m, (nn.Conv2d, nn.Conv3d)):
            initializer(m.weight.data, gain=gain)
            if m.bias is not None:
                m.bias.data.zero_()
        elif isinstance(m, (nn.BatchNorm2d, nn.BatchNorm3d, nn.GroupNorm)):
            m.weight.data.fill_(1)
            if m.bias is not None:
                m.bias.data.zero_()
        elif isinstance(m, nn.Linear):
            initializer(m.weight.data, gain=gain)
            if m.bias is not None:
                m.bias.data.zero_()


def Kaiming(model, slope=0, mode='fan_out', nonlinearity='relu', random_type='normal'):
    """Initialize a model params by Xavier.

    Fills the input `Tensor` with values according to the method
    described in `Delving deep into rectifiers: Surpassing human-level
    performance on ImageNet classification` - He, K. et al. (2015)

    Args:
        model (nn.Module): model you need to initialize.
        slope: the negative slope of the rectifier used after this layer (0 for ReLU
            by default)
        mode (string): either ``'fan_in'`` (default) or ``'fan_out'``. Choosing ``'fan_in'``
            preserves the magnitude of the variance of the weights in the
            forward pass. Choosing ``'fan_out'`` preserves the magnitudes in the
            backwards pass.
        nonlinearity (string): the non-linear function (`nn.functional` name),
            recommended to use only with ``'relu'`` or ``'leaky_relu'`` (default).
        random_type (string): random_type

    """
    assert random_type in ('uniform', 'normal')
    initializer = kaiming_uniform_ if random_type == 'uniform' else kaiming_normal_

    for m in model.modules():
        if isinstance(m, (nn.Conv2d, nn.Conv3d)):
            initializer(m.weight.data, slope, mode, nonlinearity)
            if m.bias is not None:
                m.bias.data.zero_()
        elif isinstance(m, (nn.BatchNorm2d, nn.BatchNorm3d, nn.GroupNorm)):
            m.weight.data.fill_(1)
            if m.bias is not None:
                m.bias.data.zero_()
        elif isinstance(m, nn.Linear):
            initializer(m.weight.data, slope, mode, nonlinearity)
            if m.bias is not None:
                m.bias.data.zero_()