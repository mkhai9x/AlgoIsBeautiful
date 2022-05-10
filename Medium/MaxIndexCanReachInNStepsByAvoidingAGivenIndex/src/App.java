public class App {
    private static int maximumIndex(int steps, int badIndex) {
        /*
        steps = 4
        badIndex = 6 
          *   *     *        *
        0 1 2 3 4 5 6 7 8 9 10
        If there is no badIndex -> the maximum index will be sum from onn to steps. (i.e 1 + 2 + 3 + 4 = 10)
        If there is a badIndex on the go, the maximum index will happen if we skip the jump when the stepNumber is minimum 
            *     *       *
        0 1 2 3 4 5 6 7 8 9 10
        */
        int maxIndexWithoutBadIndex = steps*(steps + 1)/2;
        int step = 0, jumpAmount = 1;
        while(step < steps) {
            int currentIndex = step + jumpAmount;
            if(currentIndex == badIndex) {
                return maxIndexWithoutBadIndex - 1;
            }
            jumpAmount++;
            
        } 
        return maxIndexWithoutBadIndex;
    }
    public static void main(String[] args) throws Exception {
        System.out.println("Maximum index");
        int steps = 4, badIndex = 6;
        int maxIndex = maximumIndex(steps, badIndex);
        System.out.println(maxIndex);
    }
}
