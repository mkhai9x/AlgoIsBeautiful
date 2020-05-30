
/*
You’re testing a new driverless car that is located at the Southwest (bottom-left) corner of an n×n grid.
The car is supposed to get to the opposite, Northeast (top-right), corner of the grid.
Given n, the size of the grid’s axes,
write a function numOfPathsToDest that returns the number of the possible paths the driverless car can take.

The car must abide by the following two rules: it cannot cross the diagonal border.
In other words, in every step the position (i,j) needs to maintain i >= j. See the illustration above for n = 5.
In every step, it may go one square North (up), or one square East (right), but not both. E.g. if the car is at (3,1),
it may go to (3,2) or (4,1).
*/
public class NumberOfPaths {
    public int numOfPathsToDest(int n){
        if(n == 1) return 1;
        int[][] counts = new int[n][n];
        for(int i = 0 ; i< n;i++){
            counts[0][i] = 1;
        }
        for(int i = 1; i < n;i++){
            for(int j = 1; j < n; j++){
                if(j >= i ){
                    counts[i][j] = counts[i-1][j] + counts[i][j-1];
                }
            }
        }
        return counts[n-1][n-1];
    }
    public void tester(){
        System.out.println("Input: n = 1 \nOutput: "+ numOfPathsToDest(1));
        System.out.println("Input: n = 2 \nOutput: "+ numOfPathsToDest(2));
        System.out.println("Input: n = 3 \nOutput: "+ numOfPathsToDest(3));
        System.out.println("Input: n = 4 \nOutput: "+ numOfPathsToDest(4));
        System.out.println("Input: n = 100 \nOutput: "+ numOfPathsToDest(100));

    }
    public static void main(String[] args){
        NumberOfPaths testcase = new NumberOfPaths();
        testcase.tester();
    }
}
