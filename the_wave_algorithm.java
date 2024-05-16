import java.util.LinkedList;
import java.util.Queue;

public class the_wave_algorithm {
    private static final int[][] DIRECTIONS = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };

    public static void wave(int[][] grid, int startX, int startY) {
        int rows = grid.length;
        int cols = grid[0].length;

        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[] { startX, startY });

        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int currX = curr[0];
            int currY = curr[1];

            for (int[] dir : DIRECTIONS) {
                int newX = currX + dir[0];
                int newY = currY + dir[1];

                if (newX >= 0 && newX < rows && newY >= 0 && newY < cols && grid[newX][newY] == 0) {
                    grid[newX][newY] = grid[currX][currY] + 1;
                    queue.add(new int[] { newX, newY });
                }
            }
        }
    }

    public static void main(String[] args) {
        int[][] grid = {
                { 0, 0, 0, 0 },
                { 0, -1, -1, 0 },
                { 0, 0, 0, 0 }
        };

        wave(grid, 0, 0);

        for (int[] row : grid) {
            for (int cell : row) {
                System.out.print(cell + " ");
            }
            System.out.println();
        }
    }
}
