class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        flood(image, sr, sc, color, image[sr][sc]);
        return image;
    }

    public void flood(int[][] image, int sr, int sc, int color, int initColor){
        if(sr < 0 || sc < 0 || sr >= image.length || sc >= image[0].length){
            return;
        }

        if(image[sr][sc] == color || image[sr][sc] != initColor){
            return;
        }

        image[sr][sc] = color;

        flood(image, sr +1, sc, color, initColor);
    
        flood(image, sr -1, sc, color, initColor);
        
        flood(image, sr, sc +1, color, initColor);
        
        flood(image, sr, sc -1, color, initColor);
    }

}