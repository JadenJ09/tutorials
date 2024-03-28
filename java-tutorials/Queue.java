public class Queue<Item> {
    private Node first;
    private Node last;
    private int N;
    private class Node {
        Item item;
        Node next;
    }
    public boolean isEmpty() {
        return first == null;
    }
    public int size() {
        return N;
    }
    public void enqueue(Item item) {
        Node oldLast = last;
        last = new Node();
        last.item = item;
        last.next = null;
        if (isEmpty()) first = last;
        else oldLast.next = last;
        N++;
    }
    public Item dequeue() {
        Item item = first.item;
        first = first.next;
        if (isEmpty()) last = null;
        N--;
        return item;
    }
   
   public void bfs(Graph g, int sourceNode) {
        boolean[] marked = new boolean[g.sizeOfV()];
        //marked[v]: v has been visited
        int[] distTo = new int[g.sizeOfV()];
        //dist[v]: (current) distance to v
        int[] parentOf = new int[g.sizeOfV()];
        //parentOf[v]: (current) parent node on shortest path to v
        Queue<Integer> queue = new Queue<Integer>();

            for (int v=0; v<g.sizeOfV(); v++) {
                distTo[v] = INFINITY;
                distTo[sourceNode] = 0;
                marked[sourceNode] = true;
                queue.enqueue(sourceNode);
            }

            while (!queue.isEmpty()) {
                int v = queue.dequeue();
                int[] nodesAdjacentToV = g.nodesAdjacentTo(v);

                for (int w=0; w<nodesAdjacentToV.length; w++) {

                    if (!marked[nodesAdjacentToV[w]]) {
                        parentOf[nodesAdjacentToV[w]] = v;
                        distTo[nodesAdjacentToV[w]] = distTo[v] + 1;
                        marked[nodesAdjacentToV[w]] = true;
                        queue.enqueue(nodesAdjacentToV[w]);
                    }
            }   
        }
    }
}