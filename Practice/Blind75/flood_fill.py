class Solution:
    
    def fill(self, image, r, c, color, newColor):
        
        if r < 0 or c < 0 or r >= len(image) or c >= len(image[0]) or image[r][c] == newColor or image[r][c] != color:
            return
        
        else:
            image[r][c] = newColor
            self.fill(image, r+1, c, color, newColor)
            self.fill(image, r-1, c, color, newColor)
            self.fill(image, r, c+1, color, newColor)
            self.fill(image, r, c-1, color, newColor)
        
    
    def floodFill(self, image, sr, sc, newColor):
        
        color = image[sr][sc]
        self.fill(image, sr, sc, color, newColor)
        return image