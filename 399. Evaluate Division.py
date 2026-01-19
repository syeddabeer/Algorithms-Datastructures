"""
399. Evaluate Division
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
Return the answers to all queries. If a single answer cannot be determined, return -1.0.
Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.
Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.
Example 1:
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0
Example 2:
Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:
Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
"""
class Solution:
        def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
            from collections import defaultdict
            graph = defaultdict(defaultdict)
            for (num, den), val in zip(equations, values):
                graph[num][den] = val
                graph[den][num] = 1/val
            def finddenval(num, den, prod, visited):
                visited.add(num)
                ret = -1.0
                neighbor = graph[num]
                if den in neighbor: 
                    ret = prod*neighbor[den]
                else:
                    for neighbor, value in neighbor.items():
                        if neighbor in visited:
                            continue
                        ret = finddenval(neighbor, den, prod*value, visited)
                        if ret!= -1.0:
                            break
                visited.remove(num)
                return ret
            ans = []
            for num, den in queries:
                if num not in graph or den not in graph:
                    ret = -1.0
                elif num==den:
                    ret = 1.0
                else:
                    visited = set()
                    ret = finddenval(num, den, 1, visited)
                ans.append(ret)
            return ans
