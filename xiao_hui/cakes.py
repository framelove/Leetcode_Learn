#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 时间:   2019-5-27 15:41
# 作者:   ljk

# 将人的饭量由小到大排列，当从小到大匹配蛋糕时，即使用了贪心算法，容易得到局部最优解（从在一个蛋糕可以满足两个人而被一个人分）；
# 所以只能从大到小来匹配蛋糕，并且切分最先满足条件的蛋糕，这样做的一个基础结论是【最多满足的顾客组合中，一定有一个是连续的】
