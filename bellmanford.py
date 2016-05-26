#=======================================================================
# Author: Isai Damier
# Title:  Bellman-Ford's Single Source Shortest Path
# Project: geekviewpoint
# Package: algorithm.graph
#
# Statement:
#   Given a source vertex and a directed, weighted graph; find the
#   shortest path between the source vertex and each of the other
#   vertices. Some of the edges may have negative weights. If the graph
#   contains any negative weight cycle, throw an exception.
#
# Time-complexity: O(V*E)
#   where V is the number of vertices and E is the number of edges.
#
# The Bellman-Ford Strategy:
#
#   The Bellman-Ford argument is that the longest path in any graph
#   can have at most V-1 edges, where V is the number of vertices.
#   Furthermore, if we perform relaxation on the set of edges once, then
#   we will at least have determined all the one-edged shortest paths;
#   if we traverse the set of edges twice, we will have solved at least
#   all the two-edged shortest paths; ergo, after the V-1 iteration thru
#   the set of edges, we will have determined all the shortest paths
#   in the graph.
#
#   But then Bellman-Ford continues: If after V-1 iterations we are still
#   able to relax any path, then the graph has a negative edge cycle.
#
#   From that argument, even before looking at any code, we can see
#   that the time complexity is (V-1)*E +1*E = V*E. The 1*E is the
#   cycle-detection pass.
#
#   The argument also implicitly tells us that this algorithm does not
#   mind handling negatives edges -- only negative cycles are scary.
#
#   Hence, while Bellman-Ford takes longer than all versions of
#   Dijkstra's algorithm, it has the advantage of accepting all
#   directed graphs.
#
#   I use the term relaxation a few times. Here is the explanation.
#   The computation starts by estimating that all vertices are infinitely
#   far away from the source vertex. Then as we compute, we relax that
#   outrageous assumption by checking if there is actually a shorter
#   distance. For instance, say we have already computed the shortest
#   distance from s to v as sv and now we are seeking the solution from
#   s to x, where x is adjacent to v. Then we know sx <= sv + vx; which
#   simply means, either the path from s to v to x is the shortest path
#   or there is yet a shorter path than that. If however we find that
#   our "outrageous" estimate so far is that sx > sv+vx, then we can
#   set sx = sv+vx as our new better estimate. That's it. That's
#   relaxation.
#======================================================================= 
import unittest
from sys import maxint

class BellmanFord( object ):
 
  def __init__( self ):
      '''
      Constructor
      '''
 
  def singleSourceShortestPath( self, weight, source ) :
    # auxiliary constants
    SIZE = len( weight )
    EVE = -1; # to indicate no predecessor
    INFINITY = maxint
 
    # declare and initialize pred to EVE and minDist to INFINITY
    pred = [EVE] * SIZE
    minDist = [INFINITY] * SIZE
 
    # set minDist[source] = 0 because source is 0 distance from itself.
    minDist[source] = 0
 
    # relax the edge set V-1 times to find all shortest paths
    for i in range( 1, SIZE - 1 ):
      for v in range( SIZE ):
        for x in self.adjacency( weight, v ):
          if minDist[x] > minDist[v] + weight[v][x]:
            minDist[x] = minDist[v] + weight[v][x]
            pred[x] = v
 
    # detect cycles if any
    for v in range( SIZE ):
      for x in self.adjacency( weight, v ):
        if minDist[x] > minDist[v] + weight[v][x]:
          raise Exception( "Negative cycle found" )
 
    return [pred, minDist]
 
 
  #=====================================================================
  # Retrieve all the neighbors of vertex v.
  #=====================================================================
  def adjacency( self, G, v ) :
    result = []
    for x in range( len( G ) ):
      if G[v][x] is not None:
        result.append( x )
 
    return result;

def testBellmanFordWithPositiveEdges():
  fordAlgorithm = BellmanFord()
  weight = [
    [None, 10, None, None, 3],
    [None, None, 2, None, 1],
    [None, None, None, 7, None],
    [None, None, 9, None, None],
    [None, 4, 8, 2, None]
  ]
  source = 0
  result = fordAlgorithm.singleSourceShortestPath( weight, source )
  print result
 
testBellmanFordWithPositiveEdges()
 
  # def testBellmanFordWithNegativeEdges( self ):
  #   fordAlgorithm = BellmanFord()
  #   weight = [
  #     [None, -1, 4, None, None],
  #     [None, None, 3, 2, 2],
  #     [None, None, None, None, None],
  #     [None, 1, 5, None, None],
  #     [None, None, None, -3, None]
  #   ]
  #   source = 0
  #   expResult = [[-1, 0, 1, 4, 1], [0, -1, 2, -2, 1]]
  #   result = fordAlgorithm.singleSourceShortestPath( weight, source )
  #   self.assertEquals( expResult, result )
 
 
 
  # def testBellmanFordWithNegativeCycle( self ):
  #   fordAlgorithm = BellmanFord()
  #   weight = [
  #     [None, -1, 4, None, None],
  #     [None, None, 3, 2, 2],
  #     [None, -6, None, None, None],
  #     [None, 1, 5, None, None],
  #     [None, None, None, -3, None]
  #   ]
  #   source = 0
  #   try :
  #     fordAlgorithm.singleSourceShortestPath( weight, source )
  #   except:
  #     pass
  #   else:
  #     self.fail( "Should have thrown an exception: Negative cycle" )