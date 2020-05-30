import java.util.*;

/*
You are asked to cut off trees in a forest for a golf event. The forest is represented as a non-negative 2D map, in this map:
    1. 0 represents the obstacle can't be reached
    2. 1 represents the ground can be walked through.
    3. The place with number bigger than 1 represents a tree can be walked through,
    and this positive number represents the tree's height.

In one step you can walk in any of the four directions top, bottom, left and right
also when standing in a point which is a tree you can decide whether or not to cut off the tree.

You are asked to cut off all the trees in this forest in the order of tree's height - always cut off the tree with lowest height first.
And after cutting, the original place has the tree will become a grass (value 1).

You will start from the point (0, 0) and you should output the minimum steps you need to walk to cut off all the trees.
If you can't cut off all the trees, output -1 in that situation.
 */
public class Solution {
    int[] dr = {1, -1, 0, 0};
    int[] dc = {0, 0, -1, 1};

    public int cutOffTree(List<List<Integer>> forest) {
        List<int[]> trees = new ArrayList<>();
        int row = forest.size();
        int column = forest.get(0).size();
        // get the information of all trees in the forest such height, and position
        for (int i = 0; i < forest.size(); i++) {
            for (int j = 0; j < forest.get(0).size(); j++) {
                int v = forest.get(i).get(j);
                if (v > 1) {
                    int[] infor = new int[]{v, i, j};
                    trees.add(infor);
                }
            }
        }
        //after we got all the trees, we need to sort it
        Collections.sort(trees, (a, b) -> Integer.compare(a[0], b[0]));
        int sr = 0, sc = 0;
        int answer = 0;
        for (int[] tree : trees) {
            int dist = findDist(forest, sr, sc, tree[1], tree[2]);
            if (dist < 0) return -1;
            answer += dist;
            sr = tree[1];
            sc = tree[2];
        }
        return answer;
    }

    public int findDist(List<List<Integer>> forest, int sr, int sc, int tr, int tc) {

        int R = forest.size();
        int C = forest.get(0).size();
        Queue<int[]> queue = new LinkedList();
        queue.add(new int[]{sr, sc, 0});
        boolean[][] seen = new boolean[R][C];
        seen[sr][sc] = true;
        while (!queue.isEmpty()) {
            int[] node = queue.poll();
            if (node[0] == tr && node[1] == tc) return node[2];
            for (int di = 0; di < 4; di++) {
                int r = node[0] + dr[di];
                int c = node[1] + dc[di];
                if (r >= 0 && r < R && c >= 0 && c < C && !seen[r][c] && forest.get(r).get(c) > 0) {
                    seen[r][c] = true;
                    queue.add(new int[]{r, c, node[2] + 1});
                }
            }
        }
        return -1;
    }

    public void tester() {
        List<List<Integer>> forest1 = new ArrayList();
        ArrayList<Integer> row1 = new ArrayList();
        row1.add(2);
        row1.add(3);
        row1.add(4);
        forest1.add(row1);
        ArrayList<Integer> row2 = new ArrayList();
        row2.add(0);
        row2.add(0);
        row2.add(5);
        forest1.add(row2);
        ArrayList<Integer> row3 = new ArrayList();
        row3.add(8);
        row3.add(7);
        row3.add(6);
        forest1.add(row3);
        System.out.println(cutOffTree(forest1));

        List<List<Integer>> forest2 = new ArrayList();
        row1.set(0, 2);
        row1.set(1, 3);
        row1.set(2, 4);
        row2.set(0, 0);
        row2.set(1, 0);
        row2.set(2, 0);
        row3.set(0, 8);
        row3.set(1, 7);
        row3.set(2, 6);
        forest2.add(row1);
        forest2.add(row2);
        forest2.add(row3);
        System.out.println(cutOffTree(forest2));

    }

    public static void main(String[] args) {
        Solution test = new Solution();
        test.tester();
    }
}
