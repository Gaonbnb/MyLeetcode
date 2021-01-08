# 20 有效的括号
1. 暴力解法 不断replace匹配到的字符串
2. stack

# 155 最小栈


# 84 求柱子面积
1. 暴力求解 o(n^3)
>for i -> 0, n-2  
>&nbsp;&nbsp;&nbsp;&nbsp;for j-> i+1, n-1  
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(i, j) -> 最小高度， area<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;update max_area
2. 暴力求解加强版
>for i -> 0, n-1:<br>
>&nbsp;&nbsp;&nbsp;&nbsp;找到left bound, right bound,  
>&nbsp;&nbsp;&nbsp;&nbsp;area = height[i] * (right-left)  
>&nbsp;&nbsp;&nbsp;&nbsp;update max_area

2. stack
